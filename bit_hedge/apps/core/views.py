# -*- coding: utf-8 -*-

from annoying.decorators import render_to

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from bit_hedge.apps.core.forms import *


@render_to('core/home.html')
def home_view(request):
    form = HomeForm()
    return {
        'form': form,
    }


@render_to('core/first_step.html')
def first_step_view(request):
    form = None
    if request.user.is_authenticated() and not request.user.is_anonymous():
        form = RegisterForm()
    else:
        form = BitcoinRecipient()
    return {
        'from': form,
        }