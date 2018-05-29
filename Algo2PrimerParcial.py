def linear_search(A=str, x=str):
	for i in range(len(A)):
		if A[i]==x:
			return i
		i=i+1
	return -1

def binary_search(A=str, x=str):
	start = 0
	end = len(A) -1
	while start < end :
		mid = (start+end)/2
		if A[mid]==x:
			return mid
		elif x>A[mid]:
			start=mid+1
		elif x<A[mid]:
			end=mid-1

	if A[start]==x:
		return start
	return -1

def insertion_sort(A):
	start=0
	end=len(A)
	for j in range(end):
		key = A[j]
		i = j - 1
		while i >= start and A[i] > key :
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

def insertion_sort(A):
	start=0
	end=len(A)
	for j in range(end):
		key = A[j]
		i = j - 1
		while i >= start and A[i] > key :
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

def merge(A, p, r, q):
    n1 = r - p + 1
    n2 = q- r
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0 , n1):
        L[i] = A[p + i]
 
    for j in range(0 , n2):
        R[j] = A[r + 1 + j]
 
    i = 0
    j = 0
    k = p
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
 

def aux_mergesort(A,p,q):			# Esta funcion auxiliar es necesaria para que el merge
    if p < q:						# no use centinelas y se mantengan las firmas de las
        r = int((p+(q-1))/2)		# subrutinas tal y como se pidieron, ademas no afecta
        aux_mergesort(A, p, r)		# el tiempo de ejecucion del algoritmo.
        aux_mergesort(A, r+1, q)
        merge(A, p, r, q)

def mergesort(A):
	aux_mergesort(A,0,len(A)-1)
	return A			

def multiply(N, A, Z):
	ZZ= N*[0]
	for I in range(N):
		for J in range(N):
			ZZ[I]=ZZ[I]+(A[I][J]*Z[J])
	return ZZ

def freivalds(N, A, B, C):
	Z = N*[0]				# vector fila de ceros
	for I in range(N):
		Z[I] = Random(0,1)	# construimos vector aleatorio
	Y=multiply(N,B,Z)
	X1 = multiply(N,A,Y)
	X2 = multiply(N,C,Z)
	return X1 == X2 

def amplified_freivalds(k, n, A, B, C):
    for i in range(k):
        r = freivalds(n, A, B, C)
        if r == False:
            return False
    return True

def check_if_exist(A=str, x=str): #es un binary_search con un cambio en el output
	start = 0						# pues no nos interesa el numero, solo si existe.
	end = len(A) -1
	while start < end :
		mid = (start+end)/2
		if A[mid]==x:
			return True
		elif x>A[mid]:
			start=mid+1
		elif x<A[mid]:
			end=mid-1
	if A[start]==x:
		return True
	return False

def problema_3_8(A, x):	# problema_3_8, es O(nlog(n)) en el peor de las casos,
	mergesort(A)		# pues mergesort es O(nlog(n)) y binary_search es O(log(n)),
	N=len(A)			# ya que aplicamos binary_search a lo sumo n veces,
	for I in range(N):  # el tiempo de corrida en el peor caso es n(log(n)),
		KEY=x-A[I]		# por lo que todo el programa toma 2(nlog(n)).
		if check_if_exist(A,KEY):
			return True
	return False

#### HEAPSORT

# aplica heapsort al arrego A
def heapsort(A):
    heapsort_aux(A, 0, len(A) - 1)

# aplica heapsort al arrego A[p...r]
def heapsort_aux(A, p, r):

    # Build a maxheap.
    build_max_heap(A,p,r)
 
    for i in range(r, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A,0,p,i)

# aplica max-heapify en nodo i del arreglo A[p..r]
def max_heapify(A, i, p, r):

    left = heap_left(i,p,r)
    right = heap_right(i,p,r)
    largest=i
    
    if left < r and A[left] > A[i]:
        largest=left
    
    if right < r and A[right] > A[largest]:
        largest=right
    
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,p,r)

# construye un max-heap en el arreglo A[p...r]
def build_max_heap(A, p, r):
    for i in range(r+1, -1, -1):
        max_heapify(A,i,p,r+1)

# retorna el indice del hijo izquierdo del nodo i en el heap [p...r]
def heap_left(i, p, r):

    index = i - p + 1
    left_child = 2 * index
    return p + left_child - 1

