import os
import sys
import json
import utils
import pickle

from post_db import *
from glob import glob
"""
Benching MOngoDB
"""

SIZE = 100000
DB = "postgres"
jobs, blobs = utils.load_pickle_data(size=SIZE)

con, meta = connect_post('postgres', 'mysecretpassword', 'jobs')
create_tables(con ,meta)

add_jobs_post_loop(
    con, jobs=jobs
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