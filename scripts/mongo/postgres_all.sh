sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 1000 1
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 1000 10
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 1000 100
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 1000 1000
sudo docker stop postgres; sudo docker rm postgres;

# ========================================================================================================

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 10000 1
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 10000 10
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 10000 100
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 10000 1000
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 10000 10000
sudo docker stop postgres; sudo docker rm postgres;

# =========================================================================================================

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 100000 1
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 100000 100
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 100000 1000
sudo docker stop postgres; sudo docker rm postgres;

sudo docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=ganga -d postgres
sleep 3
sudo /home/needshelp/anaconda3/bin/python bench_postgres.py 100000 10000
sudo docker stop postgres; sudo docker rm postgres;