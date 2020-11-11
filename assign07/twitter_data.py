#   Author: Cheryl Dugas

#  This program accesses data from a twitter user site (hard-coded as Stevens)

#  To run in a terminal window:   python3  twitter_data.py


import tweepy

### PUT AUTHENTICATOIN KEYS HERE ###
CONSUMER_KEY = "ynX0tNLLLgbE4Z65wtxejEllU"
CONSUMER_KEY_SECRET = "uA1NM8QjzvNkVTxOgyzbH6C6kxvQPJeuIo4VCyuaPbuILQl9xH"
ACCESS_TOKEN = "352837898-7reEbg6uNTrnt0kf6bqIAG6bDTCoiEDhbsPn4s5u"
ACCESS_TOKEN_SECRET = "KKJCCzHRsHT1Wd2Z0Qx467kBmSMYpbP9DddcPRRI3mN36"

# Authentication

authenticate = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
authenticate.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#  use wait_on_rate_limit to avoid going over Twitter's rate limits
api = tweepy.API(authenticate, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)
                 
# Get Information About a Twitter User Account

twitter_user = api.get_user('FollowStevens')

# Get Basic Account Information
print("twitter_user id: ", twitter_user.id)

print("twitter_user name: ", twitter_user.name)

# Determine an Account’s Friends 
friends = []

print("\nFirst 5 friends:")

# Creating a Cursor
cursor = tweepy.Cursor(api.friends, screen_name='FollowStevens')

# Get and print 5 friends
for account in cursor.items(5):
    print(account.screen_name)
    