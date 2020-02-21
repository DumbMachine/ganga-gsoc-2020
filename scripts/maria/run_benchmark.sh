sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga -e MYSQL_ROOT_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10 1;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10 10;




sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 100 1;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 100 10;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 100 100;




sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 1000 1;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 1000 10;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 1000 100;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 1000 1000;





sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 1;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 10;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 100;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 1000;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 1000;

sudo docker stop mariadb; sudo docker rm mariadb;
sudo docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_USER=ganga  -e POSTGRES_PASSWORD=ganga -d mariadb
python simple_benchmark.py 10000 10000;