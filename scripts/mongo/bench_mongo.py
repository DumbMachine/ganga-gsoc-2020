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
batch_size = size+2
db = "mongo"

if len(sys.argv) > 2:
    size, batch_size = int(sys.argv[1]), int(sys.argv[2])

if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}.json"

def bench(size, batch_size, filename):
    if os.path.isfile(filename):
        open("../benchmarks/pid", "w+").write(str(os.getpid()))
    else:
        jobs, blobs = utils.load_pickle_data_batch(size=size)
        db = connect_mongo()

        add_jobs_mongo(
            db, jobs=jobs, batch_size=batch_size
        )
        add_blobs_mongo(
            db, blobs=blobs, batch_size=batch_size
        )

        # query_jobs_all_mongo(db, "jobs")
        # query_blobs_all_mongo(db, "blobs")

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
except TypeError:
    print("Killed both threads, successfully exiting now")

