from Process import Process


def startExecution():
    # TODO-> comienzo de discriminacion de procesos ...
    ...


def sortCalls(processes):
    calls = [p1.call, p2.call, p3.call, p4.call]
    callsOrdened = sorted(calls)
    return callsOrdened

def fillLlamada(processes, exeMatrix):

    calls = [p1.call, p2.call, p3.call, p4.call]
    calls = sorted(calls)

    # calls[3] -> es el ultimo valor a rellenar en Llamada: y el +1 es porque se empieza del cero
    for i in range(calls[3] + 1): 

        exeMatrix[12].append("     ") # espacio justo para por ej: " 3P1 "
        if (i + 1) == (calls[0]):
            exeMatrix[12][i].insert(calls[0]) # TODO-> ver como concatenar lo con el espacio
            calls.pop(0)

    print(calls)

    # TODO-> sort de processes.call y llenar la fila de "Llegada en"

def showHeaderMatrix(HEADER_MATRIX, exeMatrix):

    # para insertar ambas LISTAS dentro de otra es...
    for i in range(len(HEADER_MATRIX)):
        filaPrint = [HEADER_MATRIX[i], exeMatrix[i]]
        print(filaPrint)

def createProcess(name):

    newProcess = Process()

    print("\nVa a ingresar datos del proceso " + name)
    newProcess.name = name
    newProcess.call = int(input("En que quantum de tiempo se ingresa este proceso?: "))
    newProcess.gusts = ask4Gusts()

    return newProcess

def ask4Gusts():
    gusts = []

    ammount = int(input("De cuántas ráfagas es este proceso?: "))

    for i in range(ammount):
        valor = int(input(f"Ingresa el valor de la ráfaga {i + 1}: "))
        gusts.append(valor)

    return gusts

# ---------- Variables ----------

ENTRY_EXIT = 3  # tiempo predeterminado que demoran los procesos en pedir datos
S_O_USAGE = 1  # timepo que hace uso
QUANTUM = 2  # quantum de tiempo para Round Robin
all_Finished = False  # estara en FALSE hasta que todos los procesos finalicen
totalTime = 0  # tiempo total usado del Procesador

# ---------- Orden Prioridades ----------

# 1_ Procesador Ocupado - S.O. Ocupado
#                       -> P -> T -> Bloqueado
# 2_ Hay Nuevo?
# 3_ Hay Bloq?
# 4_ Listo -> Exe

# ---------- Matriz CONSTANTE ----------

HEADER_MATRIX = [
    ["Terminado", "      "],
    ["    B    ", " P1   "],
    ["Bloqueado", " P2   "],
    ["    B    ", " P3   "],
    ["    B    ", " P2   "],
    ["         ", " Exe  "],
    ["    L    ", " P1   "],
    ["  Listo  ", " P2   "],
    ["    L    ", " P3   "],
    ["    L    ", " P4   "],
    ["         ", " S.O. "],
    [" Tiempo  ", "      "],
    ["Llamada: ", "      "],
]

# ---------- Matriz De Ejecicion ----------                                                                                                             me jijié

exeMatrix = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    ["0    "],
    [],
]

# ---------- Comienzo Main ----------

# P1 = createProcess("P1")
# print(P1)
# P2 = createProcess("P2")
# print(P2)
# P3 = createProcess("P3")
# print(P3)
# P4 = createProcess("P4")
# print(P4)

p1 = Process("P1", 1, [2, 3])
p2 = Process("P2", 2, [3, 1, 2])
p3 = Process("P3", 4, [2, 2])
p4 = Process("P4", 6, [3, 1])

processes = [p1, p2, p3, p4]

fillLlamada(processes, exeMatrix)
startExecution()

showHeaderMatrix(HEADER_MATRIX, exeMatrix)