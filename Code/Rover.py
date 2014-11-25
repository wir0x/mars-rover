__author__ = 'gsv'

from Plateau import Plateau


class Rover(object):
    """ Clase Marse Rover, representa al Robot."""

    def __init__(self, posicion="", instruccion=""):
        """ Constructor de la Clase Rover. """
        self.posicion = posicion
        self.instruccion = instruccion
        pos = self.posicion.split()
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.o = str(pos[2])

    def insertar_posicion(self):
        """ Funcion que insertar a Rovers en el Plateau. """
        plt1.insertar_posicion(self.x, self.y, self.o)

    def control_instruccion(self):
        """ Funcion que controla las instrucciones dadas a Rover """
        instr = list(self.instruccion)
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
                plt1.insertar_posicion(self.x, self.y, self.o)
                plt1.imprimir()

    def ejecutar(self):
        self.insertar_posicion()
        self.control_instruccion()
        print "=" * 50
        print "Output: ", self.x, self.y, self.o
        print "=" * 50

###################################################################
simbolo = "*" * 50

print(simbolo)
print "\nBienvenido a Mars Rover\n"
print(simbolo)

# NOTA!!!
# Descomenta las siguientes seis lineas y comentar la septima si quieres que el usaurio ingrese Fila y Columna
# print "El Plateau debe dividirse en grillas (Filas, Columnas)\n" \
#       "Por favor ingrese el numero 'Filas' y 'Columnas'\n"
# print(simbolo)
# fil = input("Fila: ")
# col = input("Columna: ")
# plt1 = Plateau(fil, col)
plt1 = Plateau(6, 6)


print "\nDebes ingresar la 'Posicion' (Ej: 1 2 N) y la 'Instruccion' (Ej: LMLMLMLMM) para Rovers\n" \
      "Por favor ingrese la posicion y la instruccion como en los ejemplos: \n"

print(simbolo)
posi = raw_input("Posicion: ")
inst = raw_input("Instruccion: ")
rvr1 = Rover(posi, inst)
print(simbolo)
rvr1.ejecutar()
