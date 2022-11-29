from django.shortcuts import render, redirect
import requests as req
from application.urls import home

# Create your views here.
def queryProcessor (request):

  if request.method == 'POST':
    domain = request.POST['url'].strip()
    headers = checkSite(domain)
  
    if headers == -1:
      # Django Alerts Configurations
      return redirect(home)
  
    else:
      grade = checkGrade(headers)
  
      return render (request, 'results.html', {
        'grade' : grade,
        'headers' : headers
      })
  
    return redirect(home)
  
  else:
    return redirect(home)


# RETURNS: Dict('header':True/False) if domain valid
# ELSE: 
def checkSite (domain):
  
  try:
  
    headers = req.get(domain).headers
    myHeaders = {}
  
    #1
    if 'Strict-Transport-Security' in headers:
      myHeaders['Strict-Transport-Security'] = True
    else:
      myHeaders['Strict-Transport-Security'] = False
  
    #2
    if 'Content-Security-Policy' in headers:
      myHeaders['Content-Security-Policy'] = True
    else:
      myHeaders['Content-Security-Policy'] = False
  
    #3
    if 'X-Content-Type-Options' in headers:
      myHeaders['X-Content-Type-Options'] = True
    else:
      myHeaders['X-Content-Type-Options'] = False
  
    #4
    if 'Referrer-Policy' in headers:
      myHeaders['Referrer-Policy'] = True
    else:
      myHeaders['Referrer-Policy'] = False
  
    #5
    if 'Permissions-Policy' in headers:
      myHeaders['Permissions-Policy'] = True
    else:
      myHeaders['Permissions-Policy'] = False
  
    #6
    if 'X-Frame-Options' in headers:
      myHeaders['X-Frame-Options'] = True
    else:
      myHeaders['X-Frame-Options'] = False
    
    return headers

  except:
    return -1  


# Returns the grade acheived 
def checkGrade (headers):
  
  grade = 0
  
  for key in headers:
    if headers[key] == True:
      grade += 1
  
  if grade == 0:
    return 'F'
  
  elif grade == 1:
    return 'E'
  
  elif grade == 2:
    return 'D'
  
  elif grade == 3:
    return 'C'
  
  elif grade == 4:
    return 'B'
  
  elif grade == 5:
    return 'A'
  
  else:
    return 'A+'