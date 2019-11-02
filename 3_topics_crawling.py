from __future__ import absolute_import, print_function

from tweepy import OAuthHandler, Stream, StreamListener

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="nAzFNx7KkYahMpV5oCW9Ro67Y"
consumer_secret="OnCQlkk2cNUl4oCKfIIFNZYe3RiHVTcLsfKLF3ozX2LuvEmlYA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="84760701-efAy6hpzFAqCrnOQvXIpArDy2ooaAzc1GH1Blzvy6"
access_token_secret="ttJh7sVsbrjITdGQeVpRT8XTfy1HsLzGWFQiciSs9Of5K"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['rendang','coto','sate','kapurung','indomie'])
