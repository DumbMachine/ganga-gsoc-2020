import os
import sys
import json
import utils
import pickle

from db import *
from glob import glob
"""
Benching MOngoDB
"""

SIZE = 10000
DB = "postgres"
BATCH_SIZE = 250

if len(sys.argv) > 2:
    SIZE, BATCH_SIZE = int(sys.argv[1]), int(sys.argv[2])

con, meta = connect('postgres', 'ganga', 'jobs')
JOBS, BLOBS = create_tables(con ,meta)

if BATCH_SIZE:
    print("DOING BATCH SIZE")
    jobs, blobs = utils.load_pickle_data(size=SIZE)
    add_jobs_batch(
        con, JOBS=JOBS, jobs=jobs, batch_size=BATCH_SIZE
    )

    add_blobs_batch(
        con, BLOBS=BLOBS, blobs=blobs, batch_size=BATCH_SIZE
    )

else:
    print("DOING LINEAR")
    jobs, blobs = utils.load_pickle_data_linear(size=SIZE)
    add_jobs_loop(
        con, JOBS=JOBS, jobs=jobs
    )
    add_blobs_loop(
        con, BLOBS=BLOBS, blobs=blobs
    )

query_jobs_all(con, "jobs")
query_blobs_all(con, "blobs")

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
json.dump(
    utils.TIMES,
    open(f"../benchmarks/{DB}-size-{SIZE}-batch_size-{BATCH_SIZE}-itertion-{iteration}.json", "w+")
)
