# Run this script to start the benchmark

docker run --name cassandra -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra

docker run --name postgres -p 45432:5432 -e POSTGRES_PASSWORD=ganga -d postgres

docker run --name mongo -p 27017:27017 -d mongo
