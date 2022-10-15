from battle_map import BattleMap


class Player:
    def __int__(self, name):
        self.battle_map = BattleMap()
        self.name = name

    def shoot(self, enemy_battle_map):
        raise NotImplementedError("Calling abstract method 'shoot' from Player")


class PlayerComputer(Player):
    def shoot(self):
        print("Where would you like to shoot? (x,y)")
        print("x")