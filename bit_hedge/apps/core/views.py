# -*- coding: utf-8 -*-

from annoying.decorators import render_to
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect

from bit_hedge.apps.core.forms import *
from bit_hedge.apps.core.models import *
from bit_hedge.apps.core.utils import getRate


@render_to('core/home.html')
def home_view(request):

    form = HomeForm(request.POST or None)
    rate = getRate(two_digits=True)

    if form.is_valid():
        if request.user.is_authenticated():
            user = User.objects.get(pk=request.user.pk)
            Contract.objects.create(
                owner=user,
                rate=rate,
                trade_amount=form.cleaned_data['amount'],
                closing_date=form.cleaned_data['date']
            )
            return redirect(reverse('pay_fee'))
        else:
            return redirect(reverse('register'))
    return {
        'rate': rate,
        'form': form
    }


@render_to('core/pay_fee_view.html')
def pay_fee_view(request):
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