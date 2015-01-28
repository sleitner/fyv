import string
import tweepy

def containsany(str, set=string.punctuation):
    for c in set:
        if c in str: return True;
    return False;
#read dictionary of name:[nick1,nick2,nick3] and add those nicknames to the friends list
#def nicknames(firstname):
#    return list_tnames = nicknames_dict.get(firstname,'')

def process_friend(friend): 
    name = friend.name.split()
    if (len(name)==2 or len(name)==3) and \
            name[0] != 'The' and \
            not containsany(name[0]+name[-1]):
        firstname = name[0]
        lastname = name[-1]
        return {'firstname':firstname,'lastname':lastname, 'location':friend.location}
    return 

from django.conf import settings
def authenticate_twitter(request):
    try:
        social_user = request.user.social_auth.filter(provider='twitter',).get()
    except ObjectDoesNotExist:
        return redirect(getattr(settings,'LOGIN_URL','/'))
    consumer_key = getattr(settings,'SOCIAL_AUTH_TWITTER_KEY')
    consumer_secret = getattr(settings,'SOCIAL_AUTH_TWITTER_SECRET')
    authid = tweepy.OAuthHandler(consumer_key, consumer_secret)
    access_token = social_user.tokens['oauth_token']
    access_token_secret = social_user.tokens['oauth_token_secret']
    authid.set_access_token(access_token, access_token_secret)
    return authid

def get_twitter_friends(request):
    authid = authenticate_twitter(request)
    api = tweepy.API(authid)
    # Iterate through all of the authenticated user's friends
    #http://tweepy.readthedocs.org/en/v3.1.0/code_snippet.html
    friend_props = [] # just name and location now
    for friend in tweepy.Cursor(api.friends).items():
        # Process the friend here
        prop = process_friend(friend)
        if prop:
            friend_props.append(prop)
    return friend_props
