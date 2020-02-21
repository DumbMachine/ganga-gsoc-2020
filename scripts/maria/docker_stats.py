import os
import json
from glob import glob
import time
import docker
import matplotlib.pyplot as plt

# def docker_stats(name, interval, filename):
#     client = docker.from_env()
#     if not os.path.isfile(filename):
#         json.dump({"stats": []}, open(filename, "w"))
#     while True:
#         found_container = False
#         time.sleep(interval)

#         for container in client.containers.list():
#             if container.name == name:
#                 try:
#                     found_container = True
#                     data = json.load(open(filename, "r"))
#                     data["stats"].append(container.stats(stream=False))
#                     json.dump(data, open(filename, "w+"))
#                 except json.decoder.JSONDecodeError:
#                     print(f"I guess you have stopped {name} container now")

#         if not found_container:
#             print("Coudn't find the container, exiting now")
#             exit(0)

import subprocess

def docker_stats(dummy1, dummy2,filename):
    print("Docker thread is listening now")
    filename = filename.replace("operations", "performance")
    name="mongo"
    interval = 0
    things = {
        'CONTAINER ID': None,
        'NAME': None,
        'CPU %': None,
        'MEM USAGE/LIMIT': None,
        'MEM %': None,
        'NET I/O': None,
        'BLOCK I/O': None,
        'PIDS': None
    }
    if not os.path.isfile(filename):
        json.dump({"stats": []}, open(filename, "w+"))

    proc = subprocess.Popen(["sudo", "docker",  "stats"],stdout=subprocess.PIPE)
    while True:
        time.sleep(interval)
        line = proc.stdout.readline()
        if not line:
            break
        if "CPU %" not in line.decode("utf-8"):
            items = line.decode("utf-8").split()
            things["CONTAINER ID"] = items[0]
            things['NAME'] = items[1]
            things['CPU %'] = items[2]
            things['MEM USAGE/LIMIT'] = " ".join(items[3:6])
            things['MEM %'] = items[6]
            things['NET I/O'] = " ".join(items[7:10])
            things['BLOCK I/O'] = " ".join(items[10:-2])
            things['PIDS'] = items[-1]

            data = json.load(open(filename, "r"))
            data["stats"].append(things)
            json.dump(data, open(filename, "w+"))


        pids = glob("../benchmarks/pid")
        if pids:
            for pid in pids:
                os.remove(pid)
            print("exiting the docker thread nw")
            raise SystemError


# MAX: Mark the max and min usage
def plt_docker_db(filename):
    """
    docker_stats("mongo", 1, "mongo_performance.json")
    usage: $
    """
    data = json.load(open(filename, "r"))['stats']
        #     {
        #     "NAME": "mongo",
        #     "CPU %": "0.38%",
        #     "MEM USAGE/LIMIT": "73.32MiB / 7.66GiB",
        #     "MEM %": "0.93%",
        #     "NET I/O": "32.3kB / 0B",
        #     "BLOCK I/O": "8.91MB /",
        #     "PIDS": "32"
        # },

    cpu_usage = [float(i['CPU %'][:-1]) for i in data]
    mem_usage_percent = [float(i['MEM %'][:-1]) for i in data]

    mem_usage_total=[]
    for mem in [i['MEM USAGE/LIMIT'].split("/")[0] for i in data]:
        mem = mem.replace("kiB", "")
        if "MiB" in mem:
            mem = float(mem.replace("MiB", ""))*1024
        mem_usage_total.append(mem)


    io = []
    for (i, j) in [i['BLOCK I/O'].replace("0B", "0").split("/") for i in data]:
        if i == '':
            i = 0
        else:
            if "kB" in i:
                i = float(i.replace("kB", "")) # for kbs
            elif "MB" in i:
                i = float(i.replace("MB", ""))*1024 # for kbs
            elif "GB" in i:
                i = float(i.replace("GB", ""))*1024*1024 # for kbs

        if j == '':
            j = 0
        else:
            if "kB" in j:
                j = float(j.replace("kB", "")) # for kbs
            elif "MB" in j:
                j = float(j.replace("MB", ""))*1024 # for kbs
            elif "GB" in j:
                j = float(j.replace("GB", ""))*1024*1024 # for kbs
        io.append([i, j])


    net_io = []
    for (i, j) in [i['NET I/O'].replace("0B", "0").split("/") for i in data]:
        if i == '':
            i = 0
        else:
            if "kB" in i:
                i = float(i.replace("kB", "")) # for kbs
            elif "MB" in i:
                i = float(i.replace("MB", ""))*1024 # for kbs
            elif "GB" in i:
                i = float(i.replace("GB", ""))*1024*1024 # for kbs

        if j == '':
            j = 0
        else:
            if "kB" in j:
                j = float(j.replace("kB", "")) # for kbs
            elif "MB" in j:
                j = float(j.replace("MB", ""))*1024 # for kbs
            elif "GB" in j:
                j = float(j.replace("GB", ""))*1024*1024 # for kbs
        net_io.append([i, j])



    plt.plot(cpu_usage, label="cpu_usage")
    plt.plot(mem_usage_percent, label="mem_usage")
    plt.legend(loc="upper left")
    plt.savefig(f"../images/PLOT-USGE-PRCNT-{filename.split('/')[-1]}.png", dpi=100)
    plt.clf()

    plt.plot(mem_usage_total, label="mem_usage_total")
    plt.plot([i[0] for i in io], label="io")
    plt.plot([i[0] for i in net_io], label="net_io")
    plt.legend(loc="upper left")
    plt.savefig(f"../images/PLOT-USGE-{filename.split('/')[-1]}.png", dpi=100)




def plot_mem_usage_percent(size=10000, batch_size=1):
    if not os.path.isdir("./images"):
        os.makedirs("./images")
    filename_performance = f"./benchmarks/*-performance-size-{size}-batch_size-{batch_size}.json"
    filename_time = f"./benchmarks/*-operations-size-{size}-batch_size-{batch_size}.json"
    files_performance = glob(filename_performance)
    files_time = glob(filename_time)
    plot_points = {}
    for file, file2 in zip(files_performance, files_time):
        data = json.load(open(file, 'r'))['stats']
        timing = sum(json.load(open(file2, 'r')).values())
        mem_usage_percent = [float(i['MEM %'][:-1]) for i in data]
        plot_points[file.split("/")[-1].split("-")[0]] = {"data": mem_usage_percent, "time": timing}


    for key in plot_points.keys():
        plt.plot(plot_points[key]['data'], label=key+"--"+str(plot_points[key]['time']))

    plt.title("mem_usage_percent")
    plt.legend(loc="upper left")
    plt.savefig(f"./images/mem_usage_percent-{size}-{batch_size}.png", dpi=100)
