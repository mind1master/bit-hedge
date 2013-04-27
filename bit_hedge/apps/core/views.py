# -*- coding: utf-8 -*-

from annoying.decorators import render_to
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect

from bit_hedge.apps.core.forms import *


@render_to('core/home.html')
def home_view(request):
    form = HomeForm()
    return {
        'form': form,
    }


@render_to('core/first_step.html')
def first_step_view(request):
    if request.user.is_authenticated() and not request.user.is_anonymous():
        form = BitcoinRecipient()
        user = request.user
    else:
        form = RegisterForm()
        user = None
    return {
        'form': form,
        'user': user,
    }

@render_to('core/second_step.html')
def second_step_view(request):
    if request.method != 'POST':
        return redirect('home_view')
    return {}

@render_to('core/register.html')
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('home_page'))
    return {
        'form': form,
    }