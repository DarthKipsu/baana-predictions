from django.conf.urls import patterns, include, url

import src.views

urlpatterns = patterns('',

    url(r'^$', src.views.index, name='index'),

)
