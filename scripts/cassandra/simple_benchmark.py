import json
import os
import pickle
import sys
from glob import glob

import psutil
from joblib import Parallel, delayed

import utils
from db import *

"""
Benching Cassandra
"""

SIZE = 10000
DB = "cassandra"

if len(sys.argv) > 2:
    SIZE, BATCH_SIZE = int(sys.argv[1]), int(sys.argv[2])


if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
json.dump(
    utils.TIMES,
    open(f"../benchmarks/{DB}-size-{SIZE}-batch_size-{BATCH_SIZE}-itertion-{iteration}.json", "w+")
)


size = 10000
batch_size = size+2
db = "cassandra"

if len(sys.argv) > 2:
    size, batch_size = int(sys.argv[1]), int(sys.argv[2])

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*operations-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}-itertion-{iteration}.json"

def bench(size, batch_size, filename):
    jobs, blobs = utils.load_pickle_data(size=size)
    session, _ = connect()
    session = create_tables(session)

    add_jobs_batch(
        session, jobs=jobs, batch_size=batch_size
    )
    add_blobs_batch(
        session, blobs=blobs, batch_size=batch_size
    )

    query_jobs_all(session, "JOB")
    query_blobs_all(session, "BLOB")

    if not os.path.isdir("../benchmarks"):
        os.makedirs("../benchmarks")


    json.dump(
        utils.TIMES,
        open(filename, "w+")
    )
    open("../benchmarks/pid", "w+").write(str(os.getpid()))


funcs = [utils.docker_stats, bench]

try:
    Parallel(n_jobs=2, backend="multiprocessing")(delayed(func)(size, batch_size, filename) for func in funcs)
except TypeError:
    print("Killed both threads, successfully exiting now")
