# Simple Django Rest Framework API Exemple


## Install

The only prerequisites are [Python 3.6](https://www.python.org/downloads/release/python-360/) and [PostgreSQL](https://hub.docker.com/_/postgres/)

After you cloned the repository, you may want to run the following from the source folder:

```console
$ git clone https://github.com/eduleones/drf-api-exemple.git
$ cd drf-api-exemple/
$ python3.6 -m venv venv
$ source venv/bin/active
$ pip install -r requirements.txt
```

Then you need to configure the .env file by example:

```console
DEBUG=True
SECRET_KEY='e%p7t6jwbwwgsk7c=38-svj#%jc^-95z@28phs-snegz&6v33('
DB_NAME=api_employee
DB_USER=postgres
DB_PASS=BGAyWfZccGuHqFcWvy8WFgv7
DB_HOST=localhost
```

Migrate database and running tests:

```console
$ python manager.py makemigrations
$ python manager.py migrate
$ python manager.py test
```

Create Admin User and run app:

```console
$ python manager.py createsuperuser
$ python manager.py runserver
```

The API Docs: http://localhost:8000/

The Admin Painel: http://localhost:8000/admin/



