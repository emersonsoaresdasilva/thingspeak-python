#!/usr/bin/env python3
from time import sleep
import sys
import http.client
import urllib.request
import random

random.seed()

chave = input('Digite sua chave: ')

base_url = 'https://api.thingspeak.com/update?api_key=%s' % chave

while True:
    valor = random.randint(0, 30)
    conexao = urllib.request.urlopen(base_url + "&field2=" + str(valor))
    print('O valor enviado foi: '+str(valor))
    conexao.close()
    sleep(3)