import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '4BxNrNc2312oakaBHCusk3ryo'
csecret = 'PXf9TO8eX1Ec8OvAoM6yREIRufsuMpSEUB20NssnD9iazuKXUs'
atoken = '3297223770-jC5411hhsODUXU6qbqTCbwFujaGliqVTtX9iwFK'
asecret = 'AuIUvuaSwA1qNGHZhhI3XMsR1wR5fonjVRMQAhIKR3d1W'

class listener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["car"])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
