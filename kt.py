# principal.py
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
from manual import manualPrincipal
from FuerzaBruta import FuerzaBrutaPrincipal
from Divide_Conquer import Divide_ConquerPrincipal

# Se le da la bienvenida al usuario

print "Bienvenido al Test De Primalidad"
print ""
print "Este posee 3 algoritmos para escoger: "
print "0. División por Tentativa."
print "1. Aleatorizado basico"
print "2. Solovay-Strassen"
print "3. Salir"
print ""

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
	
while True:
	try:
		Tam = input("Por favor ingrese el orden del tablero: ")
		assert(Tam >= 3)
		break
	except:
		print "Por favor ingrese un numero valido (N debe ser mayor o igual que 3)"

tabl=[Tam*[0] for i in range(Tam)]

if eleccion_algoritmo == 0:
	i=int(input("Introduzca en cual fila iniciar, empezando en 0: "))
	j=int(input("Introduzca en cual columna iniciar, empezando en 0: "))
	tabl[i][j]=1
	resultado=manualPrincipal(Tam,i,j,tabl,1,[i],[j])
	if resultado==1:
		print "Felididades has completado el Knight\'s Tour"
	elif resultado==0:
		print "Ejecute nuevamente para probar otra modalidad"
elif eleccion_algoritmo == 1:
	i=0
	j=0
	tabl[i][j]=1
	resultado=FuerzaBrutaPrincipal(Tam,i,j,tabl,1,[i],[j])
	if resultado==1:
		print "Se ha completado el Knight\'s Tour"
	elif resultado==0:
		print "No se ha completado el Knight\'s Tour"
		print "Ejecute nuevamente para probar otra modalidad"
elif eleccion_algoritmo ==2:
	# Primero Buscamos que tipo de tablero nos piden resolver
	if Tam>=8 or Tam==6:
		# Chequeamos si es del tipo potencia de 2
		i = 2
		while True:
			i *= 2
			if i == Tam:
				R=Divide_ConquerPrincipal(Tam,2)
			if i > Tam:
			    break
		# Chequeamos si es 6 o multiplo de 12
		if Tam%12==0 or Tam==6:
			R=Divide_ConquerPrincipal(Tam,12)
		
		A = [['o' for i in range(Tam)] for j in range(Tam)]
		for i  in range(len(R)):
			A[R[i][0]][R[i][1]] = i
		for i in range(len(A)):
			print A[i]
	else:
		print "Lo lamento no puedo resolver ese tipo de tableros"
		print "Ejecute nuevamente para probar otra modalidad"

else:
	print "El programa terminara"