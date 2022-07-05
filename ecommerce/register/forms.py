from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
    # save form in user's database
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

