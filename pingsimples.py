import os  # importar a biblioteca ou modulo os (integra os programas e recursos do sistema operacional

print("#" * 60)
ip_ou_host = input("Digite o Endereço IP ou Host a ser verificado: ")
print("-" * 60)
os.system(f'ping -n 6 {ip_ou_host}')  # executa um comando do sistema operacional, ou seja, ping "-n" numero de pacotes
print("-" * 60)