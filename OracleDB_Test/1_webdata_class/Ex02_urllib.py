from urllib import request
import ssl
from urllib.error import URLError, HTTPError
ssl._create_default_https_context = ssl._create_unverified_context

site = request.urlopen("https://www.google.com/")
page = site.read()
# print(site)
# print(page)

#print(site.status)

try :
    site = request.urlopen("https://www.google.com/")

except HTTPError as e:
    print("HTTP Error")

except URLError as e:
    print("URL Error")
else:
    print(site)