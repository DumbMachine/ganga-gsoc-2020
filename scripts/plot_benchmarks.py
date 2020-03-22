"""
Run these before:

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from glob import glob

SAVE_LOCATION = "images"
BECHMARKS_LOCATION  = "./bechmarks"

DBS = [
    "mongo",
    "postgres",
    "cassandra"
]

# Run the scripts
sizes = [10, 100, 1000, 10000, 10000, 100000]

data = {
    "mongo": [],
    "postgres": [],
    "cassandra": []

}
for size in sizes:
    for db in data.keys():
        file_stub = f"./benchmarks/{db}-size-{size}-batch_size-*-itertion-*.json"
        files = glob(file_stub)
        data[db].append(files)


    # plot for that size
    filename = f"plot-{size}.png"

print(data)


"""
I will run the benchmrk for the following values:
- SIZES: 10, 100, 1000, 10000
- BATCHS : 1, 10 ,100 ,1000, 10000

"""

#  Plotting the cpu usage
filename = "mongo/mongo_performance.json"
import json

data = json.load(open(filename. 'r'))
