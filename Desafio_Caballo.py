# Proyecto01.py
#
# DESCRIPCION: Programa que permite a un usuario resolver el problema del recorrido \
# del caballo, a traves de 3 modalidades: Manual: donde es el usuario, quien intenta \
# resolver el acertijo, "Fuerza Bruta" y "Divide y conquistarás": donde un algoritmo \
# de backtracking o basandose en las soluciones de Penberry, busca la solucion o determina \
# el tablero como irresoluble.
#
# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.
#
# Ultima modificacion: 17/05/2018.

"""
   CONSTANTES Logicas	#informacion proporcionada por el usuriario que el programa no modifica:		
		nombreusuario : str		# nombre del usuario que esta jugando la partida
		nivel : int  			# la dificultad escogida nivel1=Facil y nivel2=Medio, si desea salir
		partida : int	  		# si se escoge 0 se inicia una partida, 1 se carga una, 2 se cierra el juego.
		seguir : bool  			# si se desea o no rendirse en la partida actual.
		guardar : bool			# si se desea o no guardar el estado actual de la partida en curso.
  
   VARIABLES Logicas
		tabl : list				# el tablero logico del juego
		tabv : list				# tablero de victorias globales del juego
		jugando : bool  		# controla si se esta en partida o en el menu
		turno : int  			# contador de los turnos de la partida
		juegauser : int			# a quien le toca jugar(True para user, False para IA)
		ganador : int  			# el primero en cumplir las condiciones victoria
		dentro : bool  			# controla si esta dentro del programa
		movida : bool  			# permite al nivel1 reintentar hasta hacer una jugada
		x : int					# Almacena la fila jugada por el usuario
		y : int					# Almacena la columna jugada por el usuario
		i : int  				# fila de la jugada de la IA
		j : int  				# columna de la jugada de la IA
		Ruser : list			# Almacena los resultados de jugadaUser()
		Rvictoria : list		# Almacena los resultados de Rvictoria()
		RIA : list				# Almacena los resultados de IA()
"""	
import random	 
import sys
# Lista de subprogramas (funciones) que usa el esqueleto principal:

def crearPosibles(tabl=list,anteriorfila=int, anteriorcolumna=int) -> list:
	# VAR:
		# Posibles : list 
		# Candidatos : list
		# hay_fila : bool
		# hay_columna						#Candidatos: Se incializa con -1, porque no existe\
	Candidatos=[[-1,-1]*8]					#dicha fila o comuna en una matriz. Posibles: Se inicia\
	hay_fila,hay_columna=False,False		#vacia para llenarse con aquellas opciones que cumplan las \
	Posibles=[]								#condiciones del caballo y que sean una posicion libre del tablero.
	if 0<=anteriorfila-2<Tam:				#-----------------------------------------------------------------
		Candidatos[0][0]=(anteriorfila-2)	
		Candidatos[1][0]=(anteriorfila-2)
		Candidatos[2][0]=(anteriorfila-1)
		Candidatos[3][0]=(anteriorfila-1)
		hay_fila=True
	elif 0<=anteriorfila-1<Tam:
		Candidatos[2][0]=(anteriorfila-1)
		Candidatos[3][0]=(anteriorfila-1)
		hay_fila=True

	if 0<=anteriorfila+2<Tam:
		Candidatos[4][0]=(anteriorfila+1)
		Candidatos[5][0]=(anteriorfila+1)
		Candidatos[6][0]=(anteriorfila+2)
		Candidatos[7][0]=(anteriorfila+2)
		hay_fila=True
	elif 0<=anteriorfila+1<Tam:
		Candidatos[4][0]=(anteriorfila+1)	#					"""CONDICIONES DEL CABALLO"""
		Candidatos[5][0]=(anteriorfila+1)		
		d=(anteriorfila+1)
		hay_fila=True
	
	if hay_fila:
		if 0<=anteriorcolumna-2<Tam:
		Candidatos[0][1]=(anteriorcolumna-2)
		Candidatos[1][1]=(anteriorcolumna-2)
		Candidatos[2][1]=(anteriorcolumna-1)
		Candidatos[3][1]=(anteriorcolumna-1)
		hay_fila=True
	elif 0<=anteriorcolumna-1<Tam:
		Candidatos[2][1]=(anteriorcolumna-1)
		Candidatos[3][1]=(anteriorcolumna-1)
		hay_fila=True

	if 0<=anteriorcolumna+2<Tam:
		Candidatos[4][1]=(anteriorcolumna+1)
		Candidatos[5][1]=(anteriorcolumna+1)
		Candidatos[6][1]=(anteriorcolumna+2)
		Candidatos[7][1]=(anteriorcolumna+2)
		hay_fila=True
	elif 0<=anteriorcolumna+1<Tam:
		Candidatos[4][1]=(anteriorcolumna+1)
		Candidatos[5][1]=(anteriorcolumna+1)		
		d=(anteriorcolumna+1)
		hay_fila=True						#-----------------------------------------------------------------

	if hay_columna and hay_fila:
		for i in range(8):
			if Candidatos[i][0]>-1 and Candidatos[i][1]>-1:
					if tabl[Candidatos[i][0]][Candidatos[i][1]]==0:		#Casilla libre
						Posibles.append(Candidatos[i])				#Es una posible jugada valida, se agrega
