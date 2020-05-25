# test_app
test task

## Installation
There is the complete list of packages required by the project (Ubuntu)
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev python python-virtualenv python-pip python3-venv libfreetype6 libfreetype6-dev pkg-config npm postgresql-client postgresql postgresql-contrib postgresql-server-dev-9.x git python3-dev
```

## Configure packages

### Postgres

```
$ sudo su postgres -c psql

postgres$ create user <user> with password '<password>';

postgres$ create database test_app owner <user> encoding 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

#### Only for local purposes to use fabric

```
postgres$ alter user <user> with superuser;
```

Edit the `/etc/postgresql/9.x/main/pg_hba.conf` file as root user:

```
local all postgres trust

local all all trust
```

Restart the service

```
$ /etc/init.d/postgresql restart
```

## Configure the project
### Create a virtualenv

```
$ python3 -m venv myvenv
```

This command will create a new folder with the name `myvenv`

### Clone the project


```
$ git clone https://github.com/infant23/test_app.git
```

### Activate your enviroment
Inside the `test_app` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(myvenv) $
```

### Install requirements
```
(test_app)$ cd test_app

(test_app)$ pip install -r requirements.txt
```

### Setting up environment variables for project

For environment variables configuration, you will need a .env file in the parent directory of the current folder.

```
(test_app) $ touch ../.env
```

### Run the project

Once you have everything ok, you can run the project.

```
(test_app) $ ./manage.py check

(test_app) $ ./manage.py migrate

(test_app) $ ./manage.py runserver
```


### Run tests

Coverage is configured for the project for running tests and measuring in Scrutinizer

```
(test_app) $ coverage run --source="." manage.py test --settings=test_app.settings --verbosity=2
```

Once ran, if you want to see fast the results you can run

```
(test_app) $ coverage report
```

or you can run

```
(test_app) $ coverage html
```

and an HTML view of your test coverage will be generated in htmlcov/index.html


# Dockerization

## Build process

To build your project using Docker:

```
$ docker-compose build --build-arg SSH_KEY="$(cat ~/.ssh/id_rsa)" --build-arg SSH_KEY_PUB="$(cat ~/.ssh/id_rsa.pub)" project
```
> NOTE:
> - Make sure your RSA keys are not configured with a password, otherwise build will fail.
>
> - New RSA public key must be added to your Bitbucket configuration to allow clone of private repositories in *requirements.txt*

## Running the project

To start your project you can execute:

```
$ docker-compose up -d
```

When executing
```
$ docker ps
```

there should be 2 containers (`db` and `projectsource`)


To shut down containers:
```
$ docker-compose down
```

> NOTE:
>
> After configuring everything, the project should be running in localhost:8000, so be careful with port conflicts.

## Extra considerations

The file `docker-compose.yml` list the services that Docker will run, so feel free to comment / uncomment those that you need.
