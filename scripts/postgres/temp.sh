sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10 1;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10 10;




sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 100 1;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 100 10;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 100 100;




sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 1000 1;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 1000 10;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 1000 100;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 1000 1000;





sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 1;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 10;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 100;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 1000;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 1000;

sudo docker stop postgres; sudo docker rm postgres;
sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
python simple_benchmark.py 10000 10000;