# Add email to requested authorizations.
LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',] 
# Add the fields so they will be requested from linkedin.
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'user_friends',
    'friends_location',
    'user_likes',
]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/plus.login',
]
LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                       ('firstNameame', 'first_name'),
                       ('lastName', 'last_name'),]
#-------------
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
#    'thirdauth.save_profile',  # <--- set the import-path to the function
