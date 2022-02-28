## NARCISSISTIC TWITTER BOT ##

from tkinter import E
import tweepy

auth = tweepy.OAuth1UserHandler('qBihiBhXCKdtslKUwNd4ZJLlN','ILzBqUcmSuNpHrO2P2xvnnTjWq8itgC0V0bN6JyUHR9ucmuwZb')
auth.set_access_token('905030098692255745-7PwvgSWK0lWrF4aU8ERE1ZiSToylwH7', 'YWbWDJZ1sehdr5Ati0F4gN7flpkh6f2B9dBnce20LEM9P')

api = tweepy.API(auth, wait_on_rate_limit=True)

search_string = 'python'

# # iterates through the tweets with a specific search string and favorites / likes them. 
for tweet in tweepy.Cursor(api.search_tweets, search_string).items(5):
    try:
        tweet.favorite()
        print('Tweet was searched & liked')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break

search_string2 = 'ralphfitt'

# # # iterates through the tweets with a specific search string and favorites / likes them. 
for tweet in tweepy.Cursor(api.search_tweets, search_string2).items(2):
    try:
        tweet.favorite()
        liked_tweet = tweet.text
        print(f'{liked_tweet} was searched & liked !')
    except tweepy.errors.Forbidden as e:
        print(e)
    except StopIteration:
        break

# # iterates through the tweets with a specific search string and retweets 
for tweet in tweepy.Cursor(api.search_tweets, search_string).items(1):
    try:
        tweet.retweet()
        retweet = tweet.text
        print(f'{retweet} was searched & retweeted again !')
    except tweepy.errors.Forbidden as e:
        print(e)
    except StopIteration:
        break