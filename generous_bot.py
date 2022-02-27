## GENEROUS TWITTER BOT THAT ACCEPTS FOLLW REQUEST & ALWAYS FOLLOWS BACK ##
import tweepy

auth = tweepy.OAuth1UserHandler('qBihiBhXCKdtslKUwNd4ZJLlN','ILzBqUcmSuNpHrO2P2xvnnTjWq8itgC0V0bN6JyUHR9ucmuwZb')
auth.set_access_token('905030098692255745-7PwvgSWK0lWrF4aU8ERE1ZiSToylwH7', 'YWbWDJZ1sehdr5Ati0F4gN7flpkh6f2B9dBnce20LEM9P')

api = tweepy.API(auth, wait_on_rate_limit=True)


for follower in tweepy.Cursor(api.get_followers).items():
    if follower.name == 'Mazen':
        follower.follow()
        print('You have successfully follow back')