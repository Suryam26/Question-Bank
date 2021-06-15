# Question Bank

This a Django based responsive web application that is used for storing question-papers for an instituted. It is powerd by PostgreSQL Full-Text-Search for quick and powerfull searchs.

# Installation

This project is build using Docker.

To run this project first download [Docker](https://www.docker.com/products/docker-desktop). Once that is done, run the 'Docker Desktop' application (Downloaded with Docker) which inturn will start 'Docker-Daemon'.

## Starting the Project

Once 'Docker-Daemon' is up and running navigate to the project directory and in the terminal run:

```bash
$ docker-compose up -d --build
```

This command will build a docker container using 'Dockerfile' and 'docker-compose.yml' file. It will also install all the project dependencies and start the development server.

After that run the initial migration for the project using the following command:

```bash
$ docker-compose exec web python manage.py migrate
```

You can also create a superuser using:

```bash
$ docker-compose exec web python manage.py createsuperuser
```

To access the website visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Checking Logs

To check the server logs for errors use:

```bash
$ docker-compose logs
```

## Stopping the Development Server

To stop the development server and the docker container run:

```bash
$ docker-compose down
```

## Run Commands

To run commands inside the docker container use:

```
$ docker-compose exec web [COMMAND]
```

Here `[COMMAND]` could be a Django, python or bash command.

For example:

```bash
$ docker-compose exec web python manage.py test
```

## Google OAuth

This project support Google OAuth for logins using the 'django-allauth' application.

To activate this feature go through this [example](https://learndjango.com/tutorials/django-allauth-tutorial) for activation of GitHub OAuth. The implementation for both is almost same. For more details read the [Official Documentation](https://django-allauth.readthedocs.io/en/latest/installation.html) for 'django-allauth'.
