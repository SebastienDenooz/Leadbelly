# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from projects.api.resources import UserResource

v1_api = Api()
v1_api.register(UserResource())

from projects.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tuto_django.views.home', name='home'),
    # url(r'^tuto_django/', include('tuto_django.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProjectsView.as_view(), name='projects-list'),
    url(r'^add/$', ProjectCreateView.as_view(), name='project-create'),
    url(r'^api/', include(v1_api.urls)),
)

