from utils import bench_func
import pickle
import sqlalchemy

from tqdm import tqdm
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Binary

@bench_func
def connect_post(user, password, db, host='localhost', port=5432):
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
def create_tables(con, meta):
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
def add_jobs_loop(con, JOBS=None, BLOBS=None, jobs=None, blobs=None):
    """inserts the job data in a loop"""
    if jobs:
        with tqdm(total=len(jobs)) as progress:
            progress.set_description("inserting jobs")
            for i, row in enumerate(jobs):
                row[0] = i+1
                insert_job = JOBS.insert().values(row)
                con.execute(insert_job)
                progress.update(1)

@bench_func
def add_blobs_loop(con, BLOBS=None, blobs=None):
    """inserts the job data in a loop"""
    if blobs:
        with tqdm(total=len(blobs)) as progress:
            progress.set_description("inserting blobs")
            for i, row in enumerate(blobs):
                insert_blob = BLOBS.insert().values(row)
                con.execute(insert_blob)
                progress.update(1)

@bench_func
def add_jobs_batch(con, JOBS=None, jobs=None, batch_size=250):

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
def add_blobs_batch(con, BLOBS=None, blobs=None, batch_size=250):
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
def query_jobs_all(con, table="jobs"):
    rows = [*con.execute(f"""
        SELECT * from {table}
    """)]


@bench_func
def query_blobs_all(con, table="blobs"):
    rows = [*con.execute(f"""
        SELECT * from {table}
    """)]


