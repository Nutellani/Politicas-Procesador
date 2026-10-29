from Process import Process

def showHeaderMatrix(HEADER_MATRIX, exeMatrix):
    
    # para concatenar automaticamente en Python es...
    # for i in range(len(HEADER_MATRIX)):
    #     filaPrint = [HEADER_MATRIX[i], exeMatrix[i]]
    #     print(filaPrint)
        
    # que es lo mismo que hacer...
    
    matrizPrint = []
    
    for i in range(len(matrizPrint)):
        print(matrizPrint[i])
    
    for i in range(len(HEADER_MATRIX)):
        fila = []
        for j in range(len(HEADER_MATRIX[i])):
            fila.append(HEADER_MATRIX[i][j])
            
        for j in range(len(exeMatrix[i])):
            fila.append(exeMatrix[i][j])
            
        matrizPrint.append(fila)
    

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

ENTRY_EXIT = 30     # tiempo predeterminado que demoran los procesos en pedir datos
S_O_USAGE = 10      # timepo que hace uso
QUANTUM = 20        # quantum de tiempo para Round Robin
totalTime = 0       # tiempo total usado del Procesador

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

# ---------- Matriz De Ejecicion ---------- 

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
