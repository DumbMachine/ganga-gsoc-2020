import time
import pickle

from tqdm import tqdm
from joblib import Parallel, delayed

import pymongo
from pymongo import MongoClient

from utils import bench_func

@bench_func
def connect_mongo():
    """connect to defualt mongo instance at port 27017

    docker run --name mongo -p 27017:27017 mongo -d

    """

    client = MongoClient('localhost', 27017)
    db = client.ganga_test
    return db

@bench_func
def add_jobs_mongo_loop(db, jobs=None, blobs=None):
    """inserts the jobs in mongo instance"""
    # for i, (row, blob) in enumerate(zip(jobs, blobs)):
    if jobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(jobs):
                row[0] = i+1
                try:
                    db.jobs.insert_one({"data":row})
                except pymongo.errors.DuplicateKeyError as e:
                    print(e)
                    break
                progress.update(1)

@bench_func
def add_blobs_mongo_loop(db, jobs=None, blobs=None):
    if blobs:
        with tqdm(total=len(jobs)) as progress:
            for i, row in enumerate(blobs):
                row['_id'] = i+16
                try:
                    db.jobs.insert_one({"data":row})
                except pymongo.errors.DuplicateKeyError as e:
                    print(e)
                    break
                progress.update(1)

@bench_func
def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):
    """inserts the jobs in mongo instance"""
    if jobs:
        if not batch_size:
            db.jobs.insert_many(jobs)
            return

        with tqdm(total=len(jobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(jobs), batch_size):
                db.jobs.insert_many(jobs[start:batch])
                progress.update(1)


@bench_func
def add_blobs_mongo_batch(db, jobs=None, blobs=None, batch_size=None):            
    if blobs:
        if not batch_size:
            db.blobs.insert_many(blobs)
            return

        with tqdm(total=len(blobs)/batch_size) as progress:
            start = 0
            for batch in range(batch_size, len(jobs), batch_size):
                db.blobs.insert_many(blobs[start:batch])
                progress.update(1)

