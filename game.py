from player import Player
from server import Server

# A parte de redes será estruturada da seguinte forma:

'''
(Na mesma máquina) :

1 thread servidor (principal do programa) que é responsável pela lógica e manutenção de estados
compartilhados, junto de guardar as informações de inicialização e configuração das portas
'''

class Game:
    def __init__(self):
        self.server = Server()
        self.p1 = Player(self.server, 1)
        self.p2 = Player(self.server, 2)
        self.turn = 1

    def run(self):
        self.p1.init_ships()
        self.p2.init_ships()

        while True:
            
            self.server.jogada(self.p1, self.p2, self.turn)
            self.turn = 2

            # self.p1.on_turn(self.p2)
            # self.p2.on_turn(self.p1)

            self.server.jogada(self.p1, self.p2, self.turn)
            self.turn = 1

            if self.p1.have_lost() or self.p2.have_lost():
                break

        if self.p1.have_lost():
            print("+---+---+---+PLAYER2 HAS WON+---+---+---+")
            # server.informaResultados(vencedor = 2)
        else:
            print("+---+---+---+PLAYER1 HAS WON+---+---+---+")
        



