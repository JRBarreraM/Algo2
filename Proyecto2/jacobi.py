def Jacobi(a=int,n=int):
	
	R=existencia(a)
	
	if a==1:
		return 1
	
	elif a==2:
		if n%8==3 or n%8==8:
			return -1
		elif n%8==1 or n%8==7:
			return 1
	
	elif a%2==0 and coprimos(a,n):
		exp=((a-1)//2)*((n-1)//2)
		return ((-1)**(exp))*Jacobi(n,a)
	
	elif a>n:
		return Jacobi(a%n,n)

	elif R[0]==0 and R[1]==0:
		return Jacobi(b,n)*Jacobi(c,n)
Jacobi(1,2)