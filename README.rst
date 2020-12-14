HCD PROJECT / DOCKER EDITION
=======================

.. image:: https://travis-ci.org/pydanny/cookiecutter-django.svg?branch=master
    :target: https://travis-ci.org/pydanny/cookiecutter-django?branch=master
    :alt: Build Status

.. image:: https://img.shields.io/badge/cookiecutter-Join%20on%20Slack-green?style=flat&logo=slack
    :target: https://join.slack.com/t/cookie-cutter/shared_invite/enQtNzI0Mzg5NjE5Nzk5LTRlYWI2YTZhYmQ4YmU1Y2Q2NmE1ZjkwOGM0NDQyNTIwY2M4ZTgyNDVkNjMxMDdhZGI5ZGE5YmJjM2M3ODJlY2U

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code style: black

FEATURES
---------

* Flask_ - Python
* Quasar.dev_ 2.0 - Javascript
* Trabaja con Python_ 3.8
* 12-Factor_ Para variables de entorno python-environ_
* Alta seguridad por default con certificados SSL via LetsEncrypt_.

* Optimized development and production settings
* Docker support using docker-compose_ for development and production (using Traefik_ with LetsEncrypt_ support)
* Customizable SQLite_, RedisDB_ & MongoDB_ version
* Comes with custom user model ready to go
* Optional basic ASGI setup for Websockets
* Run tests with unittest or pytest

Integrations
---------------------

*These features can be enabled during initial project setup.*

* Configuration for Celery_ and Flower_ (the latter in Docker setup only)
* Integration with Sentry_ for error logging

.. _Flask: https://flask.palletsprojects.com/en/1.1.x/
.. _Quasar.dev: https://quasar.dev/
.. _Python: https://www.python.org/
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _LetsEncrypt: https://letsencrypt.org/
.. _Celery: http://www.celeryproject.org/
.. _Flower: https://github.com/mher/flower
.. _Sentry: https://sentry.io/welcome/
.. _docker-compose: https://github.com/docker/compose
.. _Traefik: https://traefik.io/
.. _SQLite: https://www.sqlite.org/
.. _RedisDB: https://redis.io/
.. _MongoDB: https://www.mongodb.com/es
.. _LetsEncrypt: https://letsencrypt.org/

Prerequisites
-------------

* Docker; if you don't have it yet, follow the `installation instructions`_;

.. _`installation instructions`: https://docs.docker.com/install/#supported-platforms

CSV Files to work
-------------

Copy your CSV files in `/temp/backend/files` before run build

Build the Stack
-------------

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml build

Execute Management Commands
---------------------------

As with any shell command that we wish to run in our container, this is done using the ``run --rm`` command: ::

    $ docker-compose -f local.yml run --rm django python manage.py collectstatic

Here, ``django`` is the target service we are executing the commands against.

Build the Stack
-------------

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

Run on

    http://localhost:8001


Execute PORTAINER.io
---------------------------

Run on

    http://localhost:9000
