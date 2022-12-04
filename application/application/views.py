from enum import unique
from urllib.robotparser import RequestRate
from django.shortcuts import render
from evaluator.models import Scan
from django.db.models import Q

def home (request):
  
  # GRAND TOTAL
  s = Scan.objects.all()
  total = s.count()

  # Q(grade__gte='A+') | Q(grade__gte='A')
  aPlus = s.filter(grade='A+')
  aPlusTotal = aPlus.count()

  a = s.filter(grade='A')
  aCount = a.count()

  b = s.filter(grade='B')
  bCount = b.count()

  c = s.filter(grade='C')
  cCount = c.count()
  
  d = s.filter(grade='D')
  dCount = d.count()

  e = s.filter(grade='E')
  eCount = e.count()

  f = s.filter(grade='F')
  fCount = f.count()


  recent = s.order_by('date_time__minute').distinct()[:8]

  hof = (aPlus.order_by('date_time__minute').distinct()[:4] |  s.order_by('date_time__minute').filter(grade='A').distinct()[:4]).distinct()

  hos = s.order_by('date_time__minute').filter(grade='F').distinct()[:8]

  return render (request, 'home.html', {
    'gt' : total,
    'apt': aPlusTotal,
    'at' : aCount,
    'bt' : bCount, 
    'ct' : cCount,
    'dt' : dCount,
    'et' : eCount,
    'ft' : fCount,
    'recent' : recent,
    'hof' : hof,  
    'hos' : hos  
  })

def sponsor (request):
  return render (request, 'sponsor.html')

def faqs (request):
  return render (request, 'faq.html')

def donate (request):
  return render (request, 'donate.html')

def www (request):
  return render (request, 'www.html')