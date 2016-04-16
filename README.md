# DicoDigital API  [![dicodigital-api on Travis](https://travis-ci.org/harmo/dicodigital-api.svg?branch=master)](https://travis-ci.org/harmo/dicodigital-api)

API for [https://lite6.framapad.org/p/dicodigital](https://lite6.framapad.org/p/dicodigital)

Build with [Django](https://www.djangoproject.com/) and [Django-rest-framework](http://www.django-rest-framework.org/)

# One click deploy !!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Requirements

* Python 3
* Virtualenv

## API Documentation

[Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger/) was installed and is accessible directly from your app to ```/docs/```

## Development

Get the project and install dependencies:

```bash
git clone https://github.com/harmo/dicodigital-api.git
cd dicodigital-api
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```

Set environement variables:

→ [dj-database-url](https://github.com/kennethreitz/dj-database-url#url-schema)

```bash
export DJANGO_SETTINGS_MODULE=dicodigital.settings
export DATABASE_URL=sqlite:///$(pwd)/dicodigital.db
export DEBUG=True
```

Migrate the database:

```bash
./manage.py migrate
```

This step allow you to create a superadmin user:

```bash
./manage.py createsuperuser
```

Run the magic:

```bash
./manage.py runserver_plus
```

## With Docker

To run a container with everything in local, there is an image for that
from the docker hub [https://hub.docker.com/u/dicodigital](https://hub.docker.com/u/dicodigital).

Run the container with:

```
docker run --rm --name dicodigital-api -p 8000:8000 dicodigital/dicodigital-api
```

To build a new images, run `docker build -t dicodigital-api .`
