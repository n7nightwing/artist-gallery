# artist-gallery
An informational app about artists and their works (whether painting, musical composition, or written works).

## Technologies Used
This app is built entirely with Django, using a PostgreSQL database.

## Installation and Contributions
If you wish to contribute to this project, please fork and clone this repository. As the database is not hosted (for now), you will have go through the following steps in order to get everything set up:

1.) Login to psql:
```
psql -d postgres
```

2.) Create a database and user:
```
CREATE DATABASE gallery;
CREATE USER galleryuser WITH PASSWORD 'gallery';
GRANT ALL PRIVILEGES ON DATABASE gallery TO galleryuser;
```

3.) Install dependencies:
```
pip install django psycopg2-binary django-extensions
```
.) Bootsrap 4 dependencies
```
pip install django-crispy-forms

```

4.) Create a virtual environment:
```
python3 -m venv .env
```

5.) Activate the environment:
```
source .env/bin/activate
```

6.) Migrate models to the database:
```
python manage.py makemigrations
```

```
python manage.py migrate
```
7.) Bootstrap documentation
    -https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html
    