"""	Posibles.append(int(a+w))
	Posibles.append(int(a+y))
	Posibles.append(int(b+v))
	Posibles.append(int(b+z))
	Posibles.append(int(d+v))
	Posibles.append(int(d+z))
	Posibles.append(int(e+w))
	Posibles.append(int(e+y))
"""	
	return Posibles

#Descripcion: Pide al usuario la columna donde desea jugar, toma el tabl y lo devuelve mas las coordenadas de la jugada
# Parametros:
def jugadaUser( tabl = list, turno = int, Posibles=list ) -> (list,int,int) :
	# VAR:
		# jugada_seleccionada : int
		# opciones : int
		# Intentos : int
	Intentos=0
	opciones=len(Posibles)
	while Intentos<64:
		try:
			jugada_seleccionada=int(input("Escoja la jugada deseada: "))
			Intentos+=1
			assert(0<=jugada_seleccionada<opciones)
			break		
		except:
			print("Parece que no has escojido una jugada valida")
	if Intentos=64:
		print("Demasiados intentos, tendras que empezar de nuevo")
		sys.exit

	anteriorfila=Posibles[jugada_seleccionada][0]
	actualcolumna=Posibles[jugada_seleccionada][1]	
	tabl[actualfila][actualcolumna]=turno
		
	return tabl,actualfila,actualcolumna

#Clase que nos almacenar los valores de juego

class valoresdejuego:
	turno=1								#turno de la partida en curso
	eleccion_algoritmo=2				#con cual algoritmo se estaba trabajando
	tabl=[[0]*Tam for i in range(Tam)]	#tablero de juego
	i=5									#fila de la ultima jugada de la IA
	j=3									#columna de la ultima jugada de la IA
anterior=valoresdejuego()				#estructura donde guardamos los datos de la partida

# Descripcion: Funcion que cada turno actualiza los valores de las variables de juego. 
# Parametros:
def actualizacion(estructura=valoresdejuego,turno=int,tabl=list,i=int,j=int):
		anterior.turno=turno
		anterior.eleccion_algoritmo=eleccion_algoritmo
		anterior.tabl=tabl
		anterior.i=i
		anterior.j=j
		return anterior

# Descripcion: Funcion que lee el archivo de guardado y almacena su informacion
#			en una lista para posteriormente sobreescribir las variables de juego. 
# Parametros:
def CargarJuego(archivo=str) -> list:
	try:
		assert(open(archivo,'r+'))
	except:
		print("No se encuentra partida cargada, guarde una partida primero")
	with open(archivo,'r+') as f:
		oldcontenido = f.readlines()
		contenido = [oldcontenido[i].rstrip() for i in range(5)]
	f.closed
	return contenido

# Descripcion: Funcion que escibe en el archivo de guardado los valores actuales
#				de las variables de juego(nombreusuario,turno,nivel,tabl,i,j,tabv). 
# Parametros:
def GuardarJuego(archivo=str, estructura=valoresdejuego): #no tiene salida
	with open(archivo,'w') as f:
		f.write(str(anterior.turno)+"\n")
		f.write(str(anterior.eleccion_algoritmo)+"\n")		
		f.write(str(anterior.tabl)+"\n")
		f.write(str(anterior.i)+"\n")
		f.write(str(anterior.j)+"\n")
	f.closed   
