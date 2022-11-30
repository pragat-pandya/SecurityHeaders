from django.shortcuts import render, redirect
import requests as req
from application.urls import home
import socket
from datetime import datetime, timezone
from .packages import *
from .models import *

# Create your views here.
def queryProcessor (request):
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

      return render (request, 'evaluator/results.html', {
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
    return redirect(home)





