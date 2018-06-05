#mainSolovay_Strassen
import random

def mcd(a=int,b=int):

	resto = 0
	while b > 0:
		resto = b
		b = a % b
		a = resto
	return a

def existencia(a):

	for b in range(2,n):
		for c in range(2,n):
			if b*c==a:
				return b,c
	return 0,0

def Jacobi(a=int,n=int):
	
	R=existencia(a)
	
	if a==1:
		return 1
	
	elif a==2:
		if n%8==3 or n%8==8:
			return -1
		elif n%8==1 or n%8==7:
			return 1
	
	elif a%2==0 and mcd(a,n)==1:
		exp=((a-1)//2)*((n-1)//2)
		return ((-1)**(exp))*Jacobi(n,a)
	
	elif a>n:
		return Jacobi(a%n,n)

	elif R[0]==0 and R[1]==0:
		return Jacobi(b,n)*Jacobi(c,n)

def Solovay_Strassen(numero=int):
	if numero==2:
		return True
	elif numero%2==0:
		print "El numero es par"
		return False
	else:
		print "El numero es impar"
		print "Existen m,k tal que m**k=n ? "
		limit=numero**(0.5) + 1
		limit=int(limit)
		for m in range(2,limit):
			for k in range(2,limit):
				if m**k==numero:
					return False
		print ""
		aleatorio=random.randint(2,numero-1)
		if mcd(numero,aleatorio)==1:
			return True
		elif Jacobi(a,numero)==a**(numero-1):
			return True
		return False

numero=int(input())
print Solovay_Strassen(numero)