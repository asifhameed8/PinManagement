# Pin Management System

### Prerequisites
* Python 3.8+

### Basic Features

* Authentication – Users can register, login, and logout.
* Map Administration - Once logged in, users can view, create, update, and delete map pins.
* Admin Panel - Manager users and pins in bulk.

### Quick Start
To get this project up and running locally on your computer follow the following steps:
1. Set up a python virtual environment (optional)
2. Run the following commands:
```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

3. Set GOOGLE_API_KEY in the .env file (optional)
4. Open a browser and go to http://localhost:8000/

### Admin Panel (Bonus)
First we need to create a superuser to be able to access the admin panel, follow these steps:
1. Run the following command and fill in the required details:
```
$ python manage.py createsuperuser
```

3. Open a browser and go to http://localhost:8000/admin
4. Login with the superuser credentials and enjoy!