
#http://axiacore.com/blog/how-retrieve-facebook-extra-info-from-django/
# def get_facebook_friends(request):
#    social_user = ''
#    try:
#       social_user = request.user.social_auth.filter(provider='facebook',).first()
#    except: 
#       pass
#    if social_user:
#       url = u'<a href="https://graph.facebook.com/{0}/">https://graph.facebook.com/{0}/</a>' \
#             u'friends?fields=id,name,location,picture' \
#             u'&access_token={1}'.format(
#          social_user.uid,
#          social_user.extra_data['access_token'],
#          )
#       #request = urllib.request(url)
#       friends = json.loads(urllib.urlopen(url).read()).get('data')
#       for friend in friends:
#          location = friend.get('location')
#          print(location)
#    else:
#       print('no facebook provider?')
#    # do something



#Let’s say we are interested in storing the user profile link, the gender and the timezone in our Profile
# def save_profile(backend, user, response, *args, **kwargs):
#     if backend.name == 'facebook':
#         profile = user.get_profile()
#         if profile is None:
#             profile = Profile(user_id=user.id)
#         profile.gender = response.get('gender')
#         profile.link = response.get('link')
#         profile.timezone = response.get('timezone')
#         profile.save()
