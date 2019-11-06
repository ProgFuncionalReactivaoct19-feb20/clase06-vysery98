"""
	@vysery98
	Programación Funcional:
		Funciones Puras
		Efectos Secundarios
"""
import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
	
	"""
	# EN VARIAS LINEAS DE CODIGO
	# Conversion de la informacion del archivo a lista
	lista = list(lineasDiccionario(midata))

	# Separadores:
	#	Toma unicamente los nombres
	mapa1 = list(map(lambda x: list(x.items())[0][1], lista))
	#	Toma lo que se encuentre despues del espacio en blanco ' '
	separador1 = lambda x: x.split(" ")[1]

	#	Toma unicamente los correos
	mapa2 = list(map(lambda x: list(x.items())[1][1], lista))
	#	Toma lo que se encuentre previo al separador '.'
	separador2 = lambda x: x.split(".")[0]

	# Conversiones a Listas
	lista1 = list(map(separador1, mapa1))
	lista2 = list(map(separador2, mapa2))

	# Concatenacion de Listas
	salida = list(zip(lista1, lista2))
	f = lambda x: x[0] + " - " + x[1]

	print(list(map(f, salida)))
	"""

	# En una linea de codigo
	
	lista = list(lineasDiccionario(midata))
	print(list(map(lambda x: x[0] + "%s" % " - " + x[1], list(zip(list(map(lambda x: x.split(" ")[1], \
		list(map(lambda x: list(x.items())[0][1], lista)))), list(map(lambda x: x.split(".")[0], \
		list(map(lambda x: list(x.items())[1][1], lista)))))))))