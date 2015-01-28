from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^FAQ.html', 'lists.views.faq', name='faq'),
    url(r'^motivation.html', 'lists.views.motivation', name='motivation'),
    url(r'^analytics.html', 'lists.views.analytics', name='analytics'),
    url(r'^testlogin.html', 'lists.views.testlogin', name='testlogin'),
    url(r'^input.html', 'lists.views.input', name='input'),
    url(r'^lists/', include('lists.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
