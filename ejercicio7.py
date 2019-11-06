"""
	@vysery98
	Programación Funcional:
		Funciones Puras
		Efectos Secundarios
"""
import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = "\t")

with open("data/trabajadores.csv") as midata:
	# Conversion de la informacion del archivo a lista
	info = list(lineasDiccionario(midata))

	"""
	# EN VARIAS LINEAS DE CODIGO
	# Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10
	paises = lambda x: len(list(x.items())[2][1]) > 10 # Funcion para comparar aquellos con tamaño superior a 10
	registro = list(filter(paises, info)) # Compara los datos en info de la posicion [2][1] segun la funcion paises
	print(registro) # Salida
	# Ordenar la lista en función del día de nacimiento
	orden = sorted(registro, key = lambda x: list(x.items())[1][1].split("-")[2]) # Ordena en base a la lista anterior, segun el dia \
																				  # mediante .split en la posicion [2]
	print(orden) # Salida
	"""

	# EN UNA LINEA DE CODIGO
	# Registros cuyos países tengan en su nombre una longitud mayor a 10
	print(list(filter(lambda x: len(list(x.items())[2][1]) > 10, info)))

	print("\n\n") # Separador, para diferenciar ambas listas

	# Lista ordenada en función del día de nacimiento
	print(sorted(list(filter(lambda x: len(list(x.items())[2][1]) > 10, info)), key = lambda x: list(x.items())[1][1].split("-")[2]))