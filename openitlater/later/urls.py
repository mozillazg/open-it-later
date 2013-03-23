#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url

from .views import index
from .views import visit_url
from .views import add_url
from .views import delete_url
from .views import search

urlpatterns = patterns(
    'later.views',
    url(r'^$', index, name='index'),
    url(r'go/(?P<url_id>\d+)$', visit_url, name='visit'),
    url(r'^search$', search, name='search'),
    url(r'^add$', add_url, name='add'),
    url(r'^delete$', delete_url, name='delete')
)
