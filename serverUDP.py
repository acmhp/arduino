#!/usr/bin/env python3

#Versão Inicial
#Data: 22.09.2019
#Ana Carmen Machado
#Alterações:
#23.09.2019
#24.09.2019
#25.09.2019
#26.09.2019
#29.09.2019

import socket

HOST = '192.168.0.101'  # Standard loopback interface address (localhost)
#HOST = socket.gethostname()
PORT = 5000       # Port to listen on (non-privileged ports are > 1023)
SIZE_PACKET = 2048

# AF_INET - Familia de endereço para ipv4 e SOCK_STREAM é para TCP.
# bind é usado para associar o socket a uma interface de rede e um número de porta especificos.
# listen - numero de conexões
# accept bloqueia e aguarda por uma conexão de entrada, quando cliente conecta, ele retorna um novo objeto de socket.
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST,PORT))

print ('Iniciando UDP Server Arduino...')
print ('IP: '+str(HOST))
print ('Porta: '+str(PORT))

while True:
  data, addr = udp.recvfrom(2048)
#print ("")
  if len(data.decode('utf8'))is None:

    print('Mensagem None')

  else:
    print ('Mensagem recebida:', data)
    print ('IP Arduino Remoto:', addr[0])


