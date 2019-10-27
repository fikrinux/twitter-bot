import tweepy
import datetime
import xlsxwriter
import sys

# credentials from https://apps.twitter.com/
consumerKey = "nAzFNx7KkYahMpV5oCW9Ro67Y"
consumerSecret = "OnCQlkk2cNUl4oCKfIIFNZYe3RiHVTcLsfKLF3ozX2LuvEmlYA"
accessToken = "84760701-efAy6hpzFAqCrnOQvXIpArDy2ooaAzc1GH1Blzvy6"
accessTokenSecret = "ttJh7sVsbrjITdGQeVpRT8XTfy1HsLzGWFQiciSs9Of5K"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

username = sys.argv[1]
startDate = datetime.datetime(2019, 10, 22, 0, 0, 0)
endDate =   datetime.datetime(2019, 10, 24, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(sandiuno)
for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")
