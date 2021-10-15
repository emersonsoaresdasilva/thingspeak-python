import sys
import http.client
import urllib.request
import random
from time import sleep

# Inicia a semente dos números pseudo randômicos
random.seed()

# Chave de escrita do canal
chave = input('Digite sua chave: ')

# URL do canal
base_url = f'https://api.thingspeak.com/update?api_key={chave}'

while True:
    valor = random.randint(0, 30)
    # Envia dado para o ThingSpeak
    conexao = urllib.request.urlopen(f'{base_url}&field1={valor}')
    print(f'O valor enviado foi: {valor}')
    # Encerra a conexão
    conexao.close()
    sleep(3)
