from Process import Process

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
        valor = input(f"Ingresa el valor de la ráfaga {i + 1}: ")
        gusts.append(valor)
        
    return gusts
     

ENTRY_EXIT = 30     # tiempo predeterminado que demoran los procesos en pedir datos
S_O_USAGE = 10      # timepo que hace uso
QUANTUM = 20        # quantum de tiempo para Round Robin

# ---------- Comienzo Main ---------- 


P1 = createProcess("P1")
print(P1)
P2 = createProcess("P2")
print(P2)
P3 = createProcess("P3")
print(P3)
P4 = createProcess("P4")
print(P4)

# amountGusts = int(input("Cuántas ráfagas tiene el Proceso P1 ?? "))
# for i in range(0, amountGusts):
#     print(p1.gusts[i])
