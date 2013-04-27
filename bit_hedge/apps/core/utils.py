# -*- coding: utf-8 -*-
# put misc functions that are used in models, views, tags, etc.

# USD to BTC
def getRate() :
    rate = 0.139
    return rate

def getPremium(rate, date, amount) :
    #TODO
    return amount * 0.035
