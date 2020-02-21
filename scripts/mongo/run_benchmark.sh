sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10 1;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10 10;




sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 100 1;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 100 10;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 100 100;




sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 1000 1;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 1000 10;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 1000 100;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 1000 1000;





sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 1;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 10;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 100;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 1000;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 1000;

sudo docker stop mongo; sudo docker rm mongo;
sudo docker run --name mongo -p 27017:27017 -d mongo;
python simple_benchmark.py 10000 10000;