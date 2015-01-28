

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'PORT': '3306',
        # ------- laptop
         'HOST': 'localhost',
         'NAME': 'test_djangotest',
         'USER': 'root',
         'PASSWORD': '',
    },
    'votersdb': {
        'ENGINE': 'mysql.connector.django',
        'PORT': '3306',
        # ------- laptop
        'HOST': 'localhost',
        'NAME': 'voter_history',
        'USER': 'root',
        'PASSWORD': '',
    }
}
