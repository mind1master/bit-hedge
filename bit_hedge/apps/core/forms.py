# -*- coding: utf-8 -*-

from django import forms


class HomeForm(forms.Form):
    date = forms.DateField(input_formats=[
        '%Y-%m-%d',       # '2006-10-25'
        '%m/%d/%Y',       # '10/25/2006'
        '%m/%d/%y',
        '%d.%m.%y',
    ])
    amount = forms.DecimalField()


class BitcoinRecipient(forms.Form):
    bitcoin_recipient = forms.CharField(max_length=100)


class RegisterForm(BitcoinRecipient):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

