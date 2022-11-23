import os
import time

with open('hosts.txt') as file:  # abrindo arquivo
    dump = file.read()  # lendo o arquivo
    dump = dump.splitlines() # organizando o arquivo em linhas separadas

    for ip in dump:  # iterando o arquivo para testar cada ip ou host
        print(f"Verificando o ip: {ip}")
        print('-' * 60)
        os.system(f'ping -n 2 {ip}')
        print('-' * 60)
        time.sleep(5)  # 5 segundos de espera a cada verificada de ip