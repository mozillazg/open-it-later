#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _


class URLForm(forms.Form):
    url = forms.URLField(label=_('URL'),
                         help_text=_('URL you want open it later.'))
