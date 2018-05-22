
# principal.py
#
# DESCRIPCION: Programa que permite a un usuario resolver el problema del recorrido \
# del caballo, a traves de 3 modalidades: Manual: donde es el usuario, quien intenta \
# resolver el acertijo, "Fuerza Bruta" y "Divide y conquistaras": donde un algoritmo \
# de backtracking o basandose en las soluciones de Penberry, busca la solucion o determina \
# el tablero como irresoluble.
#
# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.
#
# Ultima modificacion: 24/05/2018.


import random
import sys
from manual import manualPrincipal
#from FuerzaBruta import FuerzaBrutaPrincipal

# Se le da la bienvenida al usuario

print 'Bienvenido al Knight\'s Tour'
print ''
print 'Este posee 3 modalidades: '
print '0. Manual: Usted escoge el camino que desee.'
print '1. Fuerza Bruta: se evaluan recorridos de manera aleatoria'
print '2. Divide y Conquistaras'
print '3. Salir'
print ''

while True:
	try:
		# Select a modality
		eleccion_algoritmo = input('Por favor, ingrese el numero correspondiente al modo que desea ejecutar: ')
		assert(0 <= eleccion_algoritmo <= 3)
		break
	except:
		print 'Por favor, introduzca una modalidad valida.'

if eleccion_algoritmo == 3:
	print "Hasta Luego"
	sys.exit()
	
while True:
	try:
		Tam = input('Por favor ingrese el orden del tablero: ')
		assert(Tam >= 3)
		break
	except:
		print 'Por favor ingrese un numero valido (N debe ser mayor o igual que 3)'

tabl=[Tam*[0] for i in range(Tam)]

if eleccion_algoritmo == 0:
	i=int(input("Introduzca en cual fila iniciar, empezando en 0: "))
	j=int(input("Introduzca en cual columna iniciar, empezando en 0: "))
	tabl[i][j]=1
	if manualPrincipal(Tam,i,j,tabl,1,[i],[j])==1:
		print "Felididades has completado el Knight\'s Tour"
elif eleccion_algoritmo == 1:
	FuerzaBrutaPrincipal(Tam,tabl)
elif eleccion_algoritmo ==2:
	print "Divide y Conquistaras"
else:
	print 'El programa terminara'