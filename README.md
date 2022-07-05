# Ecommerce_website
A simple version of ecommerce website is createdy by django, back-end: python, front-end: JavaScript, HTML, CSS

**Functions:**

Either registered user or guest user can review products, add or remove products in cart, fill in shipping information for checkout

Cart items can be saved when user returns to the website

User can sign up an account

csrftoken is generated to avoid malicious attacks

Javascript code for Paypal can be found at https://developer.paypal.com/home

**Set up:**

Start Project (ecommerce): django-admin startproject "project name"

Create Apps (store and register): python manage.py startapp "app name"

Add new apps (store, register, crispy_forms) to INSTALLED_APPS in settings.py
Set up image url and folder address in settings.py
Set up redirect path for login and logout in settings.py
Set up css for crispy form using bootsrap in settings.py

Add names, views, and paths to urlpatterns in urls.py in store folder

Add urls in apps to urls.py in project folder

Migration:
python manage.py makemigrations
python manage.py migrate

Create superuser: python manage.py createsuperuser
Add products to database at /admin when log in as superuser

Add styling sign up and log in forms: pip install django-crispy-forms

**Run the website:**

python manage.py runserver
