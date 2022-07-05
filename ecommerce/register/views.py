from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "You've successfully created an account with us, please log in!")
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})