from Process import Process

def startExecution():
    ...

def fillLlamada(processes):
    top = 0
    for i in range(len(processes)):
        if top > processes[i].call:
            top = processes[i].call

    # TODO: sort de processes.call y llenar la fila de "Llegada en"

    return

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

ENTRY_EXIT = 3          # tiempo predeterminado que demoran los procesos en pedir datos
S_O_USAGE = 1           # timepo que hace uso
QUANTUM = 2             # quantum de tiempo para Round Robin
all_Finished = False    # estara en FALSE hasta que todos los procesos finalicen
totalTime = 0           # tiempo total usado del Procesador

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
    ["Llamada: ", "      "]
]

# ---------- Matriz De Ejecicion ----------                                                                                                             me jijie

exeMatrix = [
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"],
    ["algo"]
]

# ---------- Comienzo Main ---------- 

showHeaderMatrix(HEADER_MATRIX, exeMatrix)

P1 = createProcess("P1")
print(P1)
P2 = createProcess("P2")
print(P2)
P3 = createProcess("P3")
print(P3)
P4 = createProcess("P4")
print(P4)

processes = [P1, P2, P3, P4]

fillLlamada(processes)
startExecution()