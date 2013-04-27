# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('BTC', 'BTC'),
)


class Contract(models.Model):
    owner = models.ForeignKey(User)
    source_currency = models.CharField(choices=CURRENCY_CHOICES, default='USD', max_length=50)
    target_currency = models.CharField(choices=CURRENCY_CHOICES, default='BTC', max_length=50)
    rate = models.DecimalField(decimal_places=8, max_digits=12)
    trade_amount = models.DecimalField(decimal_places=8, max_digits=12)
    creation_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    premium_received = models.DateTimeField(null=True, blank=True)
    money_received = models.DateTimeField(null=True, blank=True)
    money_sent = models.DateTimeField(null=True, blank=True)
    recipient_account = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.owner) + '\'s contract at ' + unicode(self.creation_date)