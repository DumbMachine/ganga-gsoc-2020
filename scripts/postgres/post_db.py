from utils import bench_func
import pickle
import sqlalchemy

from tqdm import tqdm
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Binary

@bench_func
def connect_post(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    try:
        con = sqlalchemy.create_engine(url, client_encoding='utf8')
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
def create_tables(con, meta):
    JOBS = Table(
            f"jobs", meta,
            Column("id", Integer, primary_key=True),
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
            Column("jid", Integer, ForeignKey("JOBS.id")),
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


@bench_func
def add_jobs_post_loop(con, jobs=None, blobs=None):
    """inserts the job data in a loop"""
    if jobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(jobs):
                row[0] = i+1
                insert_job = JOBS.insert().values(row)
                try:
                    con.execute(insert_job)
                except Exception as e:
                    print(e)
                    break
                progress.update(1)

# @bench_func
# def add_blobs_post_loop(db, jobs=None, blobs=None):

# @bench_func
# def add_blobs_post_batch(db, jobs=None, blobs=None, batch_size=None):
# @bench_func
# def add_blobs_post_batch(db, jobs=None, blobs=None, batch_size=None):