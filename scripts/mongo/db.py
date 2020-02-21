# from memory_profiler import profile
import pickle
import time
import warnings

import pymongo
import sqlalchemy
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, SimpleStatement
from joblib import Parallel, delayed
from pymongo import MongoClient
from sqlalchemy import Binary, Column, ForeignKey, Integer, String, Table
from tqdm import tqdm

from utils import bench_func


@bench_func
# @profile
def connect_mongo():
    """connect to defualt mongo instance at port 27017

    docker run --name mongo -p 27017:27017 mongo -d

    """

    client = MongoClient('localhost', 27017)
    db = client.ganga_test
    return db


@bench_func
# @profile
def add_jobs_mongo(db, jobs=None, blobs=None, batch_size=False):
    """inserts the jobs in mongo instance"""
    # jobs = [{"data":row} for i, row in enumerate(jobs)]
    if jobs:
        if not batch_size or batch_size > len(jobs):
            try:
                db.jobs.insert_many(jobs)
            except pymongo.errors.BulkWriteError as bwe:
                print(bwe.details)
                raise

            return

        with tqdm(total=len(jobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(jobs)+1, batch_size):
                try:
                    db.jobs.insert_many(jobs[start:batch])
                except pymongo.errors.BulkWriteError as bwe:
                    print(bwe.details)
                    raise

                start = batch
                progress.update(1)


@bench_func
# @profile
def add_blobs_mongo(db, jobs=None, blobs=None, batch_size=False):
    # blobs = [{"data":row} for i, row in enumerate(blobs)]
    if blobs:
        if not batch_size or batch_size > len(blobs):
            try:
                db.blobs.insert_many(blobs)
            except pymongo.errors.BulkWriteError as bwe:
                print(bwe.details)
                raise

            return

        with tqdm(total=len(blobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(blobs)+1, batch_size):
                try:
                    db.blobs.insert_many(blobs[start:batch])
                except pymongo.errors.BulkWriteError as bwe:
                    print(bwe.details)
                    raise

                start = batch
                progress.update(1)



@bench_func
def query_jobs_all_mongo(db, table="jobs"):
    rows = [*db.jobs.find({})]

@bench_func
def query_blobs_all_mongo(db, table="blobs"):
    rows = [*db.blobs.find({})]




@bench_func
def connect_postgres(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object

    sudo docker stop postgres; sudo docker rm postgres; sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres

    '''

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    try:
        con = sqlalchemy.create_engine(url, client_encoding='utf8',  executemany_mode='batch')
        meta = sqlalchemy.MetaData(bind=con, reflect=True)
    except Exception as e:
        if "does not exist" in str(e):
            url = 'postgresql://{}:{}@{}:{}/template1'
            url = url.format(user, password, host, port)
            con = sqlalchemy.create_engine(url, client_encoding='utf8')
            meta = sqlalchemy.MetaData(bind=con, reflect=True)
        else:
            raise e

    return con, meta

@bench_func
def create_tables_postgres(con, meta):
    JOBS = Table(
            f"jobs", meta,
            Column("jid", Integer, primary_key=True),
            Column("status", String),
            Column("name", String),
            Column("subjobs", Integer),
            Column("application", String),
            Column("backend", String),
            Column("backend_actualCE", String),
            Column("comment", String),
            extend_existing=True
        )

    BLOBS = Table(
            f"blobs", meta,
            Column("jid", Integer, ForeignKey("jobs.jid")),
            Column("inputsandbox", Binary),
            Column("outputsandbox", Binary),
            Column("info", Binary),
            Column("comment", Binary),
            Column("time", Binary),
            Column("application", Binary),
            Column("backend", Binary),
            Column("inputfiles", Binary),
            Column("outputfiles", Binary),
            Column("non_copyable_outputfiles", Binary),
            Column("id", Binary),
            Column("status", Binary),
            Column("name", Binary),
            Column("inputdir", Binary),
            Column("outputdir", Binary),
            Column("inputdata", Binary),
            Column("outputdata", Binary),
            Column("splitter", Binary),
            Column("subjobs", Binary),
            Column("master", Binary),
            Column("postprocessors", Binary),
            Column("virtualization", Binary),
            Column("merger", Binary),
            Column("do_auto_resubmit", Binary),
            Column("metadata", Binary),
            Column("been_queued", Binary),
            Column("parallel_submit", Binary),
            extend_existing=True
        )

    meta.create_all(con)
    return JOBS, BLOBS

@bench_func
def add_jobs_postgres(con, JOBS=None, jobs=None, batch_size=250):

    start = 0
    with tqdm(total=int(len(jobs)/batch_size)) as progress:
        for end in range(batch_size, len(jobs)+1, batch_size):
            con.execute(
                JOBS.insert(),
                jobs[start:end]
            )
            progress.set_description(f"{start}-{end}")
            progress.update(1)
            start = end


@bench_func
def add_blobs_postgres(con, BLOBS=None, blobs=None, batch_size=250):
    start = 0
    with tqdm(total=int(len(blobs)/batch_size)) as progress:
        for end in range(batch_size, len(blobs)+1, batch_size):
            con.execute(
                BLOBS.insert(),
                blobs[start:end]
            )
            progress.set_description(f"{start}-{end}")
            progress.update(1)
            start = end


@bench_func
def query_jobs_all_postgres(con, table="jobs"):
    rows = [*con.execute(f"""
        SELECT * from {table}
    """)]


@bench_func
def query_blobs_all_postgres(con, table="blobs"):
    rows = [*con.execute(f"""
        SELECT * from {table}
    """)]





warnings.filterwarnings("ignore", message=" exceeding specified threshold of")



@bench_func
def connect_cassandra():
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
def create_tables_cassandra(session):
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
def add_blobs_cassandra(session, blobs=None, batch_size=50):
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
            progress.set_description(f"{start}-{end}")
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
            for row in blobs[start:end]:
                batch.add(query, row)

            session.execute(batch)
            progress.update(1)
            start = end


@bench_func
def add_jobs_cassandra(session, jobs=None, batch_size=250):
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
def query_jobs_all_cassandra(session, table="JOB"):
    rows = [*session.execute(f"""
        SELECT * from {table}
    """)]

@bench_func
def query_blobs_all_cassandra(session, table="BLOB"):
    rows = [*session.execute(f"""
        SELECT * from {table}
    """)]
