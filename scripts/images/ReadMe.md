NOTE: I wasnt able to test cassandra db with batches bacause of the following error when inserting blobs in any batch_size > 1: `InvalidRequest - code=2200 [Invalid query] message="Batch too large"`. Internet search says that changing `batch_size_fail_threshold_in_kb` attribute in the cassandra.yaml file does the trick. I have tried this but got no luck. I'm still trying to get cassandra to work with large batch sizes. Ill update these results soon with appropriate results.


The legend in the left hand top corner of each image has the name of the function benchmarked and their corresponding number on the x axis.
- connect: This function connects to the respective database.
- create_tables: This function creates tables (jobs and blobs) for storing the information. (mongo doesnt require this and thus is marked zero)

- add_jobs_batch: This function adds rows to the jobs table in batch_size.
- add_blobs_batch: This function adds rows to the blobs table in batch_size.

- query_jobs_all: This function queries all the rows in the jobs table.
- query_blobs_all: This function queries all the rows in the blobs table.

My conclusions:
- `connect` and `create_tables` shouldn't really be a factor to judge upon since they are one time setup based functions.
- `add_jobs_batch`:  MongoDB was faster in each insertion when the size of data to be inserted exceeded 1k. For smaller table sizes (<1K) PostgreSQL performed bettter than MongoDB.
- `add_blobs_batch`: MongoDB consistently performed better here.
- `query_jobs_all`: Superisingly the performance here for both the databases are very similar.
- `query_blobs_all`: MongoDB consistently performed better here.


# Note:
I believe these tests do not represent the actual work load, as it was mentioned that users could have 1000s of jobs with 1000s of subjobs, so we should expect Million+ rows in each table. I will rerun these tests, after I get cassandra db's batchs working.