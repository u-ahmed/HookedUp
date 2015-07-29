from __future__ import absolute_import, print_function
import tweepy
import logging
import requests
from requests.exceptions import Timeout
from threading import Thread
from time import sleep
import os
import six
import ssl
from emoji import Emoji

##########
# tweepy #
##########

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.models import Status
from tweepy.api import API
from tweepy.error import TweepError
from tweepy.utils import import_simplejson
json = import_simplejson()

''''
if response.success:
    print(response.id)
else:
    print(response.error_code)
    print(response.error_description)
'''

STREAM_VERSION = '1.1'

ckey = '4BxNrNc2312oakaBHCusk3ryo'
csecret = 'PXf9TO8eX1Ec8OvAoM6yREIRufsuMpSEUB20NssnD9iazuKXUs'
atoken = '3297223770-jC5411hhsODUXU6qbqTCbwFujaGliqVTtX9iwFK'
asecret = 'AuIUvuaSwA1qNGHZhhI3XMsR1wR5fonjVRMQAhIKR3d1W'

'''
class listener(StreamListener):
    obselete once StreamListener works
    prints from home feed only

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
'''

class StreamListener(object):
    # main listening class, includes timestamped data.
    def __init__(self, api=None):
        self.api = api or API()

    def on_connect(self):
        # called on connect to streaming server
        return

    def on_data(self, raw_data):
        # called on recieval of raw data
        data = json.loads(raw_data)

        # start of if tree
        if 'in_reply_to_status_id' in data:
            status = Status.parse(self.api, data)
            if self.on_status(status) is False:
                return False
        elif 'delete' in data:
            delete = data['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'event' in data:
            status = Status.parse(self.api, data)
            if self.on_event(status) is False:
                return False
        elif 'direct_message' in data:
            status = Status.parse(self.api, data)
            if self.on_direct_message(status) is False:
                return False

# tokening stuff, will need to be iterated for multiple users, add cookie stuff here.
auth = OAuthHandler(ckey, csecret)
# auth.get_access_token("verifier_value")
auth.set_access_token(atoken, asecret)

'''
filtering code, may be useful.
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["car"])
'''

api = tweepy.API(auth)

public_tweets = api.home_timeline()
f = open('twitterFeed.txt', 'w')
f.write("")
for tweet in public_tweets:
    print (tweet.text)
    f = open('twitterFeed.txt', 'a')
    # f.write('\n')
    f.write(tweet.text)
