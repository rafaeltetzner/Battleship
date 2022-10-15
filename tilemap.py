import numpy as np


class TileMap:
    def __init__(self):
        self.tile_map = np.empty([100], dtype=str)
        self.tile_map[:] = " "

        self.tile_view = """
   0   1   2   3   4   5   6   7   8   9
 +---+---+---+---+---+---+---+---+---+---+
A| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |
 +---+---+---+---+---+---+---+---+---+---+
B| {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} | {18} | {19} |
 +---+---+---+---+---+---+---+---+---+---+
C| {20} | {21} | {22} | {23} | {24} | {25} | {26} | {27} | {28} | {29} |
 +---+---+---+---+---+---+---+---+---+---+
D| {30} | {31} | {32} | {33} | {34} | {35} | {36} | {37} | {38} | {39} |
 +---+---+---+---+---+---+---+---+---+---+
E| {40} | {41} | {42} | {43} | {44} | {45} | {46} | {47} | {48} | {49} |
 +---+---+---+---+---+---+---+---+---+---+
F| {50} | {51} | {52} | {53} | {54} | {55} | {56} | {57} | {58} | {59} |
 +---+---+---+---+---+---+---+---+---+---+
G| {60} | {61} | {62} | {63} | {64} | {65} | {66} | {67} | {68} | {69} |
 +---+---+---+---+---+---+---+---+---+---+
H| {70} | {71} | {72} | {73} | {74} | {75} | {76} | {77} | {78} | {79} |
 +---+---+---+---+---+---+---+---+---+---+
I| {80} | {81} | {82} | {83} | {84} | {85} | {86} | {87} | {88} | {89} |
 +---+---+---+---+---+---+---+---+---+---+
J| {90} | {91} | {92} | {93} | {94} | {95} | {96} | {97} | {98} | {99} |
 +---+---+---+---+---+---+---+---+---+---+
        """

    def set(self, coord, char):
        self.tile_map[self._coord2idx(coord)] = char

    def get(self, coord):
        return self.tile_map[self._coord2idx(coord)]

    def draw(self):
        print(self.tile_view.format(*self.tile_map))

    def place_ship(self, coord, ship):
        if not ship.fits_at(coord):
            return False
        # Check if there is already a ship at coord
        idx = self._coord2idx(coord)
        for i in range(0, ship.length):
            for j in range(0, ship.width):
                if self.tile_map[idx + j + i * 10] != ' ':
                    return False

        # Place the ship
        for i in range(0, ship.length):
            for j in range(0, ship.width):
                self.tile_map[idx + j + i * 10] = ship.symbol
        ship.coord = coord
        return True

    @staticmethod
    def _coord2idx(coord):
        j = ord(coord[1]) - ord('0')
        i = (ord(coord[0]) - ord('A'))
        return i * 10 + j
