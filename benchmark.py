"""
This script is for benchmarking the database with 3 differnet sizes

TODO: Use joblib to parallelize the process of making multiple databases

"""
import pick




le
import sqlalchemy
from utils import *
from time import time
from tqdm import tqdm
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Binary

SIZES = [
    10,
    100,
    1000,
    10000,
    100000,
    1000000
]

JOBS = {}
BLOBS = {}

con, meta = connect('ganga', 'ganga', 'jobs')

jobs = pickle.load(open("rows.pkl", "rb"))
blobs = pickle.load(open("blobs.pkl", "rb"))

for size in SIZES:
    JOBS[size] = Table(
                 f"jobs-{size}", meta,
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

    BLOBS[size] = Table(
                f"blobs-{size}", meta,
                Column("jid", Integer, ForeignKey("jobs.id")),
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

def fill_database(size, progress=False):
    """Will fill the tables with size=size"""

    _jobs = jobs[:size]
    _blobs = blobs[:size]

    if not progress:
        with tqdm(total=size) as progress:
            for i, (row, blob) in enumerate(zip(_jobs, _blobs)):
                row[0] = i+1
                insert_job = JOBS[size].insert().values(row)
                insert_blob = BLOBS[size].insert().values(list(blob.values()))
                blob['jid'] = i+1

                try:
                    con.execute(insert_job)
                    con.execute(insert_blob)
                except Exception as e:
                    print(f"[ERROR] {e}")

def search_database(jid, size):
    """Searches both the databases and returns the time taken for querying each one of them"""

    table_jobs = meta.tables[f'jobs-{size}']
    table_blobs = meta.tables[f'blobs-{size}']

    st = time()
    clause  = table_jobs.select().where(
        table_jobs.c.id == jid
    )
    ct = time() - st

    st = time()
    clause  = table_blobs.select().where(
        table_blobs.c.jid == jid
    )
    qt = time() - st

    return (ct, qt)
