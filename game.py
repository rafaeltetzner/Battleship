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
        # Inicializa o servidor e os jogadores, que sao registrados no servidor 
        self.server = Server()
        self.p1 = Player(self.server)
        self.p2 = Player(self.server)
        self.turn = 1

    def run(self):
        # Implementar no cliente

        self.server.posiciona_ships(self.p1, 1)
        self.server.posiciona_ships(self.p2, 2)

        while True:
            
            self.server.jogada(self.p1, self.p2, self.turn)
            self.turn = 2

            self.server.jogada(self.p1, self.p2, self.turn)
            self.turn = 1

            if self.p1.perdeu() or self.p2.perdeu():
                break
        
        vencedor = 2 if self.p1.perdeu() else 1
        self.server.informaResultados(vencedor)