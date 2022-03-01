# alura-recipe-app

## Prerequisites

- [Install Python 3.10](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)
- [Install Poetry](https://python-poetry.org/docs/master/#installation)

### Setting Poetry

Enabling configuration that allows using .venv

```sh
 - poetry config virtualenvs.in-project true
```

Making poetry use python3.10

```sh
 - poetry env use $(which python3.10)
```

## On MacOS

You need to install postgresql on your system, else the installation of psycopg2-binary will fail.

```sh
 - brew install postgresql
```

## Install packages

```sh
 - poetry install
```

## Running Project

```sh
 - python manage.py runserver
```
