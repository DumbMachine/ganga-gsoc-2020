import os
import sys
import json
import utils
import pickle

from db import *
from glob import glob
"""
Benching Cassandra
"""

SIZE = 10000
DB = "postgres"

if len(sys.argv) > 2:
    SIZE, BATCH_SIZE = int(sys.argv[1]), int(sys.argv[2])

jobs, blobs = utils.load_pickle_data(size=SIZE)
session, cluster = cassandra_connection()
session = create_tables(session)


if BATCH_SIZE:
    print("DOING BATCH SIZE")
    add_jobs_batch(
        session, jobs=jobs, batch_size=BATCH_SIZE
    )
    add_blobs_batch(
        session, blobs=blobs, batch_size=BATCH_SIZE
    )
else:
    print(f"DOING LINEAR {SIZE}")
    add_jobs_loop(
        session, jobs=jobs
    )
    add_blobs_loop(
        session, blobs=blobs
    )
query_jobs_all(session, "JOB")
query_blobs_all(session, "BLOB")

if not os.path.isdir("../benchmarks"):
    os.makedirs("./benchmarks")

filename = f"../benchmarks/*-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
json.dump(
    utils.TIMES,
    open(f"../benchmarks/{DB}-size-{SIZE}-batch_size-{BATCH_SIZE}-itertion-{iteration}.json", "w+")
)
