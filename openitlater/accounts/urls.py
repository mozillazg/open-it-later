#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from django.conf.urls import url

from .views import login

urlpatterns = patterns(
    'accounts.views',
    url(r'^login$', login, name='login')
)
