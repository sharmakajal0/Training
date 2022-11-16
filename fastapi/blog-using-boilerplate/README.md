# Installation instructions for YT-Stories



## Make sure following tools are already installed in your system.

1) [Poetry](https://python-poetry.org/docs/)


## Setup Poetry Environment


1) Install the required packages from poetry
```
poetry install
```

## Run the project
1) Run the below command (from where the docker-compose file is located.)
```
docker-compose up
```
2) Go inside the root of the project (src)
3) Migrate the models to the database
```commandline
alembic upgrade head
```
4) Run the server
```commandline
python main.py
```

## Notes
1) Please make sure to run the below commands whenever any model is changed.
```commandline
alembic revision --autogenerate
```
2) Then migrate the files to the database

## If using Pycharm, setup project interpreter like below

1) Go to Add interpreter option, select Poetry environment
2) Select Existing one, if the above commands executed perfectly, the environment should be displayed in the existing 
interpreter.

 
