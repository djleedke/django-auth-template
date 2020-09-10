# Django Auth Template

This is a base template created for Django that has the default Django authentication system implemented along with a few minor tweaks.  It's designed to be a starting point for future projects that I would like to implement a login system in.  See a deployed version at https://django-auth-template.herokuapp.com/login/.

## Contents
- [Features](#features)
- [Setup](#setup)
- [Built With](#built-with)

## Features

- Login & Logout (via Email address) 
- Password Reset (via Email)
- Sign Up Page
- Settings Page
- Bootstrap enabled

## Setup
To get this up and running quickly follow these steps:

On Github, click "Use this template" and create a new repo:
![image](https://user-images.githubusercontent.com/33850990/89134476-303e1700-d4eb-11ea-87df-02e00ddbcb0d.png)

In a fresh folder on your computer, start up your git:
```
git init
```
Pull in the repo you just created:
```
git pull INSERT_REPO_URL_HERE
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

Now we will make a superuser to play with (follow the prompts):
```
python manage.py createsuperuser
```

Lastly we need to make an empty file called ```local_settings.py``` in the same folder as ```settings.py```.  This file is already included in .gitignore and is where you can store any environment variables you may need (email credentials, secret keys, etc.).  For now it is ok that is empty, ```settings.py``` just needs it to exist for it to run locally or you will get an error.

Now things should be up and running!  Let's start the server:
```
python manage.py runserver
```
Now if you navigate to 127.0.0.1:8000 in your browser you should get a login page!

One last item to mention is that the password reset emails will be collected as text files in ```PROJECT_ROOT/sent_emails```.  

### Renaming the Project

If you're like me you will want to change the project name from ```project``` to whatever you want it to be. You should do this **before** you migrate the database or your tables will be created with the generic "project_tablename" name instead of whatever your new project name is.  To do so follow these steps:

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
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - for quick and easy responsive CSS & Javascript
