#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import auth


def register(request, template_name="", extra_context=None):
    if request.method == 'POST':
        form = None
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username, email=email, password=password)
    else:
        form = None

    context = {
        'form': form,
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


@login_required
def login(request, template_name="", extra_context=None):
    if request.method == 'POST':
        form = None
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(username, email=email, password=password)
    else:
        form = None

    context = {
        'form': form,
    }
    if extra_context:
        context.update(extra_context)
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))
