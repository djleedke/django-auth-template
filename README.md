# Django Template

This is a base template created for Django that has the default Django 
authentication system implemented along with a few minor tweaks.  It's designed to be a starting point for future projects that I would like to implement a login system in.

### Features

- Login & Logout (via Email address) 
- Sign Up
- Password Reset (via Email)
- Bootstrap enabled

## Contents
- [Setup](#setup)
- [Built With](#built-with)

## Setup
To get this up and running quickly follow these steps:

In a fresh folder on your computer, start up your git:
```
git init
```
Pull in the repo:
```
git pull https://github.com/djleedke/django-template.git
```

Install virtualenv if you don't have it already and set up the environment (in the root folder still):
```
pip install virtual env
```
```
python -m virtualenv venv
```
Activate the virtual environment:
```
venv\scripts\activate
```

Now install the requirements.txt (currently this is just Django 3.0.8):
```
pip install -r requirements.txt
```

Let's create the database models:
```
python manage.py migrate
```

And lastly, lets create a superuser to play with (follow the prompts):
```
python manage.py createsuperuser
```

Now things should be up and running!  Let's start the server:
```
python manage.py runserver
```
Now if you navigate to 127.0.0.1:8000 in your browser you should get a login page!

One noteworthy item is that the password reset emails will be collected as text files in ```PROJECT_ROOT/sent_emails```.  You will need to set this up manually for whichever email service you would like to use.  

### Renaming the Project

If you're like me you will want to change the project name from ```project``` to whatever you want it to be.  To do so follow these steps:

- Rename the ```project``` directory to ```newprojectname```
- In ```manage.py``` change this line:
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newprojectname.settings')
```
- In ```newprojectname/wsgi.py``` change the following to match:
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newprojectname.settings')
```
- Then, in ```settings.py``` change these lines:
```
ROOT_URLCONF = 'newprojectname.urls'
```
```
'DIRS': [os.path.join(BASE_DIR, 'newprojectname/templates')],
```
```
WSGI_APPLICATION = 'newprojectname.wsgi.application'
```


## Built With
- [Django](https://www.djangoproject.com/start/overview/) - for the webserver and base authentication system
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - for quick and easy responsive CSS