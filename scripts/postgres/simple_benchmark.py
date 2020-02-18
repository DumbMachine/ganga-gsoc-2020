import psutil
import os
import sys
import json
import utils
import pickle
from db import *
from glob import glob
from joblib import Parallel, delayed

"""
Benching MOngoDB
"""

size = 10000
db = "postgres"
batch_size = 250

if len(sys.argv) > 2:
    size, batch_size = int(sys.argv[1]), int(sys.argv[2])

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*operations-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}-itertion-{iteration}.json"

def bench(size, bench_size, filename):
    db="postgres"
    con, meta = connect('postgres', 'ganga', 'jobs')
    JOBS, BLOBS = create_tables(con ,meta)

    if batch_size:
        print("DOING BATCH size")
        jobs, blobs = utils.load_pickle_data(size=size)
        add_jobs_batch(
            con, JOBS=JOBS, jobs=jobs, batch_size=batch_size
        )

        add_blobs_batch(
            con, BLOBS=BLOBS, blobs=blobs, batch_size=batch_size
        )

    else:
        print("DOING LINEAR")
        jobs, blobs = utils.load_pickle_data_linear(size=size)
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

    json.dump(
        utils.TIMES,
        open(filename, "w+")
    )
    open("../benchmarks/pid", "w+").write(str(os.getpid()))

funcs = [utils.docker_stats, bench]


try:
    Parallel(n_jobs=2, backend="threading")(delayed(func)(size, batch_size, filename) for func in funcs)
except psutil.AccessDenied:
    print("Killed both threads, successfully exiting now")