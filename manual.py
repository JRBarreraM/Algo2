# Modo Manual
def manualPrincipal(Tam=int,ActualF=int,ActualC=int,tabl=list,turno=int,JugadasF=list,JugadasC=list):

    # Posibles Movimientos Del Caballo
    verticales = [-1,-2,-2,-1,1,2,2,1]
    horizontales = [2,1,-1,-2,-2,-1,1,2]

    # Verifica si las coordenadas de la jugada estan dentro del tablero
    def valida(m=int,n=int,ActualF=int,ActualC=int):
        return 0<=ActualF<m and 0<=ActualC<n

    # Imprime el tablero en la pantalla de la terminal
    def mostrar_tablero(Tam=int,ActualF=int,ActualC=int,tabl=list):
        for i in range(Tam):
            for j in range(Tam):
                if i==ActualF and j==ActualC:
                    print 'K',
                elif tabl[i][j]:
                    print 'v',
                else:
                    if i==ActualF-1 and j==ActualC+2:
                        print '0',
                    elif i==ActualF-1 and j==ActualC-2:
                        print '3',
                    elif i==ActualF-2 and j==ActualC+1:
                        print '1',
                    elif i==ActualF-2 and j==ActualC-1:
                        print '2',             
                    elif i==ActualF+1 and j==ActualC+2:
                        print '7',
                    elif i==ActualF+1 and j==ActualC-2:
                        print '4',
                    elif i==ActualF+2 and j==ActualC+1:
                        print '6',
                    elif i==ActualF+2 and j==ActualC-1:
                        print '5',
                    else:
                        print 'o',
                print '|',
            print '\n'

    # Imprimimos el tablero
    mostrar_tablero(Tam,ActualF,ActualC,tabl)

    # Verificamos si quedan movimientos validos
    if turno==Tam*Tam:
        return 1    

    # Pedimos al usuario que escoja
    while True:
        try:
            movimiento=int(input("Movimiento(-1 = un mov atras)(-2 = empezar de nuevo)(-3 = abandonar): "))
            assert(7 >= movimiento >= -3)
            break
        except:
            print 'Por favor ingrese un movimiento valido'

    # Deshacer Jugada
    if movimiento==-1:
        if len(JugadasF)==1:
            print "No se ha hecho ningun movimiento"
            return manualPrincipal(Tam,ActualF,ActualC,tabl,turno,JugadasF,JugadasC)
        else:               # Llevamos las varibles al estado anterior
            JugadasF.pop()
            JugadasC.pop()
            tabl[ActualF][ActualC]=0
            return manualPrincipal(Tam,JugadasF[len(JugadasF)-1],JugadasC[len(JugadasC)-1],tabl,turno-1,JugadasF,JugadasC)

    elif movimiento==-2:    # Se eliminan todos los movimientos y se comienza desde el ultimo
        tabl=[Tam*[0] for i in range(Tam)]
        tabl[ActualF][ActualC]=1
        manualPrincipal(Tam,ActualF,ActualC,tabl,1,[ActualF],[ActualC])
    elif movimiento==-3:    # Se abandona el modo manual
        return 0

    Ki=ActualF+verticales[movimiento]       # Fila del movimiento actual del caballo
    Kj=ActualC+horizontales[movimiento]     # Columna del movimiento actual del caballo
    
    # Mover
    if valida(Tam,Tam,Ki,Kj):
        if tabl[Ki][Kj]==1:                 # No esposible jugar en la casilla
            print " Casilla ya visitada"
            return manualPrincipal(Tam,ActualF,ActualC,tabl,turno,JugadasF,JugadasC)
        elif tabl[Ki][Kj]==0:  
            tabl[Ki][Kj]=1                  # Marcamos la casilla como visitada
            JugadasF.append(Ki)             # Agregamos las coordenadas al registro \
            JugadasC.append(Kj)             # de filas y columnas visitadas
            return manualPrincipal(Tam,Ki,Kj,tabl,turno+1,JugadasF,JugadasC)
    else:
        print "Movimiento invalido"
        return manualPrincipal(Tam,ActualF,ActualC,tabl,turno,JugadasF,JugadasC)