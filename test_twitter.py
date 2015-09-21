from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key="AJYKwrFmDlRUm7TywJ1Qsnytb"
consumer_secret="YpSyGxrgFEVQm0FgCNXAnqKc2PycjykoAr71NX8COO2zgiVr7T"
access_token = "386253530-xlsJkLRR0TYLT92ks7Lk8vUYfDUnJRmq9XFElfqB"
access_token_secret = "lZpELyR4YWSCSJzEjt9tDlodAlq7RV9XdaXFKhJd31yjl"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        #with open("twitter_data.txt", "a") as myfile:
        #    myfile.write(data+"\n")

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Javascript','python','ruby','big data'])
