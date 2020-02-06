import os
import sys
import json
import utils
import pickle

from mongo_db import *
from glob import glob
"""
Benching MOngoDB
"""

SIZE = 100000
DB = "mongo"
jobs, blobs = utils.load_pickle_data(size=SIZE)
db = connect_mongo()
add_jobs_mongo_loop(
    db, jobs=jobs
)
add_blobs_mongo_loop(
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