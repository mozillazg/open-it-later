#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy

from .models import URL
from .utils import object_does_not_exist
from .utils import get_url_info
from .forms import URLForm


@login_required
def index(request, template_name="", extra_context=None):
    urls = URL.objects.filter(author=request.user)

    context = {
        'urls': urls,
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


@login_required
def add_url(request, template_name="", extra_context=None):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            url_info = get_url_info(url)
            title = url_info['title']
            description = url_info['description']
            note = form.cleaned_data['note']

            URL.objects.create(author=request.user, url=url,
                               title=title, description=description,
                               note=note)
            return HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = URLForm()

    context = {
        'form': form,
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


@login_required
@object_does_not_exist
def visit_url(request, url_id, template_name="", extra_context=None):
    url = URL.objects.get(author=request.user, pk=url_id)

    return HttpResponseRedirect(url)


@login_required
@object_does_not_exist
def delete_url(request, template_name="", extra_context=None):
    if request.method == 'POST':
        try:
            url_id = int(request.POST.get('url_id', 0))
        except ValueError:
            url_id = 0
        URL.objects.get(author=request.user, pk=url_id).delete()

    return HttpResponseRedirect(reverse_lazy('index'))
