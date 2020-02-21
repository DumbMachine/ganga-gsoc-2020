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

size = 10000
db = "cassandra"
batch_size = 250


if len(sys.argv) > 2:
    size, batch_size = int(sys.argv[1]), int(sys.argv[2])

if batch_size > 1000:
    raise Exception("Getting an error when trying to pass 1000 itertions")
if not os.path.isdir("../benchmarks"):
    os.makedirs("../benchmarks")

filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}.json"


def bench(size, batch_size, filename):
    if os.path.isfile(filename):
        open("../benchmarks/pid", "w+").write(str(os.getpid()))
    else:
        jobs, blobs = utils.load_pickle_data(size=size)
        print("starting to conniet")
        session, _ = connect_cassandra()
        session = create_tables_cassandra(session)

        add_jobs_cassandra(
            session, jobs=jobs, batch_size=batch_size
        )
        add_blobs_cassandra(
            session, blobs=blobs, batch_size=batch_size
        )

        # query_jobs_all_cassandra(session, "JOB")
        # query_blobs_all_cassandra(session, "BLOB")

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
