import copy
import time
import pickle

from tqdm import tqdm
from joblib import Parallel, delayed

import pymongo
from pymongo import MongoClient

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

import sqlalchemy
from sqlalchemy import Binary, Column, ForeignKey, Integer, String, Table

TIMES = {}

def bench_func(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} was {time} seconds."
        print(msg.format(func=func.__name__,
                         time=runtime))
        TIMES[func.__name__] = runtime
        return value
    return function_timer



@bench_func
def load_pickle_data(size=100000):
    jobs = pickle.load(open("../../data/rows.pkl", "rb"))[:size]
    rows = []
    for itr, job in enumerate(jobs):
        row = {}
        for header, value in zip(
            ['jid', 'status', 'name', 'subjobs', 'application',
            'backend', 'backend_actualCE', 'comment'],
            job
        ):
            row[header] = value

        row["jid"] = itr
        rows.append(row)
    jobs = rows


    _blobs = pickle.load(open("../../data/blobs.pkl", "rb"))[:size]
    blobs = []
    for i, blo in enumerate(_blobs):
        # FIXME: Dirty patch, for some reason any change to a single element fof blobs array, goes to all the elements. I decided to create copies after failing to debug this at that time.
        blob = copy.deepcopy(blo)
        blob["jid"] = i
        blobs.append(blob)
    return jobs, blobs