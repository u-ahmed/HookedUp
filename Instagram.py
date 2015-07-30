from instagram.client import InstagramAPI

access_token = "233291163.8a612cd.c49f77de073746e9a2f53116b720302e"
client_secret = "f17ce3c97eb14fd2b03f123c1900f973"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media = api.user_recent_media(user_id='ahmed_enigma', count=10)
for media in recent_media:
   print (media.images['standard_resolution'].url)
