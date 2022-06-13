from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('vis_app:index'))       
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('vis_app:index')
    