import socket
from battle_map import BattleMap
import sys

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)
class Cliente():

    def __init__(self):

        self.battle_map_my_view = BattleMap()
        self.battle_map_enemy_view = BattleMap()
        self.nomes_navios = ['porta avios', 'destruidor', 'navio de batalha', 'crusador', 'submarino', 'patrulhador']

        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.vezInicial = self.receive_message()

        self.POSICAO_VALIDA = 'PV'
        self.POSICAO_INVALIDA = 'PI'

        self.LOCALIZACAO_ERRADA = 'LE'
        self.ESPERA_VEZ = 'EV'
        self.SUA_VEZ = 'SV'
        self.FIM_DE_JOGO = 'FJ'

        self.VENCEDOR = 'VV'
        self.PERDEDOR= 'PP'

        self.AGUA = 'XX'

        self.SERVER_IP = socket.gethostname()
        self.SERVER_PORT = 1234 
        self.MSG_SIZE = 2 # Tamanho mínimo de mensagem pelo protocolo TCP = 20

        self.cliente.connect((self.SERVER_IP, self.SERVER_PORT))

    def receive_message(self):

        try:
            mensagem = self.cliente.recv(self.MSG_SIZE)

            if not len(mensagem):
                return False

            return mensagem.decode('utf-8')

        except:
            return False                                         

    def client_send(self, mensagem):
        # Ver se tem a chance da socket estar fechada ? Se estiver, matar cliente
        self.cliente.send(mensagem.encode('utf-8'))
        
    def run(self):
        
        # No comeco mesmo tem que saber onde instanciar as naves
        # Temos uma lógica parecida para esta parte, mas é bom colocar dentro de battle_map_view a
        # estrutura de IO 
        self.init_ship()

        fimDoJogo = False
        minhaVez = True if self.vezInicial == self.SUA_VEZ else False 

        while not fimDoJogo:

            try:
                # self.battle_map_view_view.draw4me()
                if minhaVez:
                    coord = input("> Onde voce quer atacar? (ex A2): ").upper()

                    if not self.validate_input_format(coord):
                        print(">> Input invalido")
                        continue

                    self.client_send(coord)
                    feedback = self.receive_message()

                    if not feedback:
                        pass

                    elif(feedback == self.LOCALIZACAO_ERRADA):
                        print(">> Localizacao invalida")
                        continue

                    elif(feedback == self.FIM_DE_JOGO):
                        fimDoJogo = True

                    else:
                        # Chegou aqui minha jogada foi valida
                        self.battle_map_view.enemy_view.set(coord, feedback[0])
                        minhaVez = False
                else:
                    _ = self.receive_message()
                    hit_coord = self.receive_message()
                    self.battle_map_view.my_view.set(hit_coord, 'X')
                    minhaVez = True

            except: #SIGKILL
                pass
                    
        # Fim do jogo
        resultadoJogo = self.receive_message()
        mensagemFinal = "+---+---+---+Parabens, voce ganhou+---+---+---+" if resultadoJogo == self.VENCEDOR else "+---+---+---+Infelizmente, voce perdeu+---+---+---+"
        print(mensagemFinal)
        sys.exit() #acabou o jogo

    def validate_input_format(coord):
        if len(coord) > 2:
            return False
        if coord[0] < 'A' or coord[0] > 'J':
            return False
        if coord[1] < '0' or coord[1] > '9':
            return False
        return True


    #passa as coordenadas dos navios para o servidor de modo a posiciona-los
    def init_ship(self):
        for ship in self.battle_map_my_view.ships:
            self.battle_map_my_view.draw4me()
            while True:
                coord = input("> Onde voce gostaria de posicionar o {}? (ex A2): ").format(ship.name).upper()
                if not self.validate_input_format(coord):
                    print(">> Input invalido")
                    continue
                self.cliente.send(coord.encode('utf-8'))
                feedback = self.receive_message()
                if(feedback == self.POSICAO_INVALIDA):
                    print(">> O {} nao se encaixa nessa posicao").format(ship.name)
                    continue
                else:
                    self.battle_map_my_view.place_ship(coord, ship)
                    break

# inputValido = False 

#                     while not inputValido:

#                         coord = input("> Onde voce quer atacar? (ex A2): ").upper()

#                         if not self.validate_input_format(coord):
#                             print(">> Input invalido")
#                             continue

#                         # Envia para o servidor
#                         self.client_send(coord)
#                         feedback = self.receive_message()

#                         if not feedback:
#                             pass

#                         elif(feedback == self.LOCALIZACAO_ERRADA):
#                             print(">> Localizacao invalida")
#                             continue

#                         elif(feedback == self.ESPERA_VEZ):
#                             print(">> Nao eh sua vez de jogar ainda")
#                             continue

#                         elif(feedback == self.SUA_VEZ):
#                             inputValido = True

#                             # Como chegou aqui, quer dizer que acabou de acabar a jogada
#                             # do outro player. Isso implica que ALGO foi atingido, logo
#                             # atualizar battle_map_my_view para ter agora o ponto novo 
#                             # atingido, de forma que quando voltar no loop para cima
#                             # (draw4me) temos que ter algo consistente
#                             coordAtingida = self.receive_message() 
#                             self.battle_map.my_view(coordAtingida)

#                         elif(feedback == self.FIM_DE_JOGO):
#                             inputValido = True 
#                             fimDoJogo = True

#                         else: # Atingiu algo, marcar no mapa 
#                             inputValido = True
#                             self.battle_map.enemy_view(coord, feedback)
                            
#                             # Depois de acabar de atacar, fica bloqueado esperando sua vez, liberada pelo server
#                             feedback = self.receive_message()

#                 # Quando chegar algo do tipo SIGKILL
#                 except:
#                     # Listar todos os tipos de excecao, via de regra, provavelmente só vai ter que
#                     # mandar pro servidor um aviso de CM (cliente morto), que é tratado do outro lado
#                     # pra matar o outro cliente tbm (às vezes nao precisa tratar isso por comunicacao)
#                     pass