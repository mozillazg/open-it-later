#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import TOpen


class TOpenAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at',
                    'last_opened_at', 'is_invalid')
    search_fields = ('title', 'description', 'note')
    list_filter = ('created_at', 'last_opened_at', 'is_invalid')

admin.site.register(TOpen, TOpenAdmin)
