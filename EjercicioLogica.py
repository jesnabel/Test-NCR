# A Y B son los tablones A inicio, B fin
# C son los clavos (posicion en el tablon)




def solucion(A, B, C): # Se reciben los 3 arrays iniciales: tablones A, tablones B y Clavos
    final = len(C)
    inicio = 0
    resultado = -1 
    while final >= inicio: 
        mitad = (inicio + final) // 2
        if checkear(A, B, C, mitad):
            final = mitad - 1
            resultado = mitad
        else:
            inicio = mitad + 1
    return resultado


def checkear(A, B, C, M): # Aca va a determinar si los clavos pueden clavar los tablones en base al rango de A y B, sino da -1
    clavos = [0] * 2 * ( len(C) + 1 )
    for I in range(0, M):
        clavos[C[I]] += 1
    for I in range(1, len(clavos)):
        clavos[I] += clavos[I - 1]
    for I in range(len(A)):
        if (clavos[B[I]] - clavos[A[I]-1]) == 0:
            return False
    return True

