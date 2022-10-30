from battle_map import BattleMap
from tilemap import TileMap
from ship import Ship
from server import Server


class Player:
    def __init__(self, server):
        server.registerPlayer()
        self.battle_map = BattleMap()

    def perdeu(self):
        return self.battle_map.check_if_lost()

