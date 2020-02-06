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
jobs, blobs = utils.load_pickle_data(size=SIZE)
db = connect_mongo()

if BATCH_SIZE:
    add_jobs_batch(
        db, jobs=jobs, batch_size=BATCH_SIZE
    )
    add_blobs_batch(
        db, blobs=blobs, batch_size=BATCH_SIZE
    )
else:
    add_jobs_loop(
        db, jobs=jobs
    )
    add_blobs_loop(
        db, blobs=blobs
    )

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