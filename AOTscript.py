import tweepy
import time
import os
from os import environ

consumer_key = "5w6cFZtcYCWKi9gZD8q4jear4"
consumer_secret = "VWkFytthGZ954R1U8EI3UHvXLr5O5rmqQVMdWggp3rBzGbQZqc"
access_token = "1265090303502938114-QpIjRy2l8M9BmhPIjC63Jb77wL6zEp"
access_token_secret = "xoK7wHzlU8dkVWUh0K3fT1v1ZrX6BfaWSNSFxwSj84zl6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
for i in range(1, 1851):
    f = open("num.txt", "r+")
    f.seek(0)
    number = f.read()
    filename = f"Random/({number}).jpg"
    status = ""
    api.update_with_media(filename, status)
    f.seek(0)
    f.truncate()
    f.write(f"{int(number)+1}")
    time.sleep(17280)
    f.close()