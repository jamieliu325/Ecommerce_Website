from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
    # save form in user's database
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


