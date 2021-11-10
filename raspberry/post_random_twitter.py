#!/usr/bin/env python3
import urllib
import time
from urllib.request import urlopen
from urllib.parse import urlencode
from random import randint

BASE_TWITTER = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
TWITTER_KEY = '' # Insira sua chave do ThingTweet.
CHANNEL_KEY = '' # Insira sua chave do ThingSpeak.
BASE_SPEAK = 'https://api.thingspeak.com/update?api_key=%s' % CHANNEL_KEY

def tweet(numero):
    status = 'O numero enviado foi maior que 75 -> O numero enviado foi = ' + str(numero)
    data = urlencode({'api_key' : TWITTER_KEY, 'status': status})
    response = urlopen(url=BASE_TWITTER, data=data.encode('utf-8'))

while True:
    numero = randint(0, 100)
    conexao = urlopen(BASE_SPEAK + "&field1=" + str(numero))
    print('O numero recebido foi: ' + str(numero))
    conexao.close()
    if numero > 75:
        print('O numero enviado foi: ' + str(numero))
        tweet(numero)
    time.sleep(15)
# python3 post_random_twitter.py