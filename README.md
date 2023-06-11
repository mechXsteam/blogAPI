# BLOG API project
This project is a Django API implementation based on the book "Django for APIs" by William S. Vincent. It provides a foundation for building RESTful APIs using Django and Django REST Framework.
## The project structure follows standard Django conventions with additional components specific to building APIs:

```
blogAPI
  blogAPI
  |_ __init__.py
  |_ asgi.py
  |_ settings.py
  |_ urls.py
  |_ wsgi.py
  posts
  |_ __init__.py
  |_ admin.py
  |_ apps.py
  |_ models.py
  |_ permissions.py
  |_ serializers.py
  |_ tests.py
  |_ urls.py
  |_ views.py
manage.py
```
## Setup and installation
1. [clone the repository here](https://github.com/mechXsteam/blogAPI.git)
2. ```pip install requirements.txt```
3. ```python manage.py migrate```
4. ```python manage.py runserver```

## API Endpoints
* /: The root endpoint for the API.
* /pk/: post with an id = pk.
* /users/: get all the users list.
* /users/pk/: get the user with an id = pk.
* /rest-auth/registration/: user registration
* /rest-auth/login/: user login
* /rest-auth/logout/: user logout
* /rest-auth/password/reset/: password
* /rest-auth/password/reset/confirm/: password confirmation

## Documentation and Resources
For detailed instructions and explanations on building APIs with Django, refer to the book "Django for APIs" by William S. Vincent. You can find additional resources and documentation at the following links:

* Django Documentation
* Django REST Framework Documentation
* Python Documentation

