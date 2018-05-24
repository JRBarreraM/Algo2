# Modo Fuerza Reservada

#FuerzaBruta
def FuerzaReservadaPrincipal(Tam=int,ActualF=int,ActualC=int,FilaReservada=int,ColumnaReservada=int,tabl=list,turno=int,JugadasF=list,JugadasC=list):
	#print turno
	# Posibles Movimientos Del Caballo
	filas = [-1,-2,-2,-1,1,2,2,1]
	columnas = [2,1,-1,-2,-2,-1,1,2]

	if turno==Tam*Tam:				# Ha finalizado el recorrido
		for i in range(len(JugadasF)):
			tabl[JugadasF[i]][JugadasC[i]]=i
		for i in range(Tam):			# Se muestra el tablero
			for j in range(Tam):
				print tabl[i][j],
				print '|',
			print '\n'
		print "Se muestra el recorrido logrado, los arreglos corresponden a las Filas y Columnas de cada Movimiento"
		print JugadasF
		print JugadasC
		return 1		# Se termina satisfactoria mente el recorrido
	
	elif turno==Tam*Tam-1:
		for z in range(8):
			i=ActualF+filas[z]
			j=ActualC+columnas[z]
		if (i==FilaReservada) and (j==ColumnaReservada):
			JugadasF.append(i)
			JugadasC.append(j)
			tabl[i][j]=1
			if FuerzaReservadaPrincipal(Tam,i,j,FilaReservada,ColumnaReservada,tabl,turno+1,JugadasF,JugadasC)==1:
				return 1
		JugadasF.pop()
		JugadasC.pop()
		#print JugadasF
		#print JugadasC
		#print "Back Tracking"
		tabl[ActualF][ActualC]=0
		return 0

	for z in range(8):
		i=ActualF+filas[z]
		j=ActualC+columnas[z]
		if (0<=i<Tam) and (0<=j<Tam) and (i!=FilaReservada or j!=ColumnaReservada):
			if tabl[i][j]==0:
				JugadasF.append(i)
				JugadasC.append(j)
				tabl[i][j]=1
				if FuerzaReservadaPrincipal(Tam,i,j,FilaReservada,ColumnaReservada,tabl,turno+1,JugadasF,JugadasC)==1:
					return 1
	JugadasF.pop()
	JugadasC.pop()
	#print JugadasF
	#print JugadasC
	#print "Back Tracking"
	tabl[ActualF][ActualC]=0
	return 0