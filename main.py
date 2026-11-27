from Process import Process

def startExecution():
    # TODO-> comienzo de discriminacion de procesos ...
    ...
    
def fillLlamada(exeMatrix): # TODO->

    aux = 0

    # calls[3] -> es el ultimo valor a rellenar en Llamada: y el +1 es porque se empieza del cero
    for i in range(processes[3].call + 1):

        exeMatrix[INDEX_CALL_IN].append("     ") # espacio justo para por ej: " 3P1 "
        if i == processes[aux].call:

            exeMatrix[INDEX_CALL_IN][i] = f"  {processes[aux].call:<3}"
            aux += 1
            
    # TODO-> ver como concatenar lo con el espacio            


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
total_time_executed = 0  # tiempo total usado del Procesador

INDEX_CALL_IN = 12

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
    ["0    "], # con esos espacios tienen que quedar
    [],
]

# ---------- Comienzo Main ----------

# p1 = createProcess("P1")
# print(p1)
# p2 = createProcess("P2")
# print(p2)
# p3 = createProcess("P3")
# print(p3)
# p4 = createProcess("P4")
# print(p4)

p1 = Process("P1", 1, [2, 3])
p2 = Process("P2", 2, [3, 1, 2])
p3 = Process("P3", 4, [2, 2])
p4 = Process("P4", 6, [3, 1])

processes = sorted([p1, p2, p3, p4], key=lambda p:p.call )

fillLlamada(exeMatrix)

startExecution()

showHeaderMatrix(HEADER_MATRIX, exeMatrix)