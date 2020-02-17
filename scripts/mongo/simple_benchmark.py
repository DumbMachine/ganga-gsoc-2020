import psutil
import os
import sys
import json
import utils
import pickle
from docker_stats import *
from threading import Thread
from db import *
from glob import glob
"""
Benching MOngoDB
"""

size = 10000
batch_size = size+2
db = "mongo"

if len(sys.argv) > 2:
    size, batch_size = int(sys.argv[1]), int(sys.argv[2])

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/*operations-size-*-batch_size-*-itertion-*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}-itertion-{iteration}.json"

def bench(size, batch_size, filename):
    jobs, blobs = utils.load_pickle_data_batch(size=size)
    db = connect()

    print(utils.TIMES)
    if batch_size:
        print("DOING BATCH SIZE")
        add_jobs_batch(
            db, jobs=jobs, batch_size=batch_size
        )
        add_blobs_batch(
            db, blobs=blobs, batch_size=batch_size
        )
    else:
        print("DOING LINEAR")
        add_jobs_loop(
            db, jobs=jobs
        )
        add_blobs_loop(
            db, blobs=blobs
        )
    print(utils.TIMES)

    query_jobs_all(db, "jobs")
    query_blobs_all(db, "blobs")
    print(utils.TIMES)

    if not os.path.isdir("../benchmarks"):
        os.makedirs("../benchmarks")


    json.dump(
        utils.TIMES,
        open(filename, "w+")
    )
    open("../benchmarks/pid", "w+").write(str(os.getpid()))


funcs = [docker_stats, bench]


try:
    Parallel(n_jobs=2, backend="multiprocessing")(delayed(func)(size, batch_size, filename) for func in funcs)
except psutil.AccessDenied:
    print("Killed both threads, successfully exiting now")