# coding=utf-8
__author__ = 'gsv'


class Plateau(object):
	""" Clase Plateau que representa al Objeto donde recorrera MarsRovers. """

	def __init__(self, fil=0, col=0):
		""" Constructor de la clase Plateau. """

		def es_numero(valor):
			""" Function que verificar que si valor es numero. """
			return isinstance(valor, (int, long, float, complex))

		if es_numero(fil) and es_numero(col):
			self.fil = fil
			self.col = col
			self.plt = [[" "] * self.fil for i in range(self.col)]
		else:
			raise TypeError("Fila y Columna deben ser números enteros")

	def insertar_posicion(self, x, y, o):
		""" Inserta en Plateau la posicion (coordenas X, Y e Orientacion) de Mars Rovers. """
		y = self.fil - (y + 1)
		self.plt[y][x] = o

	def imprimir(self):
		""" Imprime las grillas de Plateou. """
		temp = ""
		for i in range(self.fil):
			for j in range(self.col):
				temp += "[" + str(self.plt[i][j]) + "]"
			temp += "\n"
		print temp

