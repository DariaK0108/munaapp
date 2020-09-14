from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

# Create your views here.

def todolist(request):
    return HttpResponse("Welcome to Muna App")

def contact(request):
    context = {
        'contact_text': "Welcome to Contact Page."
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': "Welcome to About Page."
    }
    return render(request, 'about.html', context)

def index(request):
    context = {
        'index_text': "Welcome to Index Page."
    }
    return render(request, 'index.html', context)
