from battle_map import BattleMap
from ship import Ship


class Player:
    def __init__(self, server, num):
        server.registerPlayer(num)
        self.num = num
        self.battle_map = BattleMap()

    def init_ships(self):
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the carrier? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_carrier(coord):
                print(">> The carrier doesn't fit at this coordinates")
            else:
                break
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the destroyer? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_destroyer(coord):
                print(">> The destroyer doesn't fit at this coordinates")
            else:
                break
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the battleship? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_battleship(coord):
                print(">> The battleship doesn't fit at this coordinates")
            else:
                break
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the cruiser? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_cruiser(coord):
                print(">> The cruiser doesn't fit at this coordinates")
            else:
                break
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the submarine? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_submarine(coord):
                print(">> The submarine doesn't fit at this coordinates")
            else:
                break
        self.battle_map.draw4me()
        while True:
            coord = input("> Where would you like to place the patrol? (ex A2): ").upper()
            if not self._validate_input(coord):
                print(">> Invalid input")
            elif not self.battle_map.place_submarine(coord):
                print(">> The patrol doesn't fit at this coordinates")
            else:
                break

    def on_turn(self, enemy, coord):
        self.battle_map.draw4me()
        coord = input("> Where would you like to attack? (ex A2): ").upper()

        while True:
            if not self._validate_input(coord):
                print(">> Invalid input")
       
            else:
                break
        
        return coord

    def have_lost(self):
        return self.battle_map.check_if_lost()

    # @staticmethod
    def _validate_input(coord):
        if len(coord) > 2:
            return False
        if coord[0] < 'A' or coord[0] > 'J':
            return False
        if coord[1] < '0' or coord[1] > '9':
            return False
        return True
