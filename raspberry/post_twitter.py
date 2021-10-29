#!/usr/bin/env python
import time, os, urllib, urllib2

TEMPERATURA_MAXIMA = 38
TEMPO_MINIMO = 60
BASE_URL = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
KEY = '' # Insira sua chave do ThingTweet.

def tweet(temperatura):
    status = 'Raspberry Pi getting hot -> Temperatura da CPU = ' + temperatura
    data = urllib.urlencode({'api_key' : KEY, 'status': status})
    response = urllib2.urlopen(url=BASE_URL, data=data)
    print(response.read())

def temperatura_cpu():
    captura = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    temperatura_cpu = captura.read()[5:-3]
    return temperatura_cpu

while True:
    temperatura = temperatura_cpu()
    print('CPU Temperatura (C): ' + str(temperatura))
    if temperatura > TEMPERATURA_MAXIMA:
        print('A CPU ta pegando fogo rapaz.')
        tweet(temperatura)
        print('Nao ha mais notificacoes, aguarde: ' + str(TEMPO_MINIMO) + ' minutos.')
        time.sleep(TEMPO_MINIMO * 60)
    time.sleep(1)