from battle_map import BattleMap
from ship import Ship

if __name__ == '__main__':
    b = BattleMap()
    b.place_patrol('A0')
    b.place_carrier('B1')
    b.receive_bomb("C1")
    b.receive_bomb("J9")
    b.draw4me()
    print("")
    b.draw4enemy()


