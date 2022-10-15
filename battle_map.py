import numpy as np


class BattleMap:
    def __init__(self):
        self.tile_map_data = np.chararray([100], unicode=True)
        self.tile_map_data[:] = ' '
        print(self.tile_map_data)
        self.tile_map = """
           1   2   3   4   5   6   7   8   9   10
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

    def draw(self):
        print(self.tile_map.format(*self.tile_map_data))

    