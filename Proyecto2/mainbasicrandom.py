#mainbasicrandom
import random

def Aleatorio_Basico(n=int,m=int):
	for i in range(1,m+1):
		a=random.randint(1,n-1)
		if a**(n-1)%n!=1:
			return "El  numero es compuesto"
		elif a**(n-1)%n==1:		
			return "el numero es primo"
    
#Esto me imagino que va en el main
N=int(input("Coloque el valor de n:"))
M=int(input("Coloque el valor de m para indicar cuantas veces se repetira el experimento:"))
print Aleatorio_Basico(N,M)
