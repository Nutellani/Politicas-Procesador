import textwrap

class Process:
        
    def __init__(self, name = None, call = None, gusts = None, timeExecuted = None): # constructor
        # el self. es el this. en Java
        self.name = name # P1 P2 ...
        self.call = call # tiempo de llegada
        self.gusts = gusts # gusts = rafagas
        self.timeExecuted = 0 # es el tiempo total que lleva ejecutado
        
    def __str__(self):
        
        #   esto del textwrap.dedent es un print pero que te permite identarlo de esta manera
        return textwrap.dedent(f"""
            Nombre: {self.name}
            Llegada: {self.call}
            Ráfagas: {self.gusts}
            Tiempo Ejecutado: {self.timeExecuted}
        """)