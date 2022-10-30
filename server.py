import socket 
import select

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)

class Server:

    def __init__(self):

        self.PORT= 1234 
        self.CLIENT_IP = socket.gethostname()
        
        self.QUEUE_SIZE = 2
        self.MESSAGE_LENGHT =  2 #dois caracters definem a coordenada do espaço no mapa

        self.POSICAO_INVALIDA = 'PI'

        self.LOCALIZACAO_ERRADA = 'LE'
        self.SUA_VEZ= 'SV'
        self.FIM_DE_JOGO= 'FJ'

        self.VENCEDOR = 'VV'
        self.PERDEDOR = 'PP'
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.num_registered_players = 0
        self.clientSockets = {1: '', 2: ''}
        self.clientSockets_lists = []


    def jogada(self, player1, player2, turn):

        inputValido = False

        while not inputValido:

            # Le das sockets disponiveis
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

                    # Checar se a posicao que eu quero atingir eh valida, nao eh repedita
                    if not inimigo.battle_map.is_hit(coord):
                        self.clientSockets[turn].send(self.LOCALIZACAO_ERRADA.encode('utf-8'))
                    else:
                        inputValido = True
                        
                        simbolo_revelado = inimigo.battle_map.bomb(coord)

                        # Manda para o atual o que ele atingiu
                        self.clientSockets[turn].send(simbolo_revelado.encode('utf-8'))

                        # Passa o turno
                        self.clientSockets[1 if turn == 2 else 2].send(self.SUA_VEZ.encode('utf-8'))
                        
                        # Manda para o inimigo que ele foi atingido em posicao tal
                        self.clientSockets[1 if turn == 2 else 2].send(coord.encode('utf-8'))

    def registerPlayer(self):
        self.server_socket.bind((self.CLIENT_IP, self.PORT))
        self.server_socket.listen(self.QUEUE_SIZE)

        read_socket, _, _ = select.select([self.server_socket],[],[])

        client_socket, client_address = self.server_socket.accept()

        self.num_registered_players += 1
        self.clientSockets[self.num_registered_players] = client_socket
        self.clientSockets_lists.append(client_socket)
        
        vez = self.SUA_VEZ if self.num_registered_players == 1 else self.ESPERA_VEZ 
        client_socket.send(vez.encode('utf-8'))

    def posiciona_ships(self, player, turn):
        posicao = self.receive_message(turn)
        if not player.battle_map.place_carrier(posicao):
            self.clientSockets[turn].send(self.POSICAO_INVALIDA.endode('utf-8'))

    def receive_message(self, turn):

        try:
            mensagem = self.clientSockets[turn].recv(self.MESSAGE_LENGTH)

            if not len(mensagem):
                return False

            return mensagem.decode('utf-8')

        except:
            return False

    def informaResultados(self, vencedor):
        
        # Informa para ambos o fim do jogo
        self.clientSockets[1].send(self.FIM_DE_JOGO.encode('utf-8'))
        self.clientSockets[2].send(self.FIM_DE_JOGO.encode('utf-8'))

        # Divulga resultado
        self.clientSockets[vencedor].send(self.VENCEDOR.encode('utf-8'))
        self.clientSockets[1 if vencedor == 2 else 2].send(self.PERDEDOR.encode('utf-8'))