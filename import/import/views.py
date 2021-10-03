from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.hashers import make_password, check_password
from .models import Company


def index(request):
    return HttpResponse("Hello, world.")

