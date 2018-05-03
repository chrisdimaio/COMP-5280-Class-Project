# COMP-5280-Class-Project

## How to run the server (Ubuntu/Debian)
### Install Python venv
* sudo apt install python3-venv
### Setup the virtual environment
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
### Setup & run the server
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver
