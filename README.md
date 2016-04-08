## AnkiStatsServer

This is a [Flask](http://flask.pocoo.org) application that provides an API for storing a subset of [Anki]() statistics in a MySQL database. Out-of-the box Anki provides a rich set of metrics for tracking your learning efficiency; but does not provide a solution for saving this data over time. This application is one part of a solution to save this data for further use.

As of April 2016, this application simply provides a one-way conduit for getting data into a MySQL database. And it only accepts a certain subset of metrics - those that are provided by the companion project [AnkiStats](). If you have idea that build on this basic project, please dive in.

### Prerequisites

You'll need to get some prerequisites out of the way first.

#### Install Flask

``` bash
$ pip install flask
```

#### Install SQLAlchemy

[SQLAlchemy](http://www.sqlalchemy.org) is a Python SQL toolkit and ORM that this application leverages to work closes with Flask.

``` bash
$ sudo pip install sqlalchemy==0.7.9
```

On AWS Linux, I needed `sudo` privileges to install SQLAlchemy.

#### Install Flask/SQLAlchemy

[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/) is a [Flask](http://flask.pocoo.org/) extension that provides [SQLAlchemy](http://www.sqlalchemy.org/) support for the application.

``` bash
$ pip install flask-sqlalchemy
```

#### Install SQLAlchemy-Migrate

[SQLAlchemy-Migrate](https://sqlalchemy-migrate.readthedocs.org/en/latest/) allows us to deal with changes in the database schema.

``` bash
$ pip install sqlalchemy-migrate
```

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
```
