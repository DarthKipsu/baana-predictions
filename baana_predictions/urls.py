from django.conf.urls import patterns, include, url

import hello.views

urlpatterns = patterns('',

    url(r'^$', hello.views.index, name='index'),

)
