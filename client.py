import socket

# Python versão 3.8.10 (Colocar assert com mensagem de warning)

# Primeiramente temos que utilizar uma conexão do tipo TCP, devido à orientação à conexão deste tipo (SOCK_STREAM)
# Devido à ampla utilização do padrão IPV4 no Brasil, temos de instanciar a classe socket com esta configuração (AF_INET)
class Cliente():

    def __init__(self):

        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #logica para passagem de mensagem
        self.LOCALIZACAO_ERRADA = 'LE'
        self.ESPERA_VEZ= 'EV'
        self.SUA_VEZ= 'SV'
        self.FIM_DE_JOGO= 'FJ'

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

        while not fimDoJogo:
            try:
                # self.battle_map_view_view.draw4me()

                inputValido = False 

                while not inputValido:

                    coord = input("> Onde voce quer atacar? (ex A2): ").upper()

                    if not self.validate_input_format(coord):
                        print(">> Input invalido")
                        continue

                    # Envia para o servidor
                    self.client_send(coord)
                    feedback = self.receive_message()

                    if not feedback:
                        pass

                    elif(feedback == self.LOCALIZACAO_ERRADA):
                        print(">> Localizacao invalida")
                        continue

                    elif(feedback == self.ESPERA_VEZ):
                        print(">> Nao eh sua vez de jogar ainda")
                        continue

                    elif(feedback == self.SUA_VEZ):
                        inputValido = True

                        # Como chegou aqui, quer dizer que acabou de acabar a jogada
                        # do outro player. Isso implica que ALGO foi atingido, logo
                        # atualizar battle_map_my_view para ter agora o ponto novo 
                        # atingido, de forma que quando voltar no loop para cima
                        # (draw4me) temos que ter algo consistente
                        coordAtingida = self.receive_message() 
                        #self.battle_map_my_view.atualiza(coordAtingida)

                    elif(feedback == self.FIM_DE_JOGO):
                        inputValido = True 
                        fimDoJogo = True

                    else: # Cabuloso, server enviou algo válido mas que não está previsto, na duvida continua
                        continue

            # Quando chegar algo do tipo SIGKILL
            except:
                # Listar todos os tipos de excecao, via de regra, provavelmente só vai ter que
                # mandar pro servidor um aviso de CM (cliente morto), que é tratado do outro lado
                # pra matar o outro cliente tbm (às vezes nao precisa tratar isso por comunicacao)
                pass
        

    def validate_input_format(coord):
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
            coord = input("> Onde voce gostaria de posicionar o porta-avioes? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_carrier(coord):
                print(">> O porta-avioes nao se encaixa nessa posicao")
            else:
                break
        #self.battle_map_view.draw4me()
        while True:
            coord = input("> Onde voce gostaria de posicionar o destruidor? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_destroyer(coord):
                print(">> O destruidor nao se encaixa nessa posicao")
            else:
                break
        self.battle_map_view.draw4me()
        while True:
            coord = input("> Onde voce gostaria de posicionar o navio de batalha? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_battleship(coord):
                print(">> O navio de batalha nao se encaixa nessa posicao")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Onde voce gostaria de posicionar o cruzador? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_cruiser(coord):
                print(">> O cruzador nao se encaixa nessa posicao")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Onde voce gostaria de posicionar o submarino? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_submarine(coord):
                print(">> O submarino nao se encaixa nessa posicao")
            else:
                break
        # self.battle_map_view.draw4me()
        while True:
            coord = input("> Onde voce gostaria de posicionar o patrulhador? (ex A2): ").upper()
            if not self.validate_input_format(coord):
                print(">> Input invalido")
            elif not self.battle_map_view.place_submarine(coord):
                print(">> O patrulhador nao se encaixa nessa posicao")
            else:
                break