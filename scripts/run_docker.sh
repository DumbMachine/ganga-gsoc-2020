# Run this script to start the benchmark
sudo docker run --name cassandra -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -e CASSANDRA_BATCH_SIZE_FAIL_THRESHOLD_IN_KB=5000000000000000000000=500000 -d cassandra
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sudo docker run --name mongo -p 27017:27017 -d mongo
