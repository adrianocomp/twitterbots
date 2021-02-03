import twitter_follow_bot

####Automatically follow any users that tweet something with a specific phrase

from twitter_follow_bot import auto_follow

auto_follow("")
###You can also search based on hashtags.

###By default, the bot looks up the 100 most recent tweets. You can change this number with the count parameter:

from twitter_follow_bot import auto_follow

auto_follow("", count=100)
####Automatically follow any users that have followed you

from twitter_follow_bot import auto_follow_followers

auto_follow_followers()
####Automatically favorite any tweets that have a specific phrase

from twitter_follow_bot import auto_fav

auto_fav("", count=100)
####Automatically retweet any tweets that have a specific phrase

from twitter_follow_bot import auto_rt

#auto_rt("phrase", count=100)
####Automatically unfollow any users that have not followed you back (with exceptions that you can set)

###from twitter_follow_bot import auto_unfollow_nonfollowers

###auto_unfollow_nonfollowers()
