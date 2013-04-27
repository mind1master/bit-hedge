# -*- coding: utf-8 -*-
# put misc functions that are used in models, views, tags, etc.

# USD to BTC
import json
import urllib2


def getRate() :
    v = urllib2.urlopen(urllib2.Request(url = 'http://data.mtgox.com/api/1/BTCUSD/ticker'))
    vv = v.read()
    res = json.loads(vv)

    btcToUsdRate = res['return']['last_all']['value']
    if btcToUsdRate :
        return 1 / float(btcToUsdRate)

    return 'unavailable'

def getPremium(rate, date, amount) :
    #TODO
    return amount * 0.035
