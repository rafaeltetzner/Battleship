import socket

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = socket.gethostname()
SERVER_PORT = 1234
MSG_BUFF_SIZE = 32 # Tamanho mínimo de mensagem pelo protocolo TCP = 20

client.connect((SERVER_IP, SERVER_PORT))

while True:
    msg = client.recv(MSG_BUFF_SIZE)
    print(msg.decode("utf-8"))