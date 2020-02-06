import time
import pickle

from tqdm import tqdm
from utils import bench_func
from joblib import Parallel, delayed

from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement




@bench_func
def cassandra_connection():
    """
    Connection object for Cassandra
    :return: session, cluster
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
        id INT PRIMARY KEY, status varchar, name varchar, subjobs INT, application varchar,
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
        INSERT INTO JOB(id, status, name, subjobs, application, backend, backend_actualCE, comment)
        VALUES          (?,      ?,    ?,       ?,           ?,       ?,                ?,       ?)
    """)

    if jobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(jobs):
                row[0] = i+1
                try:
                    session.execute(query.bind(row))
                except Exception as e:
                    print(e)
                    break
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
                try:
                    session.execute(query.bind(blob))
                except Exception as e:
                    print(e)
                    break
                progress.update(1)

# @bench_func
# def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):
#     """inserts the jobs in mongo instance"""
#     if jobs:
#         if not batch_size:
#             db.jobs.insert_many(jobs)
#             return

#         with tqdm(total=len(jobs)/batch_size) as progress:
#             start = 0
#             for batch in range(batch_size, len(jobs), batch_size):
#                 db.jobs.insert_many(jobs[start:batch])
#                 progress.update(1)


# @bench_func
# def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):
#     if blobs:
#         if not batch_size:
#             db.blobs.insert_many(blobs)
#             return

#         with tqdm(total=len(blobs)/batch_size) as progress:
#             start = 0
#             for batch in range(batch_size, len(jobs), batch_size):
#                 db.blobs.insert_many(blobs[start:batch])
#                 progress.update(1)

