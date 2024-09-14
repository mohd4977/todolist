# Introduction

The goal of this project is to provide minimalistic django project for todo list with full CRUD implementation and User authentication like Login, Logout and Register

### Main features

* User registration and login/logout using Django's built-in User model.

* A Task model with fields for the task name, description, completion status, and the user it belongs to (using ForeignKey).

* Users can only view and manage their own tasks.

* CRUD functionality (Create, Read, Update, Delete) for tasks

* Use Django’s class-based views (CBVs) for handling CRUD operations.

* Add task filtering by completion status (e.g., active, completed)

* Implement flash messages to show feedback (e.g., “Task created successfully”)

### Remaining Features

* Front End Styling (Adding bootstrap in project)

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install -r requirements.txt
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

To run test cases:

    $ python manage.py test
