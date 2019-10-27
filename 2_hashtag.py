import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'nAzFNx7KkYahMpV5oCW9Ro67Y'
consumer_secret = 'OnCQlkk2cNUl4oCKfIIFNZYe3RiHVTcLsfKLF3ozX2LuvEmlYA'
access_token = '84760701-efAy6hpzFAqCrnOQvXIpArDy2ooaAzc1GH1Blzvy6'
access_token_secret = 'ttJh7sVsbrjITdGQeVpRT8XTfy1HsLzGWFQiciSs9Of5K'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('hashtag.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

#masukkan hashtag dalam kurung di bawah setelah kode q=
for tweet in tweepy.Cursor(api.search,q="#makassar",count=100,
                           lang="en",
                           since="2019-10-22").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
