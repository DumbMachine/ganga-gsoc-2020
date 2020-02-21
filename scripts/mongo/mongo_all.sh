sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 1000 1
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 1000 10
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 1000 100
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 1000 1000
sudo docker stop mongo; sudo docker rm mongo;

# ========================================================================================================

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 10000 1
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 10000 10
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 10000 100
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 10000 1000
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 10000 10000
sudo docker stop mongo; sudo docker rm mongo;

# =========================================================================================================

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 100000 1
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 100000 100
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 100000 1000
sudo docker stop mongo; sudo docker rm mongo;

sudo docker run --name mongo -p 27017:27017 -d mongo;
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_mongo.py 100000 10000
sudo docker stop mongo; sudo docker rm mongo;