def Completado(tabl=list):
	for i in range(Tam):
		for j in range(Tam):
			if tabl[i][j]=0:
				return False
	return True

			


# Incializacion de las variables del juego:
dentro=True							# Para entrar en el loop del juego
jugando=False						# Para entra primero al menu
anteriorfila,anteriorcolumna=0,0	# Jugada Predeterminada de la IA en su primer turno
tabl=[[0]*Tam for i in range(Tam)]	# Crear tablero de juego logico.

#Loop del juego

while dentro :							# Dentro del juego
	if not(jugando):					# en menu
		while True: 					# Se permite al usuario introducir nuevos datos correctos
			try: 
				Tam=int(input("Indique el tamaño del tablero (Debe ser un natural mayor o igual que 3)"))
				assert( Tam>=3 )
				break
			except:
				print("Ingrese un natural mayor o igual que 3")			
			try: 
				eleccion_algoritmo=int(input("Que algorimo desea usar?(0=Manual,1=Fuerza_Bruta,2=Divide_y_conquistaras,3=Terminar)"))
				assert( eleccion_algoritmo==0 or eleccion_algoritmo==2 or eleccion_algoritmo==1 or eleccion_algoritmo==3 or eleccion_algoritmo==4 )
				break
			except:
				print("Seleccione 0,1,2,3 o 4")
		tabl=[[0]*Tam for i in range(Tam)]		# Crear tablero de juego lleno de ceros.
		jugando=True
		turno=1
		
		if eleccion_algoritmo==3:	# El usuario decide que quiere salir del juego
			dentro=False			# Salimos del loop del juego
			print("Hasta luego!")	# Nos depedimos del usuario
	
	elif jugando and eleccion_algoritmo==1:					#en partida
		if turno > Tam*Tam :			# el tablero se encuentra lleno, se declara empate
			jugando=False
			print "Has Agotado Tus Turnos"
		elif turno <= Tam*Tam :			# el tablero aun no ha llenado se sigue jugando	
			# Turno del usuario
			guardar=bool(input("Desea guardar su partida?(Si=Enter)(No=Else)"))
			if not(guardar): #escribimos en alrchivo de guardado las variales de juego actuales
				actualizacion(anterior,turno,eleccion_algoritmo,tabl,i,j) #actuliza las variables de juego
				GuardarJuego("guardado.txt",anterior)	# guarda el estado del juego en el archivo
			seguir=bool(input("Desea seguir en esta partida?(Si=Enter)(No=Else)")) # en cada turno
			if not(seguir):	
				Posibles=crearPosibles(tabl,anteriorfila,anteriorcolumna)
				if len(Posibles)==0:
					print "Se agotaron las opciones"
					contenido=CargarJuego("guardado.txt")	# Leemos el archivo donde guardamos la partida
					turno = int(contenido[0])
					eleccion_algoritmo = int(contenido[1])
					tabl = eval(contenido[2])
					anteriorfila = int(contenido[3])
					anteriorcolumna = int(contenido[4])
				elif len(Posibles)==1:
					tabl[Posibles[0][0]][Posibles[0][1]]=turno
					if Completado:
						print "Felicidades lo lograste"
						jugando=False
					elif not(Completado):
						print "Parece que fue una mala jugada"
						contenido=CargarJuego("guardado.txt")	# Leemos el archivo donde guardamos la partida
						turno = int(contenido[0])
						eleccion_algoritmo = int(contenido[1])
						tabl = eval(contenido[2])
						anteriorfila = int(contenido[3])
						anteriorcolumna = int(contenido[4])
				elif len(Posibles)>=2:
					print "Veamos el tablero"
					print "\n"
					print tabl
					print "Estas son tus Posibles jugadas"
					print "Opcion 0 1 2 3 4 5 6 7"
					print Posibles
					Ruser=jugadaUser(tabl, turno, Posibles)	# Almacenamos los cambios tras la jugada del usuario.
					tabl=Ruser[0]			# Reescribimos el tablero con la jugada
					anteriorfila=Ruser[1]		# Guardamos la fila de la jugada
					anteriorcolumna=Ruser[2]	# Guardamos la columna de la jugada

			turno = turno + 1		# contamos el siguiente turno


assert( dentro==False )

# Aqui termina el el loop del juego.