'''
Ahora mismo hay 2 técnicas de resolución:

    - La primera comprueba si existe un solo candidato en una casilla
    - La segunda comprueba si en cada línea, columna y grupo existe un solo candidato de entre todos

Ambas se aplican con la función: *resolver_numeros_unicos*

Cuando esto ya no permite sacar más números, es necesario eliminar candidatos, para ello se han implementado dos técnicas.

    - La primera analiza los candidatos que existen en una columna o fila, y solo en esa columna o fila dentro de un grupo, lo que significará que no podrá existir ese candidato en el resto de la fila o columna en los restantes grupos. Esto se realiza mediante la función: "algorit_proyeccion_grupos", que itera n veces "analisis_grupos" hasta que no se eliminan más candidatos
    - La segunda, busca dos pares de candidatos iguales que se encuentran en distintos grupos, ya que esos valores serán autoexlusivos, y por lo tantos esos dos candidatos podrán ser eliminados del resto de las casillas en la fila o columna que se encuentren las parejas. Esto se realiza mediante la función: "algorit_detecta_pares", que itera n veces "detecta_pares" hasta que no se eliminan más candidatos

'''


import numpy as np
from tabulate import tabulate


def imprimir_sudoku():
    # tabulate data
    table = tabulate(sudoku, tablefmt="fancy_grid")
    print(table)


def imprimir_posibilidades():
    # tabulate data
    table = tabulate(posibles, tablefmt="fancy_grid")
    print(table)


sudoku = np.zeros((9, 9), int)

'''
sudoku[0][5]=7
sudoku[0][7]=5
sudoku[1][0]=4
sudoku[1][5]=9
sudoku[1][7]=1
sudoku[2][1]=1
sudoku[2][6]=9
sudoku[3][0]=5
sudoku[3][4]=1
sudoku[4][1]=9
sudoku[4][2]=2
sudoku[4][6]=7
sudoku[4][7]=3
sudoku[5][4]=8
sudoku[5][8]=2
sudoku[6][2]=5
sudoku[6][7]=4
sudoku[7][1]=6
sudoku[7][3]=3
sudoku[7][8]=7
sudoku[8][1]=3
sudoku[8][3]=8
'''
'''
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
sudoku[][]=
'''
sudoku[0][1] = 2
sudoku[0][7] = 8
sudoku[1][0] = 9
sudoku[1][3] = 6
sudoku[1][5] = 1
sudoku[1][8] = 2
sudoku[2][4] = 7
sudoku[3][2] = 5
sudoku[3][3] = 4
sudoku[3][5] = 8
sudoku[3][6] = 9
sudoku[4][1] = 7
sudoku[4][4] = 9
sudoku[4][7] = 4
sudoku[6][2] = 1
sudoku[6][3] = 8
sudoku[6][5] = 2
sudoku[6][6] = 5
sudoku[7][0] = 3
sudoku[7][8] = 6
sudoku[8][0] = 7
sudoku[8][2] = 4
sudoku[8][6] = 2
sudoku[8][8] = 8

posibles = np.empty((9, 9), dtype=object)

imprimir_sudoku()


# Comprueba si esta resuelto y devuelve cuantos valores le faltan sino
def comprobar_resuelto():
    faltantes = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if posibles[i][j] != []:
                faltantes += 1

    return faltantes

# Funciones para ver si en una columna, una fila o un grupo es posible un valor y generar la lista de posibilidades
def columna_viable (valor, columna):
    for i in range(0,9):
        # Quitar que se compruebe el valor correspondiente a la casilla en cuestion, como es 0 en principio daria igual
        # porque no lo encontraria
        if sudoku[i][columna] == valor:
            return False
    return True

def fila_viable (valor, fila):
    for i in range(0,9):
        # Quitar que se compruebe el valor correspondiente a la casilla en cuestion, como es 0 en principio daria igual
        # porque no lo encontraria
        if sudoku[fila][i] == valor:
            return False
    return True

