## NARCISSISTIC TWITTER BOT ##

from tkinter import E
import tweepy

auth = tweepy.OAuth1UserHandler('','')
auth.set_access_token('', '')

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

# search_string2 = 'ralphfitt'

# # # # iterates through the tweets with a specific search string and favorites / likes them. 
# for tweet in tweepy.Cursor(api.search_tweets, search_string2).items(2):
#     try:
#         tweet.favorite()
#         liked_tweet = tweet.text
#         print(f'{liked_tweet} was searched & liked !')
#     except tweepy.errors.Forbidden as e:
#         print(e)
#     except StopIteration:
#         break

# # # iterates through the tweets with a specific search string and retweets 
# for tweet in tweepy.Cursor(api.search_tweets, search_string).items(1):
#     try:
#         tweet.retweet()
#         retweet = tweet.text
#         print(f'{retweet} was searched & retweeted again !')
#     except tweepy.errors.Forbidden as e:
#         print(e)
#     except StopIteration:
#         break