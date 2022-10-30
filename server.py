import socket 
import select

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)



class Server:
    def __init__(self):
        self.PORT= 1234 
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.CLIENT_IP = socket.gethostname()
        self.QUEUE_SIZE = 1
        self.num_registered_players = 0
        self.clientSockets = {1: '', 2: ''}

        self.MESSAGE_LENGHT =  2 #dois caracters definem a coordenada do espaço no mapa

    def registerPlayer(self):
        self.server_socket.bind((self.CLIENT_IP, self.PORT))
        self.server_socket.listen(self.QUEUE_SIZE)

        read_socket, _, _ = select.select([self.server_socket],[],[])
        client_socket, client_address = self.server_socket.accept()
        self.num_registered_players += 1
        self.clientSockets[self.num_registered_players] = client_socket
    
    def receive_message(self, turn):

        try:
            mensagem = self.clientSockets[turn].recv(self.MESSAGE_LENGTH)

            if not len(mensagem):
                return False

            return mensagem.decode('utf-8')

        except:
            return False


    def jogada(self, player1, player2, turn):

        # Recebe as mensagens 
        coord = self.receive_message(turn)

        if(turn == 1):
            player1.on_turn(player2, coord)
        else:
            player2.on_turn(player1, coord)

        # Manda para o outro player
        self.server_socket.send(self.clientSockets[1 if turn == 2 else 2].encode('utf-8'))


