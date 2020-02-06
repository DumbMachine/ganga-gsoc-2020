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

# class Timings:
#     time = {}
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
    jobs= [[i]+row[1:] for i, row in enumerate(jobs)]

    _blobs = pickle.load(open("../../data/blobs.pkl", "rb"))[:size]
    blobs = []
    for i, blob in enumerate(_blobs):
        blob["jid"] = i+1
        blobs.append(blob)
    # blobs = [
    #     blobs.update
    # ]
    return jobs, blobs