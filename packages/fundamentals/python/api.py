""" 
API: Application Program Interface
Abstract that it specifies an interface and controls the behavior
of the objects specified in that interface.
The software that provides the functionality described by an API is said
to be an implementation of the API. 
An API is typically defined in terms of the programming language
used to build an application.
 """

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
request = urllib.request.urlopen("https://api.github.com/users/laksmitawidya", context=ctx)

""" 
adding query param
request = "https://api.github.com/users/laksmitawidya" + urllib.parse.urlencode({'name': "laksmitawidya"})
 """
 
try:
    response = json.load(request)
except:
    response = None

print(response)

if not response or 'status' not in response or response['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(response)

name = response["name"]
url = response["url"]
location = response["location"]
print("\n\nGithub Profile : \nname:", name, "\nurl:",url, "\nlocation:", location)