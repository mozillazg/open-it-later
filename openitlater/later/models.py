#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone


class URL(models.Model):
    """Urls that want open it later
    """
    author = models.ForeignKey(User)
    url = models.URLField(_('URL'))
    title = models.CharField(_('title'), max_length=200, blank=True)
    description = models.TextField(_('description'), blank=True)
    note = models.TextField(_('note'), blank=True)

    date_created = models.DateTimeField(_('date created'), auto_now_add=True,
                                        default=timezone.now)
    last_opened = models.DateTimeField(_('last opened'), auto_now=True,
                                       default=timezone.now)
    is_valid = models.BooleanField(_('valid status'), default=True)

    class Meta:
        verbose_name = _('URL')
        verbose_name_plural = _('URLs')

    def __unicode__(self):
        return self.title or self.url
