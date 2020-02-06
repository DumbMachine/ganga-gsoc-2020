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