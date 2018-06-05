# main
#
# DESCRIPCION: Programa que determina la primalidad de un entero n>1 dado. \
# Para ello se puede hacer la verificacion a traves de alguno de los siguientes \
# 3 algoritmos: División por Tentativa, Aleatorizado basico y Solovay-Strassen.
#
# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.
#
# Ultima modificacion: 14/06/2018.

import sys
from maintentativedivision import tentativedivision
from mainbasicrandom import basicrandom
from mainSolovay_Strassen import  Solovay_Strassen

# Se le da la bienvenida al usuario

print "Bienvenido al Test De Primalidad"
print ""
print "Este posee 3 algoritmos para escoger: "
print "0. División por Tentativa."
print "1. Aleatorizado basico"
print "2. Solovay-Strassen"
print "3. Salir"
print ""

# El usuario selecciona el algoritmo para realizar el test de primalidad
while True:

	try:
		# Select a modality
		eleccion_algoritmo = input("Por favor, ingrese el numero correspondiente al modo que desea ejecutar: ")
		assert(0 <= eleccion_algoritmo <= 3)
		break
	except:
		print "Por favor, introduzca una modalidad valida."

if eleccion_algoritmo == 3:
	print "Hasta Luego"
	sys.exit()

# El ingresa el numero para realizar el test
while True:

	try:
		# Select a modality
		numero = input("Por favor, ingrese el numero que desea saber si es primo: ")
		assert(2 <= numero)
		break
	except:
		print "Por favor, introduzca un entero mayor estricto que 1."

# Dependiendo de sus elecciones llamamos al algoritmo correspondiente
if eleccion_algoritmo == 0:

	if tentativedivision(numero):
		print n,"Es primo"
	else:
		print n,"Es compuesto"

elif eleccion_algoritmo == 1:

	if basicrandom(numero):
		print n,"Es primo"
	else:
		print n,"Es compuesto"

elif eleccion_algoritmo ==2:
	if Solovay_Strassen(numero):
		print n,"Es primo"
	else:
		print n,"Es compuesto"

else:
	print "El programa terminara"