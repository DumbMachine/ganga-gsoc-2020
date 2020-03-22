import string

file_path = "job.string"
job_dict = {} # will represent the schema
schema_values = [
    "comment",
    "id",
    "outputsandbox",
    "status",
    "name",
    "inputdir",
    "outputdir",
    "do_auto_resubmit",
    "parallel_submit",
    "inputsandbox",
    "info",
    "time",
    "application",
    "backend",
    "inputfiles",
    "outputfiles",
    "inputdata",
    "outputdata",
    "splitter",
    "subjobs",
    "postprocessors",
    "virtualization",
    "metadata"
]
jos = []
with open(file_path, 'r') as file:
    content = file.read()
    local_oj = ""
    for line in content.splitlines():
        # detect for 
        if not local_oj:
        any([i in schema_values for i in line.split()])
        break