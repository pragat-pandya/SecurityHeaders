import requests as req
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


missingDiscriptions = {
  'Content-Security-Policy' : 'is an effective measure to protect your site from XSS attacks. By whitelisting sources of approved content, you can prevent the browser from loading malicious assets.',
  'X-Frame-Options' : 'tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value "X-Frame-Options: SAMEORIGIN".',
  'X-Content-Type-Options' : 'stops a browser from trying to MIME-sniff the content type and forces it to stick with the declared content-type. The only valid value for this header is "X-Content-Type-Options: nosniff".',
  'Referrer-Policy' : 'is a new header that allows a site to control how much information the browser includes with navigations away from a document and should be set by all sites.',
  'Permissions-Policy' : 'is a new header that allows a site to control which features and APIs can be used in the browser.',
  'Strict-Transport-Security' : ' informs browsers that the site should only be accessed using HTTPS, and that any future attempts to access it using HTTP should automatically be converted to HTTPS.'
}

upcomming = {
  'Cross-Origin-Embedder-Policy' : 'allows a site to prevent assets being loaded that do not grant permission to load them via CORS or CORP.',
  'Cross-Origin-Opener-Policy' : 'allows a site to opt-in to Cross-Origin Isolation in the browser.',
  'Cross-Origin-Resource-Policy' : 'allows a resource owner to specify who can load the resource.'

}

def getDomain (domain):
  if domain.startswith('http'):
    pass
  else:
    domain = "https://"+domain

  return domain

def getHostName(domain):
  parsed_uri = urlparse(domain)
  if parsed_uri.netloc == "" or parsed_uri.scheme == "": 
    # User only entered www.name.com without http prefix
    host = domain
  else:
    # User entered with http prefix
    host = parsed_uri.netloc
    # If starts with www remove it
    if host.startswith("www."):
      host.replace('www.', '')
      host = host.strip()
  return host

# RETURNS: Dict('header':True/False) if domain valid
# ELSE: 
def checkSite (domain):
  disable_warnings(InsecureRequestWarning)
  try:
    h = req.get(domain)
    headers = h.headers
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
    
    return myHeaders

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


def getHeaders(headers):
  allHeads = {}
  for key, value in headers.items():
    allHeads[key] = value
  return allHeads



def getMissing(mainHeads):
  missing = {}
  for key, value in mainHeads.items():
    if not value:
      missing[key] = missingDiscriptions[key]
  return missing