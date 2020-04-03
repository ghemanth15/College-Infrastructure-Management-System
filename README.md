# College Infrastructure Management System
This is an infrastructure Management site localized to a college. This project is developed using Django-(python based webframework) and i have used pgsql as the backend database querying language. Also, the project uses jinja template.

![Architecture](https://github.com/ghemanth15/College-Infrastructure-Management-System/blob/master/cims/Screenshot%20(21).png)

### For downloading django
```sh
pip install django
```
Creating virtual environment is not mandatory, but if you prefer a virtual environment , 
### Virtual Environment setup 
```sh
python -m venv venv
```
I've also downloaded pgAdmin v4 for viewing te database.
### The project can be run by using the following command 
```sh
python manage.py runserver
```
For any changes in static files ``` python manage.py collectstatic ```

For changes in models.py ``` python manage.py makemigrations ```

after performing makemigrations, do enter ``` python manage.py migrate ``` to migrate all the changes to the database.

### For creating a superuser
``` python manage.py createsuperuser ``` 

Incase of creating a django project in future ``` django-admin startproject project_name ```

and creation of apps ``` python manage.py app_name ```

Other operations and functionalities can be viewed by ``` python manage.py help ```

### The following are the links in the project domain:

| Link | View |
| -------- | -------- |
| localhost:8000/admin | To view the admin area |
| localhost:8000/ | To view the home page |
| localhost:8000/about | To view the about page |
| localhost:8000/rooms | To view all the assets |
| localhost:8000/room | To view a contact Us form |
| localhost:8000/accounts/register | To register | 
| localhost:8000/accounts/login | To login |
| localhost:8000/accounts/dashboard | To view the dashboard of logged-in users |
| localhost:8000/listings/search | To search for assets |
