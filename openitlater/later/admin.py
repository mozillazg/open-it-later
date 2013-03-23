#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created',
                    'last_opened', 'is_valid')
    search_fields = ('title', 'description', 'note')
    list_filter = ('date_created', 'last_opened', 'is_valid')

admin.site.register(URL, URLAdmin)
