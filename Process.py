class Process:
        
    def __init__(self, name = None, call = None, gusts = None, timeExecuted = None): # constructor
        # el self. es el this. en Java
        self.name = name # P1 P2 ...
        self.call = call # tiempo de llegada
        self.gusts = gusts # gusts = rafagas
        self.timeExecuted = 0 # es el tiempo total que lleva ejecutado
        