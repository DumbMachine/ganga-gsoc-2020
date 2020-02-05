import os
import sys
import utils
import pickle

from mongo_db import *
from glob import glob
"""
Benching MOngoDB
"""

SIZE = ""
jobs, blobs = utils.load_pickle_data(size=SIZE)
db = connect_mongo()
add_jobs_mongo_loop(
    db, jobs=jobs
)
add_blobs_mongo_loop(
    db, blobs=blobs
)

if not os.path.isdir("./benchmarks"):
    os.makedirs("./benchmarks")

filename = f"*-iteration-*.pkl"
iteration = glob("./bechmarks")
pickle.dump(
    utils.TIMES,
    open("")
)
print(utils.TIMES)