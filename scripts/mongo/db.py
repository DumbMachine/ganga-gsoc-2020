import time
# from memory_profiler import profile
import pickle

from tqdm import tqdm
from joblib import Parallel, delayed

import pymongo
from pymongo import MongoClient

from utils import bench_func

@bench_func
# @profile
def connect_mongo():
    """connect to defualt mongo instance at port 27017

    docker run --name mongo -p 27017:27017 mongo -d

    """

    client = MongoClient('localhost', 27017)
    db = client.ganga_test
    return db

@bench_func
# @profile
def add_jobs_loop(db, jobs=None, blobs=None):
    """inserts the jobs in mongo instance"""
    # for i, (row, blob) in enumerate(zip(jobs, blobs)):
    if jobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(jobs):
                try:
                    # db.jobs.insert_one({"data":row})
                    db.jobs.insert_one(row)
                except pymongo.errors.DuplicateKeyError as e:
                    print(e)
                    break
                progress.update(1)

@bench_func
# @profile
def add_blobs_loop(db, jobs=None, blobs=None):
    if blobs:
        with tqdm(total=len(blobs)) as progress:
            for i, row in enumerate(blobs):
                row['_id'] = i+16
                try:
                    # db.blobs.insert_one({"data":row})
                    db.blobs.insert_one(row)
                except pymongo.errors.DuplicateKeyError as e:
                    print(e)
                    break
                progress.update(1)

@bench_func
# @profile
def add_jobs_batch(db, jobs=None, blobs=None, batch_size=False):
    """inserts the jobs in mongo instance"""
    # jobs = [{"data":row} for i, row in enumerate(jobs)]
    if jobs:
        if not batch_size or batch_size > len(jobs):
            try:
                db.jobs.insert_many(jobs)
            except pymongo.errors.BulkWriteError as bwe:
                print(bwe.details)
                raise

            return

        with tqdm(total=len(jobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(jobs)+1, batch_size):
                try:
                    db.jobs.insert_many(jobs[start:batch])
                except pymongo.errors.BulkWriteError as bwe:
                    print(bwe.details)
                    raise

                start = batch
                progress.update(1)


@bench_func
# @profile                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def add_blobs_batch(db, jobs=None, blobs=None, batch_size=False):
    # blobs = [{"data":row} for i, row in enumerate(blobs)]
    if blobs:
        if not batch_size or batch_size > len(blobs):
            try:
                db.blobs.insert_many(blobs)
            except pymongo.errors.BulkWriteError as bwe:
                print(bwe.details)
                raise

            return

        with tqdm(total=len(blobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(blobs)+1, batch_size):
                try:
                    db.blobs.insert_many(blobs[start:batch])
                except pymongo.errors.BulkWriteError as bwe:
                    print(bwe.details)
                    raise

                start = batch
                progress.update(1)



@bench_func
def query_jobs_all(db, table="jobs"):
    rows = [*db.jobs.find({})]

@bench_func
def query_blobs_all(db, table="blobs"):
    rows = [*db.blobs.find({})]


