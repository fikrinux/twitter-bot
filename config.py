# tweepy-bots/bots/config.py
import tweepy
import logging

logger = logging.getLogger()

def create_api():
    consumer_key = ("cari kode seperti cAzHGx7KkYahMpV5oCW9Ro67Y")
    consumer_secret = ("cari kode seperti OnCQlkk2cNUl4oCKfIIFROWe3RiHVTcLsfKLF3ozX2LuvEmlYA")
    access_token = ("cari kode seperti 84760701-efAy6hpzFAqCrnOQvENJirDy2ooaAzc1GH1Blzvy6")
    access_token_secret = ("cari kode seperti ttJh7sVsbttYTdGQeVpRT8XTfy1H4iuzGWFQiciSs991K")

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
