"""
	@vysery98
	Programación Funcional:
		Funciones Puras
		Efectos Secundarios
"""
import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
	# Toma unicamente los emails, excluyendo 'email'
	"""
	EN VARIAS LINEAS DE CODIGO
	lista = list(lineas(midata))
	filtro = filter(lambda x:x[1] != "email", lista)
	mapa = map(lambda x: x[1], filtro)

	print(list(mapa))
	"""
	# En una linea de codigo
	print(list(map(lambda x: x[1], filter(lambda x:x[1] != "email", list(lineas(midata))))))