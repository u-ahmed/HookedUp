from instagram.client import InstagramAPI

access_token = ""
client_secret = ""
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next = api.user_recent_media(user_id)
