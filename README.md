# pyrty
Web application made with Django and PostgreSQL. A forum for python enthusiasts.
Coded for fun to show Django and Python skills.

Technologies and tools used:
VS Code, Python 3.8.5, Django 3.1, Django REST Framework, Django Extensions, Docker, Docker-Compose, PostgreSQL, Celery with RabbitMQ, Git / GitHub, Postman, OmniDB.

# How to run
Having docker and docker-compose installed:
Run: 
- $ docker-compose build
- $ docker-compose up
- Having everything running, open a new terminal. If something went wrong, just Ctrl+C, $ docker-compose up again and continue from here.
- $ docker rm -f pyrty_django_1
- $ docker-compose run --rm --service-ports django python manage.py makemigrations
- $ docker-compose run --rm --service-ports django python manage.py migrate
Having this done, remove the "#" from pyrty/urls.py at line 38, leaving this not commented.
This class instance will populate your database instance with some random content in order to get a better demo experience.
- $ docker-compose run --rm --service-ports django
Enjoy!

# Try the app
You can log in as:
username: demo - password: demo

