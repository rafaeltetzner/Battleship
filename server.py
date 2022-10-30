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

        self.LOCALIZACAO_ERRADA = 'LE'
        self.ESPERA_VEZ= 'EV'
        self.SUA_VEZ= 'SV'
        self.FIM_DE_JOGO= 'FJ'

        self.CLIENT_IP = socket.gethostname()
        self.QUEUE_SIZE = 2
        self.num_registered_players = 0
        self.clientSockets = {1: '', 2: ''}
        self.clientSockets_lists = []

        self.MESSAGE_LENGHT =  2 #dois caracters definem a coordenada do espaço no mapa

    def registerPlayer(self):
        self.server_socket.bind((self.CLIENT_IP, self.PORT))
        self.server_socket.listen(self.QUEUE_SIZE)

        read_socket, _, _ = select.select([self.server_socket],[],[])
        client_socket, client_address = self.server_socket.accept()
        self.num_registered_players += 1
        self.clientSockets[self.num_registered_players] = client_socket
        self.clientSockets_lists.append(client_socket)

    def receive_message(self, turn):

        try:
            mensagem = self.clientSockets[turn].recv(self.MESSAGE_LENGTH)

            if not len(mensagem):
                return False

            return mensagem.decode('utf-8')

        except:
            return False


    def jogada(self, player1, player2, turn):

        inputValido = False 

        while not inputValido:

            # Le das sockets disponíveis
            read_sockets, _, exception_sockets = select.select(self.clientSockets_lists, [], self.clientSockets_lists)

            # Itera pelos sockets notificados
            for notified_socket in read_sockets:

                # Verifica se a socket notificada vem do cliente correto
                if(notified_socket == self.clientSockets[turn]):
                    # Recebe as mensagens 
                    coord = self.receive_message(turn)

                    # Para chegar neste caso, tem-se que chegou uma mensagem vazia, termina programa
                    if coord is False:
                        # Avisa (?) os clientes que moio
                        pass
                        
                    atual = player1 if turn == 1 else player2 
                    inimigo = player1 if turn == 2 else player2 

                    # Como é a vez deste cliente devemos checar no battlemap se a posicao de ataque ja foi marcada
                    if not inimigo.battle_map.receive_bomb(coord):
                        self.clientSockets[turn].send(self.LOCALIZACAO_ERRADA.encode('utf-8'))

                    else: # Input realmente válido  
                        atual.on_turn(inimigo, coord)
                        inputValido = True 
                        self.clientSockets[1 if turn == 2 else 2].send(self.SUA_VEZ.encode('utf-8'))
                        self.clientSockets[turn].send(coord.encode('utf-8'))

                # Player errado mandou solicitacao, avisar ele e voltar para o comeco
                else:
                    self.clientSockets[1 if turn == 2 else 2].send(self.ESPERA_VEZ.encode('utf-8'))


        # Manda para o outro player
        # self.server_socket.send(self.clientSockets[1 if turn == 2 else 2].encode('utf-8'))


