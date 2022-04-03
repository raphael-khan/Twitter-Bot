## GENEROUS TWITTER BOT ##

import tweepy

auth = tweepy.OAuth1UserHandler('','')
auth.set_access_token('', '')

api = tweepy.API(auth, wait_on_rate_limit=True)


# iterates through the followers of a user. Follows back a specifc user. 
for follower in tweepy.Cursor(api.get_followers).items():
    if follower.name == 'Mazen':
        follower.follow()
        print('You have successfully follow back')

# iterates through the followers of a user. Follows back all requests.  
for follower in tweepy.Cursor(api.get_followers).items():
    follower.follow()
    print('You have successfully followed back all requests')

# iterates through the followings of a user. 
for friend in tweepy.Cursor(api.get_friends).items():
    print(friend.name, friend.location)