# retorna el indice del hijo derecho del nodo i en el heap [p...r]
def heap_right(i, p, r):

    index = i - p + 1
    right_child = 2 * index + 1
    return p + right_child - 1

#### QUICKSORT

# aplica quicksort al arreglo A
def quicksort(A):
    quicksort_rec(A, 0, len(A) - 1, partition)

# aplica quicksort randomizado al arreglo A
def quicksort_randomized(A):
    quicksort_rec(A, 0, len(A) - 1, partition_randomized)

# funcion de particion para quicksort deterministico sobre el arreglo A[p...r]
def partition(A, p, r):
    pivot = A[r]
    return partition_with_pivot(A, p, r, pivot)

# funcion de particion para quicksort randomizado sobre el arreglo A[p...r]
def partition_randomized(A, p, r):
    pivot_index = Random(p, r)
    pivot = A[pivot_index]
    A[pivot_index],A[r] = A[r], A[pivot_index]
    return partition_with_pivot(A, p, r, pivot)

# aplica quicksort con funcion de particion dada al arreglo A[p...r]
def quicksort_rec(A, p, r, partition_function):
    if p < r :
        l,m = partition_function(A,p,r)
        quicksort_rec(A, p, l,partition_function)
        quicksort_rec(A, m, r,partition_function)


# funcion de particion con pivote dado. El ultimo elemento en el
# arreglo es igual al pivote. La funcion retorna dos indices l,m
# tales que:
#   *  A[i] < pivot para p <= i < l
#   *  A[i] == pivot para l <= i <= m
#   *  A[i] > pivot para m < i <= r
#
# La funcion es simiular a la vista en clase excepto que para el lazo
# principal hay tres indices i, j, k tales que el siguiente invariante
# se mantiene:
#   * elementos A[p], A[p+1], ..., A[i] son < pivot
#   * elementos A[i+1], A[i+2], ..., A[j-1] son > pivot
#   * elementos A[j], A[j+1], ..., A[k-1] son "desconocidos"
#   * elementos A[k], A[k+1], ..., A[r] son == pivot
#
# Inicialmente, i = p-1, j = p, y k = r. El procedimiento tiene un 
# lazo principlan y corre en tiempo linear.
#
# Una vez que el lazo principal termina, se deben mover los elementos
# A[k], A[k+1], ..., A[r] que son iguales al pivote al "medio" del 
# arreglo en las posiciones A[l], A[l+1], ..., A[m]
def partition_with_pivot(A, p, r, pivot):
    i = p-1
    j = p
    k = r
    while j<k:
        if A[j] < pivot:
            i = i + 1
            A[i],A[j]=A[j],A[i]
            j+=1
        elif A[j] == pivot:
            k = k - 1
            A[k],A[j]=A[j],A[k]
        elif A[j] > pivot:
            j+=1
    for o in range(r-k+1):
        A[k+o],A[i+1+o]=A[i+1+o],A[k+o]
    l,m=i,i+r-k+1
    return l,m
# Para retornar los indices l,m en la funcion partition_with_pivot, 
# utilice 'return l, m'

# Para recibir los indices l,m en la llama da partition_function en la
# funcion quicksort_rec, utilice 'l, m = partition_function(A, p, r)'

########################################################################
#	Explicacion:
#	A pesar de que los algoritmos deben usar mas memoria (merge necesita 2
#	arreglos de n elementos adicionales, y partition_randomized necesita una
#	variable auxiliar mas), el comportamiento asintotico no se ve afectado
#	porque las asignaciones extra toman tiempo constante, asi que los
#	algoritmos siguen siendo nlog(n) en caso promedio.
########################################################################

#def merge(A, B, p, r, q):
def merge(values,sortBy, p, r, q):
    n1 = r - p + 1
    n2 = q - r
 
    LV = [0] * (n1)
    RV = [0] * (n2)
    LS = [0] * (n1)
    RS = [0] * (n2) 
 
    for i in range(0 , n1):
        LS[i] = sortBy[p + i]
        LV[i] = values[p + i]
 
    for j in range(0 , n2):
        RS[j] = sortBy[r + 1 + j]
        RV[j] = values[r + 1 + j]

    i = 0
    j = 0
    k = p
 
    while i < n1 and j < n2 :
        if LS[i] <= RS[j]:
            sortBy[k] = LS[i]
            values[k] = LV[i]
            i += 1
        else:
            sortBy[k] = RS[j]
            values[k] = RV[j]
            j += 1
        k += 1

    while i < n1:
        sortBy[k] = LS[i]
        values[k] = LV[i]
        i += 1
        k += 1

    while j < n2:
        sortBy[k] = RS[j]
        values[k] = RV[j]
        j += 1
        k += 1

