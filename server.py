import socket 

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT_IP = socket.gethostname()
CLIENT_PORT = 1234
QUEUE_SiZE = 2

# Da um bind
server.bind((CLIENT_IP, CLIENT_PORT))

# Inicia a 'escuta' da porta
server.listen(QUEUE_SiZE)

# Espera ocupada pelo cliente 
while True:
    clientSocket, address = server.accept()
    print(f"Conexao estabelecida com o cliente no endereco {address}! ")
    clientSocket.send(bytes("Bem vindo ao inferno corno!", "utf-8"))
