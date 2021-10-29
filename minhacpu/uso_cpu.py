import sys
import http.client
import urllib.request
import psutil
from time import sleep

# Chave de escrita do canal
chave = input('Digite sua chave: ')

# URL do canal
base_url = f'https://api.thingspeak.com/update?api_key={chave}'

while True:
    # Obtem percentual de uso da CPU
    uso_cpu = psutil.cpu_percent()

    # Envia o dado para o ThingSpeak
    conexao = urllib.request.urlopen(f'{base_url}&field1={uso_cpu}')
    print(f'O uso da CPU foi: {uso_cpu}%')

    # Fecha a conexão
    conexao.close()
    sleep(5)