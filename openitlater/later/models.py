#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class TOpen(models.Model):
    """Urls that want open it later
    """
    author = models.ForeignKey(User)
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    note = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_opened_at = models.DateTimeField(auto_now=True)
    is_invalid = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs To Open Later')

    def __unicode__(self):
        return self.title
