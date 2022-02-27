import tweepy
import time

auth = tweepy.OAuthHandler('GyC3ubAuWQQRBKh8UbWSBhZnP','NspD5vG8aazUcKdAwWKyqhShWRUrdnVEieqMTiuSfKObJsp9DG')
auth.set_access_token('905030098692255745-Qq7aBWs3JgLQ8LrSgvNWTMBIsKUPSEb', 'UupMA9UPMhQGXZPacTPEq7PRJy9sss5iqWt8opAuPHwuG')

api = tweepy.API(auth)

public_tweets = api.home_timeline() # Timeline. 
for tweet in public_tweets:
    print(tweet.text)

tweets = api.user_timeline() # Personal timeline or status posted. 
for tweet in tweets:
    print(tweet.text)


user = api.get_user(screen_name='ralphfitt') # finds a user. returns a dict. 
print(user.name)

user = api.me() # my info. returns a dict. 
print(user.screen_name)
print(user.name)
print(user.followers_count)

# Helper function to handle the rate limit for the API by delaying the function by 1 second. 
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.errors.TooManyRequests:
        time.sleep(5)