class Ship:
    def __init__(self, length, width, coord, symbol, name):
        self.length = length
        self.width = width
        self.coord = coord
        self.symbol = symbol
        self.num_hits = 0
        self.name = name

    def fits_at(self, coord):
        if chr(self.length + ord(coord[0]) - 1) > 'J':
            return False
        if chr(self .width + ord(coord[1]) - 1) > '9':
            return False
        return True

    def contains(self, coord) -> bool:
        if coord[0] < self.coord[0] or coord[0] > chr(ord(self.coord[0]) + self.length):
            return False
        if coord[1] < self.coord[1] or coord[1] > chr(ord(self.coord[1]) + self.length):
            return False
        return True

    def hit(self):
        self.num_hits += 1

    def is_alive(self):
        return self.num_hits < self.length * self.width