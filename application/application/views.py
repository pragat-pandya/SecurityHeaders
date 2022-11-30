from django.shortcuts import redirect, render
import requests as req


def home (request):
  return render (request, 'home.html')