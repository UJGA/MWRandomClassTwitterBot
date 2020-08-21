import tweepy
import time

auth = tweepy.OAuthHandler('TuhMUyIY2xhRX84cNhfmUC7D6','VCeZOlkheAqr5WpG1unOf4ESwFYGNA4KUV7FV2vpfXcobLSwFh')

auth.set_access_token('1236003676826685441-Iva1MVzx9FcUV9RFscoPBHgoOuv91h','xkHBWA2O3qBOhS3nKmAcR9GgchoPr4pCOyirVCxaEwlW6')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'mwrandomclass'
nrTweets = 500

search2 = '@mwrandomclass'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep:(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search2).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep:(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep:(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

for tweet in tweepy.Cursor(api.search, search2).items(nrTweets):
    try:
        print('Tweet Retweeted')
        tweet.retweet()
        time.sleep:(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break