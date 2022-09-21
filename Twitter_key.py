#TwitterAPIv2の準備　それぞれの入力値はTwitter開発者アカウントで準備

import tweepy
def twitter_key():
    consumer_key = '**********************'
    consumer_secret = '**********************'
    access_token = '**********************'
    access_token_secret = '**********************'
    bearer_token= '**********************'
    
    id = 'tweet_id'
    
    client = tweepy.Client(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret,
        bearer_token=bearer_token )