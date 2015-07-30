from instagram.client import InstagramAPI
import httplib2
import json
import requests
import sys

client_id = "8a612cd650344523808233c0468c80ed"
access_token = "233291163.8a612cd.c49f77de073746e9a2f53116b720302e"
client_secret = "f17ce3c97eb14fd2b03f123c1900f973"
redirect_uri = "http://u-ahmed.github.io/HookedUp/instagram.html" 
scope = ''
user_id = "233291163"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next = api.user_recent_media(user_id='user_id', count=10)
for media in recent_media:
   print (media.text)
