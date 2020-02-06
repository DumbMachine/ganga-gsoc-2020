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

SIZE = 100000
DB = "postgres"
jobs, blobs = utils.load_pickle_data(size=SIZE)

session, cluster = cassandra_connection()
session = create_tables(session)


# add_jobs_batch(
#     session, jobs=jobs
# )

add_blobs_batch(
    session, blobs=blobs
)

# add_jobs_loop(
#     session, jobs=jobs
# )

# add_blobs_loop(
#     session, blobs=blobs
# )

if not os.path.isdir("../benchmarks"):
    os.makedirs("./benchmarks")

filename = f"{DB}*.json"
iteration = len(glob(f"../benchmarks/{filename}") )
json.dump(
    utils.TIMES,
    open(f"../benchmarks/{DB}-size-{SIZE}-itertion-{iteration}.json", "w+")
)
# pickle.dump(
#     utils.TIMES,
#     open("")
# )
