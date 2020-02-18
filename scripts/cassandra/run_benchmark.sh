sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10 1;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10 10;




sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 100 1;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 100 10;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 100 100;




sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 1000 1;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 1000 10;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 1000 100;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 1000 1000;





sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 1;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 10;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 100;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 1000;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 1000;

sudo docker stop cassandra; sudo docker rm cassandra;
sudo docker run --name cassandra -v ~/code/gsoc/ganga/scripts/cassandra/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
python simple_benchmark.py 10000 10000;