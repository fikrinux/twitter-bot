# tweepy-bots/bots/config.py
import tweepy
import logging

logger = logging.getLogger()

def create_api():
    consumer_key = ("nAzFNx7KkYahMpV5oCW9Ro67Y")
    consumer_secret = ("OnCQlkk2cNUl4oCKfIIFNZYe3RiHVTcLsfKLF3ozX2LuvEmlYA")
    access_token = ("84760701-efAy6hpzFAqCrnOQvXIpArDy2ooaAzc1GH1Blzvy6")
    access_token_secret = ("ttJh7sVsbrjITdGQeVpRT8XTfy1HsLzGWFQiciSs9Of5K")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
