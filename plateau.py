class Plateau(object):
    """ This class represent to Obj Plateau. """

    def __init__(self, fil=0, col=0):

        def is_number(valor):
            return isinstance(valor, (int, long, float, complex))

        if is_number(fil) and is_number(col):
            self.fil = fil
            self.col = col
            self.plt = [[" "] * self.fil for i in range(self.col)]
        else:
            raise TypeError("row and column not are numbers")

    def set_position(self, x, y, o):
        y = self.fil - (y + 1)
        self.plt[y][x] = o

    def draw_grill(self):
        temp = ""
        for i in range(self.fil):
            for j in range(self.col):
                temp += "[" + str(self.plt[i][j]) + "]"
            temp += "\n"
        print(temp)

