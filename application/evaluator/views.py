from django.shortcuts import render, redirect
import requests as req
from application.urls import home
import socket
from datetime import datetime, timezone
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .packages import *
from .models import *

# Create your views here.
def queryProcessor (request):
  if request.method == 'POST':
    domain = request.POST['url'].strip()
    if domain == '':
      messages.error(request, "Please enter an address to search!")
      return redirect ('home')
    # FIX UP SCHEME of URL
    domain = getDomain(domain)
    
    check = checkSite(domain)
    if check == -1:
      # Django Alerts Configurations
      messages.error(request, "No host found at the given address!! OR This site do not support some headers we")
      return redirect('home')

    # DOMAIN VALID CASE  
    elif check != -1: 

      # HOST-NAME
      host = getHostName(domain)

      # IP
      origin = socket.gethostbyname(host)

      # GRADE
      grade = checkGrade(check)

      # ALl headers
      allHeaders = req.get(domain).headers

      # DATE-time
      t = datetime.now(timezone.utc)

      # Make a Scan table entery
      try:
        s = Scan.objects.get(url=domain)
        s.url = domain
        s.ip = origin
        s.grade = grade
        s.host_name = host
        s.save()
      except:
        s = Scan()
        s.url = domain
        s.ip = origin
        s.grade = grade
        s.host_name = host
        s.save()
      return render (request, 'evaluator/results.html', {
        'deep' : False,
        'found' : True,
        'grade' : grade,
        'mains' : check.items(),
        'site' : domain,
        'ip' : origin,
        'headers' : getHeaders(allHeaders).items(),
        'date' : t,
        'missing' :  getMissing(check).items(),
        'upcomming' : upcomming.items()
      })
    else:
      return redirect ('home')  
  return render (request, 'home.html')

def deep (request):
  if request.method == 'POST':
    first_name = request.POST['fname'].strip()
    last_name = request.POST['lname'].strip()
    email = request.POST['email'].strip()
    try:
      validate_email(email)
    except ValidationError as e:
       messages.error(request, 'Please enter a valid email to deep scan!!')
       return redirect('home')
    else:
      messages.success(request, 'Deep-Search enabled now!!')
      try:
        a = Lead.objects.get(email=email)
      except ObjectDoesNotExist:
        l = Lead()
        l.first_name = first_name
        l.last_name = last_name
        l.email = email
        l.save()
      return redirect('dScan')
  else:
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

    hof = s.order_by('date_time__minute').filter(grade='A+').distinct()[:8]

    hos = s.order_by('date_time__minute').filter(grade='F').distinct()[:8]

    return render (request, 'evaluator/deep.html', {
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


def dScan (request):
  if request.method == 'POST':
    domain = request.POST['url'].strip()
    # FIX UP SCHEME of URL
    domain = getDomain(domain)
    
    check = checkSite(domain)
    if check == -1:
      # Django Alerts Configurations
      return render  (request, 'evaluator/results.html', {
        'found' : False,
        'site' : domain
      })

    # DOMAIN VALID CASE  
    else: 

      # HOST-NAME
      host = getHostName(domain)

      # IP
      origin = socket.gethostbyname(host)

      # GRADE
      grade = checkGrade(check)

      # ALl headers
      allHeaders = req.get(domain).headers

      # DATE-time
      t = datetime.now(timezone.utc)

      # Make a Scan table entery
      s = Scan()
      s.url = domain
      s.ip = origin
      s.grade = grade
      s.host_name = host
      s.save()
      return render (request, 'evaluator/results.html', {
        'deep' : True,
        'found' : True,
        'grade' : grade,
        'mains' : check.items(),
        'site' : domain,
        'ip' : origin,
        'headers' : getHeaders(allHeaders).items(),
        'date' : t,
        'missing' :  getMissing(check).items(),
        'upcomming' : upcomming.items(),
      })
  else:
    return redirect('deep')


def showResult(request, site):
  #try:
    s = Scan.objects.get(ip=site)    
    domain = s.url
    # HOST-NAME
    host = s.host_name
    # IP
    origin = s.ip
    # GRADE
    grade = s.grade
    # ALl headers
    allHeaders = req.get(domain).headers

    # DATE-time
    t = s.date_time

    return render(request, 'evaluator/results.html', {
      'deep' : s.is_deep,
      'found' : True,
      'grade' : grade,
      'mains' : checkSite(domain).items(),
      'site' : domain,
      'ip' : origin,
      'headers' : getHeaders(allHeaders).items(),
      'date' : t,
      'missing' :  getMissing(checkSite(domain)).items(),
      'upcomming' : upcomming.items()
    })

    
  #except:
    messages.error(request, 'Sorry! This scan is not currently available!!')
    return redirect('home')