import sqlite3

sqliteConnection = sqlite3.connect('ganga_test.db')
cursor = sqliteConnection.cursor()

CREATION_JOB ='''CREATE TABLE IF NOT EXISTS JOB(
    id INT PRIMARY KEY, status string, name string, subjobs INT, application string,
    backend string, backend_actualCE string, comment string
)'''

INSERT_JOB = '''
    INSERT INTO JOB(id, status, name, subjobs, application, backend, backend_actualCE, comment)
    VALUES          (?,      ?,    ?,       ?,           ?,       ?,                ?,       ?)
'''

CREATION_BLOB = """ 
    CREATE TABLE IF NOT EXISTS BLOB(
        id INT PRIMARY KEY,
        inputsandbox BLOB,
        outputsandbox BLOB,
        info BLOB,
        comment BLOB,
        time BLOB,
        application BLOB,
        backend BLOB,
        inputfiles BLOB,
        outputfiles BLOB,
        non_copyable_outputfiles BLOB,
        status BLOB,
        name BLOB,
        inputdir BLOB,
        outputdir BLOB,
        inputdata BLOB,
        outputdata BLOB,
        splitter BLOB,
        subjobs BLOB,
        master BLOB,
        postprocessors BLOB,
        virtualization BLOB,
        merger BLOB,
        do_auto_resubmit BLOB,
        metadata BLOB,
        been_queued BLOB,
        parallel_submit BLOB
    )
"""

INSERT_BLOBS = """  
    INSERT INTO BLOB(
        id, inputsandbox, outputsandbox, info, comment, time, application, backend, inputfiles,
        outputfiles, non_copyable_outputfiles, status, name, inputdir, outputdir,
        inputdata, outputdata, splitter, subjobs, master, postprocessors, virtualization, merger,
        do_auto_resubmit, metadata, been_queued, parallel_submit
    ) VALUES (
        '?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?'
    )
"""

INSERT_BLOBS = """
    INSERT INTO BLOB(
        id, inputsandbox, outputsandbox, info, comment, time, application, backend, inputfiles,
        outputfiles, non_copyable_outputfiles, status, name, inputdir, outputdir,
        inputdata, outputdata, splitter, subjobs, master, postprocessors, virtualization, merger,
        do_auto_resubmit, metadata, been_queued, parallel_submit
    ) VALUES (
        '?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?'
    )
"""

cursor.execute(INSERT_BLOBS, bo[0])



inputsandbox, jid, outputsandbox, info, comment, time, application, backend,
inputfiles, outputfiles, non_copyable_outputfiles, id, status, name, inputdir,
outputdir, inputdata, outputdata, splitter, subjobs, master, postprocessors, 
virtualization, merger, do_auto_resubmit, metadata, been_queued, parallel_submit
