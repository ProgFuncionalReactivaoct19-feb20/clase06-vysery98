"""
	@vysery98
	Programación Funcional:
		Funciones Puras
		Efectos Secundarios
"""
import csv

#	def lineas(archivo):
#		return csv.reader(archivo, delimiter = ";")

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
	# Toma unicamente los nombres x.items() posicion [0][1] de los diccionarios
	"""
	EN VARIAS LINEAS DE CODIGO
	lista = list(lineasDiccionario(midata))
	mapa = map(lambda x: list(x.items())[0][1], lista)

	print(list(mapa))
	"""
	# En una linea de codigo
	print(list(map(lambda x: list(x.items())[0][1], list(lineasDiccionario(midata)))))