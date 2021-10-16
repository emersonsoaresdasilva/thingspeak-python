import sys
import http.client
import urllib.request
import psutil
from time import sleep

# Chave de escrita do canal
chave = input('Digite sua chave: ')

# URL do canal
base_url = f'https://api.thingspeak.com/update?api_key={chave}'

# Exemplo funcional em Linux:
# def temperatura_processador():
#     # Obtêm informação da frequência do processador
#     captura = "cat /sys/class/thermal/thermal_zone0/temp"
#     temperatura = subprocess.check_output(captura, shell=True)
#     return float(temperatura) / 1000
#     # Exemplo: temperatura_processador = str(temperatura_processador())

while True:
    # Obtem percentual de uso da CPU
    uso_cpu = psutil.cpu_percent()

    # Envia o dado para o ThingSpeak
    conexao = urllib.request.urlopen(f'{base_url}&field1={uso_cpu}')
    print(f'O uso da CPU foi: {uso_cpu}%')

    # Fecha a conexão
    conexao.close()
    sleep(5)