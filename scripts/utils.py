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
def connect_mongo():
    """connect to defualt mongo instance at port 27017

    docker run --name mongo -p 27017:27017 mongo -d

    """

    client = MongoClient('localhost', 27017)
    db = client.ganga_test
    return db

@bench_func
def load_pickle_data(size=100000):
    jobs = pickle.load(open("../rows.pkl", "rb"))[:size]
    jobs= [[i]+row[1:] for i, row in enumerate(jobs)]

    _blobs = pickle.load(open("../blobs.pkl", "rb"))[:size]
    blobs = []
    for i, blob in enumerate(_blobs):
        blob["jid"] = i+1
        blobs.append(blob)
    # blobs = [
    #     blobs.update
    # ]
    return jobs, blobs

@bench_func
def add_jobs_mongo_loop(db, jobs=None, blobs=None):
    """inserts the jobs in mongo instance"""
    # for i, (row, blob) in enumerate(zip(jobs, blobs)):
    if jobs:
        for i, row in enumerate(jobs):
            row[0] = i+1
            try:
                db.jobs.insert_one({"data":row})
            except pymongo.errors.DuplicateKeyError as e:
                print(e)
                break

@bench_func
def add_blobs_mongo_loop(db, jobs=None, blobs=None):
    if blobs:
        for i, row in enumerate(blobs):
            row['_id'] = i+1
            try:
                db.jobs.insert_one({"data":row})
            except pymongo.errors.DuplicateKeyError as e:
                print(e)
                break

@bench_func
def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):
    """inserts the jobs in mongo instance"""
    if jobs:
        if not batch_size:
            db.jobs.insert_many(jobs)
            return

        start = 0
        for batch in range(batch_size, len(jobs), batch_size):
            db.jobs.insert_many(jobs[start:batch])


@bench_func
def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):            
    if blobs:
        if not batch_size:
            db.blobs.insert_many(blobs)
            return

        start = 0
        for batch in range(batch_size, len(jobs), batch_size):
            db.blobs.insert_many(blobs[start:batch])

