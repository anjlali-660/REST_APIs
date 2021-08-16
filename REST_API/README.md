
# REST_APIs Using Python(Django)

### A brief description of what this project is

A REST API is a standardized way to provide data to other applications. Those applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.
There are a few key options for a REST API request:

GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide

POST — Creates a new record that gets appended to the database

PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record

DELETE — Deletes the record at the given URI

PATCH — Update individual fields of a record


## To-do list to create a REST API in Django

1) Set up Django
2) Create a model in the database and 
then fire command on cmd(py manage.py makemigrations)and (py manage.py migrate)

3) Set up the Django REST Framework
4) Serialize the model from step 2
5) Create the URL endpoints to view the serialized data



## Steps to run this API

## 1.Set up Django

To create a Django app, we’ll need to install Django.

 Install Django 
 
 (pip install Django)  That’s easy enough!

 ## 2. Set up Django REST Framework
 pip install djangorestframework

 ## 3. Set up Django Filters
 pip install django_filters

 ## 4.Open Command_Prompt
 Open Command prompt and come to the project directory called REST_API(Its a Folder)
 
[cd/REST_API]
## 5.Fire command to runserver of Django
py manage.py runserver 1200

  [Here 1200 is a port no.by default it is 8000]

## 6. Go to URL Bar

Type URL->localhost:1200.api/user/

It will give you the homepage

## 7. Queries You can write in URL Bar
Sample query endpoint:- 

/api/users?page=1&limit=10&name=James&ordering=-age

This endpoint should return list of 10 users whose first name or last name contains substring given name
and sort the users by age in descending order of page 1.

Sample query looks like:- /api/users/1 GET









