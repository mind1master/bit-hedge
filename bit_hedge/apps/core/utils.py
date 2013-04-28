# -*- coding: utf-8 -*-
# put misc functions that are used in models, views, tags, etc.

# USD to BTC
import json
from math import sqrt
import urllib2


def getRate(two_digits=False):
    try:
        v = urllib2.urlopen(urllib2.Request(url='http://data.mtgox.com/api/1/BTCUSD/ticker'))
    except:
        return 'Failed to fetch'

    if v is None:
        return 0

    vv = v.read()
    res = json.loads(vv)

    btcToUsdRate = float(res['return']['last_all']['value'])
    if two_digits:
        btcToUsdRate = round(btcToUsdRate, 2)
    return btcToUsdRate

def getPremium(rate, date, amount) :
    # Fee = [E(St) - So] + A * sigma * sqrt(N)+ profit

    fee = amount * 0.1 * 0.2 * (sqrt(2)) + 1
    return round(fee, 2)
