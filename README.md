# Ganga-gsoc-2020

## Checklist

- Benchmarks
  - [x] Mongo
    - [x] Batch
    - [x] Linear
  - []  Postgres
    - [x] Batch
    - [] Linear
  - []  Cassandra
    - [] Batch
    - [] Linear

## Instuction for running:

1. Mongodb:

   - **Start the database**:

     - ```bash
       sudo docker run --name mongo -p 27017:27017 -d mongo
       ```

   - **To restart the database:**

     - ```bash
       sudo docker stop mongo; sudo docker rm mongo;sudo docker run --name mongo -p 27017:27017 -d mongo
       ```

2. Cassandradb:

   - **Start the database**:

     - ```bash
       sudo docker run --name cassandra -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
       ```

   - **To restart the database:**

     - ```bash
       sudo docker stop mongo; sudo docker rm mongo;
       sudo docker run --name cassandra -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
       ```

3. PostgreSql:

   - **Start the database**:

     - ```bash
       sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
       ```

   - **To restart the database:**

     - ```bash
       sudo docker stop mongo; sudo docker rm mongo;
       sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
       ```