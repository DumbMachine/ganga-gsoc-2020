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
BATCH_SIZE = SIZE+2
DB = "mongo"

if len(sys.argv) > 2:
    SIZE, BATCH_SIZE = int(sys.argv[1]), int(sys.argv[2])

jobs, blobs = utils.load_pickle_data_batch(size=SIZE)
db = connect()

if BATCH_SIZE:
    print("DOING BATCH SIZE")
    add_jobs_batch(
        db, jobs=jobs, batch_size=BATCH_SIZE
    )
    add_blobs_batch(
        db, blobs=blobs, batch_size=BATCH_SIZE
    )
else:
    print("DOING LINEAR")
    add_jobs_loop(
        db, jobs=jobs
    )
    add_blobs_loop(
        db, blobs=blobs
    )

query_jobs_all(db, "jobs")
query_blobs_all(db, "blobs")

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
json.dump(
    utils.TIMES,
    open(f"../benchmarks/{DB}-size-{SIZE}-batch_size-{BATCH_SIZE}-itertion-{iteration}.json", "w+")
)