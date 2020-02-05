import sqlite3

sqliteConnection = sqlite3.connect('ganga_test.db')
cursor = sqliteConnection.cursor()

CREATION_JOB ='''CREATE TABLE IF NOT EXISTS JOB(
    id INT PRIMARY KEY,
    status string,
    name string,
    subjobs INT, 
    application string,
    backend string,
    backend_actualCE string,
    comment string
)'''


                Column("jid", Integer, ForeignKey("jobs.id")),
                Column("inputsandbox", Binary),
                Column("outputsandbox", Binary),
                Column("info", Binary),
                Column("comment", Binary),
                Column("time", Binary),
                Column("application", Binary),
                Column("backend", Binary),
                Column("inputfiles", Binary),
                Column("outputfiles", Binary),
                Column("non_copyable_outputfiles", Binary),
                Column("id", Binary),
                Column("status", Binary),
                Column("name", Binary),
                Column("inputdir", Binary),
                Column("outputdir", Binary),
                Column("inputdata", Binary),
                Column("outputdata", Binary),
                Column("splitter", Binary),
                Column("subjobs", Binary),
                Column("master", Binary),
                Column("postprocessors", Binary),
                Column("virtualization", Binary),
                Column("merger", Binary),
                Column("do_auto_resubmit", Binary),
                Column("metadata", Binary),
                Column("been_queued", Binary),
                Column("parallel_submit", Binary)
