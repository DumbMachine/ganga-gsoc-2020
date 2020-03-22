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

filename = f"../benchmarks/{db}-operations-size-{size}-batch_size-{batch_size}.json"

def bench(size, bench_size, filename):
    if os.path.isfile(filename):
        open("../benchmarks/pid", "w+").write(str(os.getpid()))
    else:
        con, meta = connect_postgres('postgres', 'ganga', 'jobs')
        JOBS, BLOBS = create_tables_postgres(con ,meta)

        jobs, blobs = utils.load_pickle_data_batch(size=size)
        add_jobs_postgres(
            con, JOBS=JOBS, jobs=jobs, batch_size=batch_size
        )

        add_blobs_postgres(
            con, BLOBS=BLOBS, blobs=blobs, batch_size=batch_size
        )

        # query_jobs_all_postgres(con, "jobs")
        # query_blobs_all_postgres(con, "blobs")

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