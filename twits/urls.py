from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twits.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

     url(r'^$', 'tweets.views.home', name='home'),

    url(r'^tweets/$', 'tweets.views.tweets', name='tweets'),
)
