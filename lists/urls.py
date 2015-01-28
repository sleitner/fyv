from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
    url(r'', include('django.contrib.auth.urls', namespace='auth')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^new_member_list', 'lists.views.new_member_list', name='new_member_list'),
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    url(r'^logout_view/$', 'lists.views.logout_view', name='logout_view'),
)
