from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^login/$', 'registration.views.login', name='login'),
    url(r'^logout/$', 'registration.views.logout', name='logout'),
    url(r'^request_email_confirmation/$',
        'registration.views.request_email_confirmation',
        name='request_email_confirmation'),
    url(r'^oauth_callback/(?P<service>\w+)/$',
        'registration.views.oauth_callback',
        name='oauth_callback'),
    url(r'^confirm_email/(?P<pk>\d+)/(?P<token>\w+)/$',
        'registration.views.confirm_email', name='confirm_email'),
)
