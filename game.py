from player import Player

# A parte de redes será estruturada da seguinte forma:

'''
(Na mesma máquina) :

1 thread servidor (principal do programa) que é responsável pela lógica e manutenção de estados
compartilhados, junto de guardar as informações de inicialização e configuração das portas
'''

class Game:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.turn = 0

    def run(self):
        print("+---+---+---+---+PLAYER1+---+---+---+---+")
        self.p1.init_ships()
        print("+---+---+---+---+PLAYER2+---+---+---+---+")
        self.p2.init_ships()

        while True:
            print("+---+---+---+---+PLAYER1+---+---+---+---+")
            self.p1.on_turn(self.p2)
            print("+---+---+---+---+PLAYER2+---+---+---+---+")
            self.p2.on_turn(self.p1)
            if self.p1.have_lost() or self.p2.have_lost():
                break

        if self.p1.have_lost():
            print("+---+---+---+PLAYER2 HAS WON+---+---+---+")
        else:
            print("+---+---+---+PLAYER1 HAS WON+---+---+---+")



