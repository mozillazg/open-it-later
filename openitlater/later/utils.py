#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponseRedirect

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def object_does_not_exist(view_func=None, redirect=None):
    """Decorator for views that catch ObjectDoesNotExist Exception.
    if redirect is None, raise Http404 Exception, otherwise Redirect.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                return view_func(request, *args, **kwargs)
            except ObjectDoesNotExist:
                if redirect:
                    return HttpResponseRedirect(redirect)
                else:
                    raise Http404()
        return _wrapped_view

    if not view_func:
        def foo(view_func):
            return decorator(view_func)
        return foo

    else:
        return decorator(view_func)


def get_url_info(url):
    """Get URL title and description
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:19.0) '
                      'Gecko/20100101 Firefox/19.0',
    }

    try:
        url_r = requests.get(url, headers=headers, cookies=None, stream=True)
    except RequestException:
        return {'title': '', 'description': ''}

    if url_r.status_code == requests.codes.ok:
        html = url_r.text
        soup = BeautifulSoup(html)
        title = soup.title or ''
        if title:
            title = title.string or url
        description = soup.find('meta', {'name': 'description'}) or ''
        if description:
            description = description.get('content', '')
    else:
        title = url
        description = ''

    return {'title': title, 'description': description}
