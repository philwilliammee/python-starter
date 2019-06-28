# python-starter

A module to connect to a postgress DB

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* A postgress DB that you can connect to. This repo includes a .lando.yml file that you can use to start up a docker container with a postgres db for local testing. learn more about lando and docker [here](https://docs.devwithlando.io/).
* Python 3.7 with pip installed or again you can use the python that comes in the docker conatiner.
* GIT

### Installing

Clone this repo with git

```bash
git clone https://github.com/philwilliammee/python-starter.git && cd python-starter
```

Create a virtual env for testing

```bash
python -m venv my_env
```

Activate the virtual env on mac linux

```bash
source ./my_env/bin/activate
```

Activate the virtual env on windows

```bash
source ./my_env/Scripts/activate
```

Install the requirement with pip

```bash
pip install -r requirements.txt
```

## Configuration

Copy the example_settings.py to settings.py and modify the DB connection and email connection information to your settings

```bash
cp example_settings.py settings.py
```

## Running the tests

Test the app by runnint python unitest to test your database connection

```bash
python -m unittest -v tests/app_test.py
```

## Running the App Command Line Interface(CLI)

Run the app cli help

```bash
python app.py -h
```

run the app send test values to enter into a table in the database check the ./storage/logs/app.log for debugging info

```bash
python app.py -u "my name" -n "mynetid"
```

run the app with send email

```bash
python app.py -u "my name" -n "mynetid" -email "true"
```
