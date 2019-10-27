#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import datetime

from tweepy import OAuthHandler, Stream, StreamListener

consumer_key="nAzFNx7KkYahMpV5oCW9Ro67Y"
consumer_secret="OnCQlkk2cNUl4oCKfIIFNZYe3RiHVTcLsfKLF3ozX2LuvEmlYA"
access_token="84760701-efAy6hpzFAqCrnOQvXIpArDy2ooaAzc1GH1Blzvy6"
access_token_secret="ttJh7sVsbrjITdGQeVpRT8XTfy1HsLzGWFQiciSs9Of5K"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[46]:


tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)


# In[65]:


user_tweets = api.user_timeline(screen_name='agnezmo', count=200, tweet_mode="extended")
for tweet in user_tweets:
    print(tweet._json)


# In[62]:


the_list = []
ambiltwit = api.user_timeline(screen_name='sandiuno', count=200, tweet_mode="extended")
startDate = datetime.datetime(2019, 10, 22, 00, 00, 00)
endDate =   datetime.datetime(2019, 10, 24, 00, 00, 00)

for tweet in ambiltwit:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        the_list.append(tweet._json)


# In[64]:


import pandas
myData = pandas.DataFrame(the_list)
myData


# In[ ]:





# In[ ]:




