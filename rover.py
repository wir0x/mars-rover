from plateau import Plateau


class Rover(object):
    def __init__(self, _position="", _instruction=""):
        self.position = _position
        self.instruction = _instruction
        pos = self.position.split()
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.o = str(pos[2])

    def insert_position(self):
        plt1.set_position(self.x, self.y, self.o)

    def instruction_control(self):
        instr = list(self.instruction)
        spinl = {"E": "N", "O": "S", "N": "O", "S": "E"}
        spinr = {"E": "S", "O": "N", "N": "E", "S": "O"}

        for i in instr:
            if i == "L":
                self.o = spinl[self.o]
            elif i == "R":
                self.o = spinr[self.o]
            elif i == "M":
                if self.o == "E":
                    self.x += 1
                elif self.o == "O":
                    self.x -= 1
                elif self.o == "N":
                    self.y += 1
                elif self.o == "S":
                    self.y -= 1
                plt1.set_position(self.x, self.y, self.o)
                plt1.draw_grill()

    def execute(self):
        self.insert_position()
        self.instruction_control()
        print "=" * 50
        print "Output: ", self.x, self.y, self.o
        print "=" * 50


symbol = "#" * 70
print(symbol)
print "WELCOME to  Mars Rover \n"

plt1 = Plateau(6, 6)

print "You should enter the position and instruction this way:" \
      "\n[example: 1 2 N] <- position" \
      "\n[example: LMLMLMLMM] <- instruction"

print(symbol)
position = raw_input("\nposition: ")
instruction = raw_input("instruction: ")
rvr1 = Rover(position, instruction)
print(symbol)
rvr1.execute()
