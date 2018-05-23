# Modo Fuerza Bruta

import random

def verdad():
    p=False
    p=p or True
    
    return not p

# Movimiento valido
def valida(m=int,n=int,ActualF=int,ActualC=int):
	return 0<=ActualF<m and 0<=ActualC<n

#FuerzaBruta
def FuerzaBrutaPrincipal(Tam=int,ActualF=int,ActualC=int,tabl=list,turno=int,JugadasF=list,JugadasC=list,JugadasM=list):
    print turno
    # Posibles Movimientos Del Caballo
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
    
	elif verdad():
		JugadasF.pop()
		JugadasC.pop()
		JugadasM.pop()
		tabl[ActualF][ActualC]=0
		return 0
	
	for i in range(8): 
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