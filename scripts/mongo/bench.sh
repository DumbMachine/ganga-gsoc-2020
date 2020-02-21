db=$1
size=$2
batch_size=$3

case $db in
    mongo)
        echo "you chose mongo"
        sudo docker run --name mongo -p 27017:27017 -d mongo;
        sudo /home/needshelp/anaconda3/bin/python bench_mongo.py $size $batch_size
        sudo docker stop mongo; sudo docker rm mongo
        ;;
    postgres)
        echo "you chose postgres"
        sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
        sleep 3
        sudo /home/needshelp/anaconda3/bin/python bench_postgres.py $size $batch_size
        sudo docker stop postgres; sudo docker rm postgres;
        ;;
    cassandra)
        echo "you chose cassandra"
        sudo docker container run --name cassandra -v ~/code/gsoc/ganga/scripts/mongo/cassandra.yaml:/etc/cassandra/cassandra.yaml -p 127.0.0.1:9042:9042 -e CASSANDRA_CLUSTER_NAME=GangaTest -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra
        sleep 15
        sudo /home/needshelp/anaconda3/bin/python bench_cassandra.py $size $batch_size
        sudo docker stop cassandra; sudo docker rm cassandra;
        ;;
    *)
        echo "Ain't got that yet";;
esac
