# Modo Divide y Conquistaras

"""
def indice_subtabl_sup_izq(subtabl sup izq):
    if (tam/2)%2==0:
        inicio=tabl[(tam/2)-1][(tam/n) - 3]
        fin= tabl[(tam/2)-2][(tam/2)-1]
    elif (tam/2)%2!=0:
        inicio=tabl[(tam/2)-1][(tam/2)-2]
        fin=tabl[(tam/2)-3][(tam/2)-1]
        # hay que decirle a fuerza bruta que en ese recorrido no toque la posicion 
        #tabl[(tam/2)-1][(tam/2)-1]

def indice_subtabl_inf_izq(subtabl inf izq):
    If (tam/2)%2==0:
        inicio=tabl[(tam/2)][(tam/2) - 1]
        fin= tabl[(tam/2)+2][(tam/2)-2]
    elif (tam/2)%2!=0:
        inicio=tabl[(tam/2)-1][(tam/2)-2]
        fin=tabl[(tam/2)-3][(tam/2)-1]
        # hay que decirle a fuerza bruta que en ese recorrido no toque la posicion 
        #tabl[(tam/2)][(tam/2)-1]

def indice_subtabl_inf_der(subtabl inf der):
    if (tam/2)%2==0:
        inicio=tabl[(tam/2)+1][(tam/2)]
        fin= tabl[(tam/2)][(tam/2)+2]
    elif (tam/2)%2!=0:
        inicio=tabl[(tam/2)-1][(tam/2)-2]
        fin=tabl[(tam/2)-3][(tam/2)-1]
        # hay que decirle a fuerza bruta que en ese recorrido no toque la posicion 
        #tabl[(tam/2)][(tam/2)]

def indice_subtabl_sup_der(subtabl inf der):
    if (tam/2)%2==0:
        inicio=tabl[(tam/2)-1][(tam/2)]
        fin= tabl[(tam/2)-3][(tam/2)+1]
    elif (tam/2)%2!=0:
        inicio=tabl[(tam/2)-1][(tam/2)-2]
        fin=tabl[(tam/2)-3][(tam/2)-1]
        # hay que decirle a fuerza bruta que en ese recorrido no toque la posicion 
        #tabl[(tam/2)-1][(tam/2)]
"""
sol8 = [[7,5],[5,4],[6,6],[7,4],[6,2],[7,0],[5,1],[7,2],[6,0],[4,1],[2,0],[0,1],[2,2],[3,0],[1,1],[0,3],[1,5],[0,7],[2,6],[4,7],[3,5],[1,6],[3,7],[5,6],[7,7],[6,5],[7,3],[6,1],[4,0],[2,1],[0,0],[1,2],[0,4],[2,5],[1,7],[0,5],[1,3],[3,2],[5,3],[3,4],[4,2],[5,0],[7,1],[6,3],[4,4],[2,3],[0,2],[1,0],[3,1],[5,2],[6,4],[4,3],[5,5],[7,6],[5,7],[3,6],[2,4],[4,5],[3,3],[2,4],[0,6],[2,7],[4,6],[6,7]]
sol6 = [[5,0],[3,1],[1,0],[0,2],[1,4],[3,5],[4,3],[5,5],[3,4],[1,5],[2,3],[1,1],[3,0],[5,1],[3,2],[4,0],[5,2],[4,4],[2,5],[0,4],[1,2],[0,0],[2,1],[1,3],[0,5],[2,4],[0,3],[2,2],[0,1],[2,0],[4,1],[5,3],[4,5],[3,3],[5,4],[4,2]]
def Divide_ConquerPrincipal(Tam=int,opcion=int):
	if opcion==2:
		def power2(Tam):
			if Tam!= 8:
				Tam= Tam/ 2
				sol = power2(Tam)
				R = 4*len(sol)*[0]

				for k in range(len(sol)):
					R[k] = [sol[k][0],sol[k][1]]
					R[k + len(sol)] = [sol[k][0],sol[k][1] + Tam]
					R[k + 2 * len(sol)] = [sol[k][0] + Tam, sol[k][1] + Tam]
					R[k + 3 * len(sol)] = [sol[k][0] + Tam, sol[k][1]]

				divisionSize = len(R)/4

				for k in range(0,len(R) - divisionSize,divisionSize):
					R = reorderSol(R, Tam, k + divisionSize, k + 2*divisionSize)
				return R
			else:
				return sol8

		def reorderSol(A, Tam, initialIndex, finalIndex):

			if len(A)/4 <= initialIndex < 2*len(A)/4:
				valorIndice = [Tam-3,Tam+1]
				index = A.index([Tam-3,Tam+1])
				reference = [Tam-1,Tam]
			elif 2*len(A)/4 <= initialIndex < 3*len(A)/4:
				valorIndice = [Tam,Tam+2]
				index = A.index([Tam,Tam+2])
				reference = [Tam+1,Tam]
			elif 3*len(A)/4 <= initialIndex < len(A):
				valorIndice = [Tam+2,Tam-2]
				index = A.index([Tam+2,Tam-2])	
				reference = [Tam,Tam-1]


			if A[index + 1] == reference:
				L = A[initialIndex:index + 1]
				R = A[index + 1:finalIndex]

				L.reverse()
				R.reverse()
			else:
				L = A[index:finalIndex]
				R = A[initialIndex:index]
						
			sol = A[:initialIndex] + L + R + A[finalIndex:]
			#print len(sol)
			return sol
	elif opcion==12:
		def mult12(Tam):
			if Tam!= 6:
				Tam= Tam/ 2
				sol = mult12(Tam)
				R = 4*len(sol)*[0]

				for k in range(len(sol)):
					R[k] = [sol[k][0],sol[k][1]]
					R[k + len(sol)] = [sol[k][0],sol[k][1] + Tam]
					R[k + 2 * len(sol)] = [sol[k][0] + Tam, sol[k][1] + Tam]
					R[k + 3 * len(sol)] = [sol[k][0] + Tam, sol[k][1]]

				divisionSize = len(R)/4

				for k in range(0,len(R) - divisionSize,divisionSize):
					R = reorderSol(R, Tam, k + divisionSize, k + 2*divisionSize)
					return R
			else:
				return sol6