#def aux_mergesort(A,B,p,q):
def aux_mergesort(values,sortBy,p,q):
    if p < q:
        r = int((p+(q-1))/2)
        aux_mergesort(values,sortBy, p, r)
        aux_mergesort(values,sortBy, r+1, q)
        merge(values,sortBy, p, r, q)

#def mergesort(A,B):
def mergesort(values, sortBy):
	aux_mergesort(values,sortBy,0,len(values)-1)

#### QUICKSORT

# aplica quicksort por referencia al arreglo A en base al B
def quicksort(values, sortBy):
    quicksort_rec(values, sortBy, 0, len(sortBy) - 1, partition)

# aplica quicksort randomizado por referencia al arreglo A en base al B
def quicksort_randomized(values, sortBy):
    quicksort_rec(values, sortBy, 0, len(sortBy) - 1, partition_randomized)

# funcion de particion para quicksort deterministico sobre el arreglo A[p...r]
def partition(values, sortBy, p, r):
    pivot = sortBy[r]
    return partition_with_pivot(values, sortBy, p, r, pivot)

# funcion de particion para quicksort randomizado sobre el arreglo A[p...r]
def partition_randomized(values, sortBy, p, r):
    pivot_index = random.randint(p, r)
    pivot = sortBy[pivot_index]
    pivotin = values[pivot_index]
    sortBy[pivot_index] = sortBy[r]
    values[pivot_index] = values[r]
    sortBy[r] = pivot
    values[r] = pivotin
    return partition_with_pivot(values, sortBy, p, r, pivot)

# aplica quicksort con funcion de particion dada al arreglo A[p...r]
def quicksort_rec(values, sortBy, p, r, partition_function):
    if p < r :
        l,m = partition_function(values, sortBy, p, r)
        quicksort_rec(values, sortBy, p, l, partition_function)
        quicksort_rec(values, sortBy, m, r, partition_function)

# funcion de particion con pivote dado. El ultimo elemento en el
# arreglo es igual al pivote. La funcion retorna dos indices l,m
# tales que:
#   *  A[i] < pivot para p <= i < l
#   *  A[i] == pivot para l <= i <= m
#   *  A[i] > pivot para m < i <= r
#
# La funcion es simiular a la vista en clase excepto que para el lazo
# principal hay tres indices i, j, k tales que el siguiente invariante
# se mantiene:
#   * elementos A[p], A[p+1], ..., A[i] son < pivot
#   * elementos A[i+1], A[i+2], ..., A[j-1] son > pivot
#   * elementos A[j], A[j+1], ..., A[k-1] son "desconocidos"
#   * elementos A[k], A[k+1], ..., A[r] son == pivot
#
# Inicialmente, i = p-1, j = p, y k = r. El procedimiento tiene un 
# lazo principlan y corre en tiempo linear.
#
# Una vez que el lazo principal termina, se deben mover los elementos
# A[k], A[k+1], ..., A[r] que son iguales al pivote al "medio" del 
# arreglo en las posiciones A[l], A[l+1], ..., A[m]

def partition_with_pivot(values, sortBy, p, r, pivot):
    i = p-1
    j = p
    k = r
    while j<k:
        if sortBy[j] < pivot:
            i = i + 1
            sortBy[i],sortBy[j]=sortBy[j],sortBy[i]
            values[i],values[j]=values[j],values[i]            
            j+=1
        elif sortBy[j] == pivot:
            k = k - 1
            sortBy[k],sortBy[j]=sortBy[j],sortBy[k]
            values[k],values[j]=values[j],values[k]

        elif sortBy[j] > pivot:
            j+=1
    for o in range(r-k+1):
        sortBy[k+o],sortBy[i+1+o]=sortBy[i+1+o],sortBy[k+o]
        values[k+o],values[i+1+o]=values[i+1+o],values[k+o]

    l,m=i,i+r-k+1
    return l,m

# Para retornar los indices l,m en la funcion partition_with_pivot, 
# utilice 'return l, m'

# Para recibir los indices l,m en la llama da partition_function en la
# funcion quicksort_rec, utilice 'l, m = partition_function(A, p, r)'