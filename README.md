# Ecommerce_website
A simple version of ecommerce website is createdy by django, back-end: python, front-end: JavaScript, HTML, CSS

Either registered user or guest user can review products, add or remove products in cart, fill in shipping information for checkout

Cart items can be saved when user returns to the website

User can sign up an account

Javascript code for Paypal can be found at https://developer.paypal.com/home

Start Project: django-admin startproject "project name"

Create App: python manage.py startapp "app name"

Add APPS to INSTALLED_APPS in settings.py
Set up image url and folder address in settings.py
Set up redirect path after login and logout in settings.py
Set up css for crispy form using bootsrap in settings.py

Add views and paths to urlpatterns in urls.py

Migration:
python manage.py makemigrations
python manage.py migrate

Create superuser: python manage.py createsuperuser
Add products to database at /admin when log in as superuser

Add styling sign up and log in forms: pip install django-crispy-forms

csrftoken is generated to avoid malicious attacks

Run: python manage.py runserver
