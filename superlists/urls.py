from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^logout_view/$', 'lists.views.logout_view', name='logout_view'),
    url(r'^FAQ.html', 'lists.views.faq', name='faq'),
    url(r'^new_member_list', 'lists.views.new_member_list', name='new_member_list'),
    url(r'^slides.html', 'lists.views.slides', name='slides'),
    url(r'^motivation.html', 'lists.views.motivation', name='motivation'),
    url(r'^modeling.html', 'lists.views.modeling', name='modeling'),
    url(r'^testlogin.html', 'lists.views.testlogin', name='testlogin'),
    url(r'^overview.html', 'lists.views.overview', name='overview'),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
