import numpy as np
from ship import Ship
from tilemap import TileMap


class BattleMap:
    def __init__(self):
        self.my_view = TileMap()
        self.enemy_view = TileMap()
        self.carrier = Ship(5, 2, "A0", 'C')
        self.destroyer = Ship(6, 1, "A2", 'D')
        self.battleship = Ship(5, 1, "A3", 'B')
        self.cruiser = Ship(4, 1, "A4", 'c')
        self.submarine = Ship(4, 1, "A5", 'S')
        self.patrol = Ship(3, 1, "A6", 'P')
        self.ships = [self.carrier, self.destroyer, self.battleship, self.cruiser, self.submarine, self.patrol]

    def place_carrier(self, coord):
        return self.my_view.place_ship(coord, self.carrier)

    def place_destroyer(self, coord):
        return self.my_view.place_ship(coord, self.destroyer)

    def place_battleship(self, coord):
        return self.my_view.place_ship(coord, self.battleship)

    def place_cruiser(self, coord):
        return self.my_view.place_ship(coord, self.carrier)

    def place_submarine(self, coord):
        return self.my_view.place_ship(coord, self.submarine)

    def place_patrol(self, coord):
        return self.my_view.place_ship(coord, self.patrol)

    def draw4enemy(self):
        self.enemy_view.draw()

    def draw4me(self):
        self.my_view.draw()

    # Method returns true when a valid tile was hit
    # False otherwise
    def receive_bomb(self, coord) -> bool:
        # Shoot at the same tile twice
        if self.my_view.get(coord) == 'X':
            return False

        symbol4enemy = self.my_view.get(coord)
        if symbol4enemy == ' ':
            symbol4enemy = 'X'
        self.enemy_view.set(coord, symbol4enemy)
        self.my_view.set(coord, 'X')
        for ship in self.ships:
            if ship.contains(coord):
                ship.hit()
                break
        return True

    def check_if_lost(self):
        for ship in self.ships:
            if ship.is_alive():
                return False
        return True
