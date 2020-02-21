sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 1000 1
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 1000 10
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 1000 100
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 1000 450
sudo docker stop cassandra; sudo docker rm cassandra;

# ========================================================================================================

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 10000 1
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 10000 10
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 10000 100
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 10000 450
sudo docker stop cassandra; sudo docker rm cassandra;

# =========================================================================================================

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 100000 1
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 100000 100
sudo docker stop cassandra; sudo docker rm cassandra;

sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
sleep 15
sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py 100000 450
sudo docker stop cassandra; sudo docker rm cassandra;
