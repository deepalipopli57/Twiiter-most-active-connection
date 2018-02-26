import twitter
from django.shortcuts import render
from most_active_connections.local_settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

#API for fetch most active 10 users for given twitter credentials as in the local_settings.py
def most_active_users(request):
    user = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=user)
    search_results = twitter_api.search.tweets(q="#top", count=20)
    statuses = search_results['statuses']
    screen_names = [user_mention['screen_name']
                    for status in statuses
                    for user_mention in status['entities']['user_mentions']][0:10]
    return render(request, 'users.html', {'data': screen_names})



