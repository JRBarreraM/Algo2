import random
verticales = [-1,-2,-2,-1,1,2,2,1]
horizontales = [2,1,-1,-2,-2,-1,1,2]
def over(n,Kx,Ky,V):
    p=False;
    for i in range(8):
        x=Kx+verticales[i];
        y=Ky+horizontales[i];
        if valida(n,n,x,y):
            p=p or V[x][y]==0;
    return not p

# Movimiento valido
def valida(m=int,n=int,ActualF=int,ActualC=int):
	return 0<=ActualF<m and 0<=ActualC<n

#FuerzaBruta
def FuerzaBrutaPrincipal(Tam=int,ActualF=int,ActualC=int,tabl=list,turno=int,JugadasF=list,JugadasC=list,JugadasM=list):
    # Movimientos
	verticales = [-1,-2,-2,-1,1,2,2,1]
	horizontales = [2,1,-1,-2,-2,-1,1,2]
    
	if turno==Tam*Tam:				# Ha finalizado el recorrido
		for i in range(len(JugadasF)):
			tabl[JugadasF[i]][JugadasC[i]]=i
		for i in range(Tam):			# Se muestra el tablero
			for j in range(Tam):
				print tabl[i][j],
				print '|',
			print '\n'
		return 1
    
	elif over(Tam,ActualF,ActualC,tabl):
		JugadasF.pop()
		JugadasC.pop()
		JugadasM.pop()
		tabl[ActualF][ActualC]=0
		return 0

	opciones=[0,1,2,3,4,5,6,7]
	
	for j in range(8): 
		i=random.choice(opciones)
		x=ActualF+verticales[i]
		y=ActualC+horizontales[i]
		aux=valida(Tam,Tam,x,y)
		if aux:
			if tabl[x][y]==0:
				JugadasF.append(x)
				JugadasC.append(y)
				JugadasM.append(i)
				tabl[x][y]=1
				ret = FuerzaBrutaPrincipal(Tam,x,y,tabl,turno+1,JugadasF,JugadasC,JugadasM)
				if ret:
					return 1
		elif aux:
			opciones.remove(i)

	JugadasF.pop()
	JugadasC.pop()
	JugadasM.pop()
	tabl[ActualF][ActualC]=0
	return 0