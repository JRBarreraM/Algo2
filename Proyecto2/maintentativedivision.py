#maintentativedivision
def Division_por_Tentativa(n=int):
	primo=True
	i=2
	while i<=n**(0.5) and primo:
		if n % i==0:
			primo=False
			return ("el numero",n, "es compuesto")
		i=i+1

	if primo==True:
		return ("el numero",n, "es primo") 	

#Esto va en el main
n=int(input("Coloque el valor de n:"))
print Division_por_Tentativa(n)		
