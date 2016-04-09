## AnkiStatsServer

This is a [Flask](http://flask.pocoo.org) application that provides an API for storing a subset of [Anki](http://ankisrs.net) statistics in a MySQL database. Out-of-the box Anki provides a rich set of metrics for tracking your learning efficiency; but does not provide a solution for saving this data over time. This application is one part of a solution to save this data for further use.

As of April 2016, this application simply provides a one-way conduit for getting data into a MySQL database. And it only accepts a certain subset of metrics - those that are provided by the companion project [AnkiStats](). If you have idea that build on this basic project, please dive in.

### Assumptions

You should have a server on which to install this application, some basic knowledge around the terminal, and a working install of MySQL server.

### Prerequisites

You'll need to get some prerequisites out of the way first. To make it easy, you can just run the included `setup.py` script to grab all of the prerequisites.

``` bash
$ sudo python ./setup.py
```

For the record, you're installing:

- [Flask](http://flask.pocoo.org) - a microframework for Python web applications
- [SQLAlchemy](http://www.sqlalchemy.org) - a Python SQL toolkit and ORM that this application leverages to work closes with Flask.
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) - a [Flask](http://flask.pocoo.org/) extension that provides [SQLAlchemy](http://www.sqlalchemy.org/) support for the application.
- [SQLAlchemy-Migrate](https://sqlalchemy-migrate.readthedocs.org/en/latest/) - allows us to deal with changes in the database schema.

### Obtaining and configuring the application

#### Clone the github repo

`cd` to the parent directory of choice and clone.

``` bash
git clone https://github.com/NSBum/AnkiStatsServer.git
```

#### Setup a configuration file

You'll need to create a configuration file `config.py` at the root level of your project. Probably I should handle this differently with environment variables or something. But I'm lazy. The configuration should look like:

``` Python
SQLALCHEMY_DATABASE_URI = 'mysql://user_name:password@127.0.0.1/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'some_top_secret_FBI_bait'
DEBUG = True
```

### Database setup

The application uses [Alembic](https://pypi.python.org/pypi/alembic/0.8.5), part of [Flask-Migrate](https://pypi.python.org/pypi/Flask-Migrate/1.8.0) that you installed above to managed schema changes. It can also be used to generate the database _de novo_. You'll need to have a database named `anki` on MySQL.

#### Initialize Alembic
``` bash
$ python manage.py db init
  Creating directory /anki/migrations ... done
  Creating directory /anki/migrations/versions ... done
  Generating /anki/migrations/alembic.ini ... done
  Generating /anki/migrations/env.py ... done
  Generating /anki/migrations/README ... done
  Generating /anki/migrations/script.py.mako ... done
  Please edit configuration/connection/logging settings in
  '/anki/migrations/alembic.ini' before proceeding.
```

After running the database initialization you should have a folder `migrations` in the project. This is all of the data needed to run migrations for the project. Next you'll need to begin the first migration.

#### Begin first migration

``` bash
$ python manage.py db migrate
  INFO  [alembic.runtime.migration] Context impl MySQLImpl.
  INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  INFO  [alembic.autogenerate.compare] Detected added table 'stats'
  Generating /home/ec2-user/AnkiStatsServer/migrations/versions/65ed34d8a8ee_.py ... done
```

Finally we have to perform the actual upgrade.

#### Database upgrade

``` bash
$ python manage.py db upgrade
  INFO  [alembic.runtime.migration] Context impl MySQLImpl.
  INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  INFO  [alembic.runtime.migration] Running upgrade  -> 65ed34d8a8ee, empty message
```

Now you are ready to run the application.

``` bash
$ python app.py
```

### Usage

This is a dead-simple API, desperately looking for more features. For now, there's one API end-point: `/data`. To save Anki stats, you'll need to make a `POST` request to that end-point with the following JSON as the payload:

``` json
{"vocab": 665, "tcount": 1165, "review": 125, "time": 1460016000, "filter": 0, "msum": 7, "relearn": 15, "mcnt": 8, "learn": 61, "duration": 979, "total": 201, "tomorrow": 132}
```

If the request is successful, you should receive the following response:

``` json
{
  "id": 8,
  "result": {
    "status": 200
  }
}
```

where `id` is the row `s_id` value.
