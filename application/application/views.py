from django.shortcuts import render


def home (request):
  return render (request, 'home.html')

def sponsor (request):
  return render (request, 'sponsor.html')

def faqs (request):
  return render (request, 'faq.html')

def donate (request):
  return render (request, 'donate.html')