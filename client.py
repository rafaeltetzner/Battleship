import socket
import select

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)
class Cliente():

    def __init__(self):

        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    def client_send(self):
        self.client.send(mensagem.encode('utf-8'))

    def run(self):
        
        # No comeco mesmo tem que saber onde instanciar as naves
        # Temos uma lógica parecida para esta parte, mas é bom colocar dentro de battle_map_view a
        # estrutura de IO 
        self.init_ship()

        fimDoJogo = False

        while not fimDoJogo:
            try:
                # self.battle_map_view_view.draw4me()

                inputValido = False 

                while not inputValido:

                    coord = input("> Onde voce quer atacar? (ex A2): ").upper()

                    if not self.validade_input_format_format(coord):
                        print(">> Input invalido")
                        continue
                    # Envia para o servidor
                    self.client_send()
                    # Se servidor devolver um LE --> Printa localizacao errada, continue
                    # Se servidor devolver um EV --> Espere sua vez, continue
                    # Se servidor devolver um SV --> Sua vez, inputValido = True
                    # Se servidor devolver um FJ --> Fim do jogo, inputValido = True, fimDoJogo = True

            # Quando chegar algo do tipo SIGKILL
            except:
                # Listar todos os tipos de excecao, via de regra, provavelmente só vai ter que
                # mandar pro servidor um aviso de CM (cliente morto), que é tratado do outro lado
                # pra matar o outro cliente tbm (às vezes nao precisa tratar isso por comunicacao)
                pass
        

    def validade_input_format_format(coord):
        if len(coord) > 2:
            return False
        if coord[0] < 'A' or coord[0] > 'J':
            return False
        if coord[1] < '0' or coord[1] > '9':
            return False
        return True

    def init_ship(self):
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the carrier? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_carrier(coord):
                print(">> The carrier doesn't fit at this coordinates")
            else:
                break
        #self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the destroyer? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_destroyer(coord):
                print(">> The destroyer doesn't fit at this coordinates")
            else:
                break
        self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the battleship? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_battleship(coord):
                print(">> The battleship doesn't fit at this coordinates")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the cruiser? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_cruiser(coord):
                print(">> The cruiser doesn't fit at this coordinates")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the submarine? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_submarine(coord):
                print(">> The submarine doesn't fit at this coordinates")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Where would you like to place the patrol? (ex A2): ").upper()
            if not self.validade_input_format(coord):
                print(">> Invalid input")
            elif not self.battle_map_view.place_submarine(coord):
                print(">> The patrol doesn't fit at this coordinates")
            else:
                break