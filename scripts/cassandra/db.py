import time
import pickle

from tqdm import tqdm
from utils import bench_func
from joblib import Parallel, delayed

from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement, BatchStatement

import warnings
warnings.filterwarnings("ignore", message=" exceeding specified threshold of")



@bench_func
def cassandra_connection():
    """
    Connection object for Cassandra
    :return: session, cluster


    sudo docker run --name cassandra -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra

    """
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS fakehealthcareorg
        WITH REPLICATION =
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
        """)
    session.set_keyspace('fakehealthcareorg')
    return session, cluster


@bench_func
def create_tables(session):
    session.execute("""CREATE TABLE IF NOT EXISTS JOB(
        jid INT PRIMARY KEY, status varchar, name varchar, subjobs INT, application varchar,
        backend varchar, backend_actualCE varchar, comment varchar
    )""")
    session.execute("""
        CREATE TABLE IF NOT EXISTS BLOB(
            jid INT PRIMARY KEY, inputsandbox BLOB, outputsandbox BLOB, info BLOB,
            comment BLOB, time BLOB, application BLOB, backend BLOB,
            inputfiles BLOB, outputfiles BLOB, non_copyable_outputfiles BLOB,
            id BLOB, status BLOB, name BLOB, inputdir BLOB, outputdir BLOB, inputdata BLOB,
            outputdata BLOB, splitter BLOB, subjobs BLOB, master BLOB, postprocessors BLOB,
            virtualization BLOB, merger BLOB, do_auto_resubmit BLOB, metadata BLOB, been_queued BLOB,
            parallel_submit BLOB
        )
    """)
    return session

@bench_func
def add_jobs_loop(session, jobs=None, blobs=None):
    """inserts the jobs in mongo instance"""
    # for i, (row, blob) in enumerate(zip(jobs, blobs)):
    query = session.prepare("""
        INSERT INTO JOB(jid, status, name, subjobs, application, backend, backend_actualCE, comment)
        VALUES          (?,      ?,    ?,       ?,           ?,       ?,                ?,       ?)
    """)

    if jobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(jobs):
                row[0] = i+1
                session.execute(query.bind(row))
                progress.update(1)

@bench_func
def add_blobs_loop(session, jobs=None, blobs=None):
    query = session.prepare("""
        INSERT INTO BLOB(
            jid, inputsandbox, outputsandbox, info,
            comment, time, application, backend,
            inputfiles, outputfiles, non_copyable_outputfiles,
            id, status, name, inputdir, outputdir, inputdata,
            outputdata, splitter, subjobs, master, postprocessors,
            virtualization, merger, do_auto_resubmit, metadata, been_queued,
            parallel_submit
        ) VALUES (
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?
        )""")

    if blobs:
        with tqdm(total=len(blobs)) as progress:
            for i, blob in enumerate(blobs):
                blob['jid'] = i+1
                session.execute(query.bind(blob))
                progress.update(1)

@bench_func
def add_blobs_batch(session, blobs=None, batch_size=250):
    query = session.prepare("""
        INSERT INTO BLOB(
            jid, inputsandbox, outputsandbox, info,
            comment, time, application, backend,
            inputfiles, outputfiles, non_copyable_outputfiles,
            id, status, name, inputdir, outputdir, inputdata,
            outputdata, splitter, subjobs, master, postprocessors,
            virtualization, merger, do_auto_resubmit, metadata, been_queued,
            parallel_submit
        ) VALUES (
            ?, ?, ?, ?,
            ?, ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?
        )""")
    start = 0
    with tqdm(total=int(len(blobs)/batch_size)) as progress:
        for end in range(batch_size, len(blobs)+1, batch_size):
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
            for row in blobs[start:end]:
                batch.add(query, row)

            session.execute(batch)
            progress.set_description(f"{start}-{end}")
            progress.update(1)
            start = end


@bench_func
def add_jobs_batch(session, jobs=None, batch_size=250):
    query = session.prepare("""
        INSERT INTO JOB(jid, status, name, subjobs, application, backend, backend_actualCE, comment)
        VALUES          (?,      ?,    ?,       ?,           ?,       ?,                ?,       ?)
    """)
    start = 0
    with tqdm(total=int(len(jobs)/batch_size)) as progress:
        for end in range(batch_size, len(jobs)+1, batch_size):
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
            for row in jobs[start:end]:
                batch.add(query, row)

            session.execute(batch)
            progress.set_description(f"{start}-{end}")
            progress.update(1)
            start = end


@bench_func
def query_jobs_all(session, table="JOB"):
    rows = [*session.execute(f"""
        SELECT * from {table}
    """)]

@bench_func
def query_blobs_all(session, table="BLOB"):
    rows = [*session.execute(f"""
        SELECT * from {table}
    """)]