def grupo_viable (valor, fila, columna):
    indice_x = (fila//3)*3
    indice_y = (columna//3)*3
    for i in range(indice_x, indice_x + 3):
        for j in range(indice_y, indice_y + 3):
        # Quitar que se compruebe el valor correspondiente a la casilla en cuestion, como es 0 en principio daria igual
        # porque no lo encontraria
            if sudoku[i][j] == valor:
                return False
    return True

def numero_viable (valor, fila, columna):
    if grupo_viable (valor, fila, columna) == True:
        if fila_viable (valor, fila) == True:
            if columna_viable (valor, columna) == True:
                return True
    return False

# Funciones para ver si en una columna, una fila o un grupo un valor es único y será el que haya que asignar
def columna_unico (valor, fila, columna):
    for i in range(0,9):
        if i != fila:
            if valor in posibles[i][columna]:
                return False
    return True

def fila_unico (valor, fila, columna):
    for i in range(0,9):
        if i != columna:
            if valor in posibles[fila][i]:
                return False
    return True

def grupo_unico (valor, fila, columna):
    indice_x = (fila//3)*3
    indice_y = (columna//3)*3
    for i in range(indice_x, indice_x + 3):
        for j in range(indice_y, indice_y + 3):
            if not((i == fila) and (j == columna)):
                if valor in posibles[i][j]:
                    return False
    return True

def numero_unico (valor, fila, columna):
    if grupo_unico (valor, fila, columna) == True:
        return True
    if fila_unico (valor, fila, columna) == True:
        return True
    if columna_unico (valor, fila, columna) == True:
        return True
    return False


# Funcion que forma el array de posibles valores desde cero
# Será necesario formarla cada vez que se descubra un valor nuevo en el sudoku
def iniciar_posibles_valores():
    # Posibles valores

    for i in range(0, 9):
        for j in range(0, 9):
            posibles[i][j] = []

    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                for valor in range(1, 10):
                    if numero_viable(valor, i, j) == True:
                        posibles[i][j].append(valor)


# Con el array de posibles actual comprueba si hay alguna opción única en una columna, fila o grupo y lo aplica al sudoku
# Además comprueba si en una sola casilla existe una sola opción porque se haya limpiado la lista de posibles candidatos
# con alguno de los algoritmos de reducción
def resolver_numeros_unicos():
    # Numeros únicos
    adivinados = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if len(posibles[i][j]) > 0:

                if len(posibles[i][j]) == 1:
                    adivinados += 1
                    print("Se ha seleccionado el número: ", posibles[i][j][0], " en la posición ", i, " - ", j)
                    sudoku[i][j] = posibles[i][j][0]

                else:
                    for h in range(0, len(posibles[i][j])):
                        if numero_unico(posibles[i][j][h], i, j) == True:
                            adivinados += 1
                            print("Se ha seleccionado el número: ", posibles[i][j][h], " en la posición ", i, " - ", j)
                            sudoku[i][j] = posibles[i][j][h]
    return adivinados


def algorit_numeros_unicos(inicializa):
    total = 0
    sacados = -1

    while sacados != 0:

        # Por si no encuentra ninguno en la primera iteración no se quede en bucle infinito
        sacados = 0

        # Si inicializa es igual a 0, es que hay que anlizar sin crear la matriz de posibles valores
        # ya que si se viene de haber reducido candidatos, se perderia la reducción si se vuelve a crear

        if inicializa != 0:
            iniciar_posibles_valores()

        # Ya se va a analizar con lo que habrá que crear nuevamente por si se ha resuelto un nuevo valor
        inicializa = 1

        sacados = resolver_numeros_unicos()
        total = total + sacados

    if total > 0:
        imprimir_sudoku()

    return total


# Se busca aquellos valores iguales que son posibles en un mismo grupo, pero que solo están en una fila o columna
# ya que se podrán eliminar en el resto de grupos en esa misma fila o columna
def analisis_grupos():
    # Hay que buscar en los 9 grupos, que un valor se repita más de una vez. A partir de ahí, hay que ver
    # si se repite solo en la misma fila o en la misma columna

    candidatos_eliminados = 0

    for grupo_x in range(0, 3):

        for grupo_y in range(0, 3):

            indice_x = grupo_x * 3
            indice_y = grupo_y * 3

            for valor in range(1, 10):

                fila = -1
                columna = -1
                segundo_valor = 0
                analizado = 0
                pertenece_x = 0
                pertenece_y = 0

                for i in range(indice_x, indice_x + 3):

                    for j in range(indice_y, indice_y + 3):

                        if valor in posibles[i][j]:
                            # Primer valor encontrado en el grupo
                            if fila == -1:
                                fila = i
                                columna = j
                            else:
                                # Misma fila. Se descarta que sea de columna
                                if i == fila:
                                    columna = -2
                                    segundo_valor = 1
                                    analizado = valor
                                    pertenece_x = grupo_x
                                    pertenece_y = grupo_y
                                # Misma columna. Se descarta que sea de fila
                                elif j == columna:
                                    fila = -2
                                    segundo_valor = 1
                                    analizado = valor
                                    pertenece_x = grupo_x
                                    pertenece_y = grupo_y
                                # Estará en una diagonal y hay que descartarlo
                                else:
                                    segundo_valor = - 1;
                                    break;
                    if segundo_valor == -1:
                        break;

                if segundo_valor == 1:
                    # print (analizado, pertenece_x, pertenece_y, fila, columna)
                    # Hay que recorrer la fila menos su grupo para borrar todos los valores que se encuentren
                    if fila != -2:
                        if pertenece_y == 0:
                            for h in range(3, 9):
                                if analizado in posibles[fila][h]:
                                    posibles[fila][h].remove(analizado)
                                    candidatos_eliminados += 1
                        elif pertenece_y == 1:
                            for h in range(0, 3):
                                if analizado in posibles[fila][h]:
                                    posibles[fila][h].remove(analizado)
                                    candidatos_eliminados += 1
                            for h in range(6, 9):
                                if analizado in posibles[fila][h]:
                                    posibles[fila][h].remove(analizado)
                                    candidatos_eliminados += 1
                        else:
                            for h in range(0, 6):
                                if analizado in posibles[fila][h]:
                                    posibles[fila][h].remove(analizado)
                                    candidatos_eliminados += 1
                    else:
                        if pertenece_x == 0:
                            for h in range(3, 9):
                                if analizado in posibles[h][columna]:
                                    posibles[h][columna].remove(analizado)
                                    candidatos_eliminados += 1
                        elif pertenece_x == 1:
                            for h in range(0, 3):
                                if analizado in posibles[h][columna]:
                                    posibles[h][columna].remove(analizado)
                                    candidatos_eliminados += 1
                            for h in range(6, 9):
                                if analizado in posibles[h][columna]:
                                    posibles[h][columna].remove(analizado)
                                    candidatos_eliminados += 1
                        else:
                            for h in range(0, 6):
                                if analizado in posibles[h][columna]:
                                    posibles[h][columna].remove(analizado)
                                    candidatos_eliminados += 1
    if candidatos_eliminados > 0:
        print("Se han eliminado", candidatos_eliminados, "candidatos posibles")

    return candidatos_eliminados


def algorit_proyeccion_grupos():
    total = 0
    candidatos_eliminados = -1

    while candidatos_eliminados != 0:
        candidatos_eliminados = analisis_grupos()

        total = total + candidatos_eliminados

    return total

def calcula_cuadrante (fila, columna):
    return (fila // 3) * 3 + (columna // 3)


# Se quiere encontrar los pares iguales que no lo son en el mismo grupo,
# ya que esos dos valores no podrán darse en el resto de la fila o columna

# Con analizar los 2 primeros cuadrantes bastará, ya que encontrará si hay algun par igual en los restantes
def detecta_pares():
    candidatos_eliminados = 0

    for i in range(0, 6):

        for j in range(0, 6):

            if len(posibles[i][j]) == 2:

                # Se busca en la misma fila, pero en el siguiente grupo, a ver si existe la misma pareja
                for z in range(((j // 3) + 1) * 3, 8):

                    if posibles[i][j] == posibles[i][z]:
                        # Hay que eliminar esos valores de la pareja en el resto de la fila

                        for n in range(0, 9):
                            if (j != n) and (z != n):
                                for s in range(0, len(posibles[i][j])):

                                    if posibles[i][j][s] in posibles[i][n]:
                                        posibles[i][n].remove(posibles[i][j][s])
                                        candidatos_eliminados += 1

                # Se busca en la misma columna, pero en el siguiente grupo, a ver si existe la misma pareja
                for z in range(((i // 3) + 1) * 3, 8):
                    if posibles[i][j] == posibles[z][j]:
                        # Hay que eliminar esos valores de la pareja en el resto de la columna

                        for n in range(0, 9):
                            if (i != n) and (z != n):

                                for s in range(0, len(posibles[i][j])):

                                    if posibles[i][j][s] in posibles[n][j]:
                                        posibles[n][j].remove(posibles[i][j][s])
                                        candidatos_eliminados += 1

    if candidatos_eliminados > 0:
        print("Se han eliminado", candidatos_eliminados, "candidatos posibles")

    return candidatos_eliminados


def algorit_detecta_pares():
    total = 0
    candidatos_eliminados = -1

    while candidatos_eliminados != 0:
        candidatos_eliminados = detecta_pares()

        total = total + candidatos_eliminados

    return total


import time

start_time = time.time()

imprimir_sudoku()

# Primero se aplica el algoritmo de los numeros únicos
resueltos = algorit_numeros_unicos(1)

eliminados = -1
encontrados = -1

# Se iterara buscando eliminar candidatos y posteriormente evaluando si se pueden resolver valores hasta que
# no se consiga avanzar, y por lo tanto se espera que este resuelto

while (eliminados + encontrados) != 0:
    # Después se aplica la reduccion de posibilidades con los algoritmos creados

    eliminados = algorit_proyeccion_grupos() + algorit_detecta_pares()

    # Después de reducir los posibles se vuelve a resolver con los únicos por si se obtiene algun valor nuevo
    # pero sin crear de nuevo la matriz de posibilidades, ya que entonces no serviría haber usado
    # los algoritmos de reducción de candidatos

    encontrados = algorit_numeros_unicos(0)

if comprobar_resuelto() == 0:
    print("Resuelto! En %s segundos" % (time.time() - start_time))
else:
    print("Faltan", comprobar_resuelto(), "números por resolver")



imprimir_posibilidades()