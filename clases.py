import random

# -------------------------------------------------------- CLASE DETECTOR --------------------------------------------------------------------

class Detector:                                                                                     
    def __init__(self, matriz_adn):                                                                 # Costructor de la clase
        self.matriz_adn = matriz_adn
        self.mutante_encontrado = False
    
    def detectar_mutantes(self):
        if self.mutacion_horizontal() or self.mutacion_vertical() or self.mutacion_diagonal():
            self.mutante_encontrado = True
            return True
        return False

    def mutacion_horizontal(self):
        for fila in self.matriz_adn:
            for i in range(len(fila) - 3):
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    return True
        return False

    def mutacion_vertical(self):
        columnas = len(self.matriz_adn[0])  
        for col in range(columnas):
            for fila in range(len(self.matriz_adn) - 3):
                if (
                    self.matriz_adn[fila][col] == self.matriz_adn[fila+1][col] ==
                    self.matriz_adn[fila+2][col] == self.matriz_adn[fila+3][col]
                ):
                    return True
        return False      

    def mutacion_diagonal(self):
        filas = len(self.matriz_adn)
        columnas = len(self.matriz_adn[0])
        for fila in range(filas - 3):
            for col in range(columnas - 3):
                if (
                    self.matriz_adn[fila][col] == self.matriz_adn[fila+1][col+1] ==
                    self.matriz_adn[fila+2][col+2] == self.matriz_adn[fila+3][col+3]
                ):
                    return True
        for fila in range(filas - 3):
            for col in range(3, columnas):
                if (
                    self.matriz_adn[fila][col] == self.matriz_adn[fila+1][col-1] ==
                    self.matriz_adn[fila+2][col-2] == self.matriz_adn[fila+3][col-3]
                ):
                    return True
        return False
   
# -------------------------------------------------------- CLASE MUTADOR --------------------------------------------------------------------

class Mutador:
    def __init__(self, base_nitrogenada, posicion_inicial, matriz_adn):     # Costructor de la clase
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial
        self.matriz_adn = matriz_adn

    def crear_mutante(self):
        pass


# -------------------------------------------------------- CLASE RADIACION (Hija de Mutador) ------------------------------------------------
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, posicion_inicial, matriz_adn , orientacion):       # Costructor de la clase
        super().__init__(base_nitrogenada, posicion_inicial, matriz_adn)
        self.orientacion = orientacion

    def crear_mutante(self):
        try:
            if self.orientacion == "H":
                fila, col = self.posicion_inicial
                fila_lista = list(self.matriz_adn[fila])            # Convertir a lista
                for i in range(4):                                  # Modificar 4 caracteres
                    fila_lista[col + i] = self.base_nitrogenada
                self.matriz_adn[fila] = "".join(fila_lista)         # Actualizar la matriz
            elif self.orientacion == "V":
                fila, col = self.posicion_inicial
                for i in range(4):
                    fila_lista = list(self.matriz_adn[fila + i])    # Convertir fila a lista
                    fila_lista[col] = self.base_nitrogenada
                    self.matriz_adn[fila + i] = "".join(fila_lista) # Actualizar la matriz
            return self.matriz_adn
        except IndexError:
            
            print(""" 
    Error: Posición fuera de rango.""")
            return self.matriz_adn
            
# -------------------------------------------------------- CLASE VIRUS (Hija de Mutador) ----------------------------------------------------------

class Virus(Mutador):
    def __init__(self, base_nitrogenada, posicion_inicial, matriz_adn, tipo_diagonal):  # Costructor de la clase
        super().__init__(base_nitrogenada, posicion_inicial, matriz_adn)
        self.tipo_diagonal = tipo_diagonal                                              # "N" para diagonal normal, "I" para inversa

    def crear_mutante(self):
        try:
            fila, col = self.posicion_inicial
            matriz_mutada = [list(fila) for fila in self.matriz_adn]                    # Convertir matriz a lista de listas
            if self.tipo_diagonal == "N":                                               # Diagonal normal \
                for i in range(4):
                    matriz_mutada[fila + i][col + i] = self.base_nitrogenada
            elif self.tipo_diagonal == "I":                                              # Diagonal inversa /
                for i in range(4):
                    matriz_mutada[fila + i][col - i] = self.base_nitrogenada
                                                                                        # Convertir de nuevo a formato original
            self.matriz_adn = ["".join(fila) for fila in matriz_mutada]
            return self.matriz_adn
        except IndexError:
            print("""
    Error: Posición fuera de rango o diagonal no válida.""")
            return self.matriz_adn       
        
# ----------------------------------------- CLASE SANADOR  ----------------------------------------------------------------
class Sanador:
    def __init__(self, detector):                                   # Costructor de la clase
        self.detector = detector
        self.matriz_sana = []

    def sanar_mutantes(self):
        if self.detector.detectar_mutantes():
            print("""
    Mutantes detectados. Sanando ADN...""")
            self.detector.matriz_adn = self.generar_adn_sano()
            self.matriz_sana = self.detector.matriz_adn
            print("""
    ADN sanado.

    Matriz sana:
                  """)
            return self.matriz_sana
        else:
            print("""
    No se detectaron mutaciones.

    La matriz es:
                  """)
            return self.detector.matriz_adn
        
    def generar_adn_sano(self):
        filas, columnas = 6, 6
        bases = "ATCG"

        def es_valida(matriz, fila, columna, base):
            if columna >= 3 and all(matriz[fila][columna - i] == base for i in range(1, 4)):                                # Valida horizontalmente 
                return False
            if fila >= 3 and all(matriz[fila - i][columna] == base for i in range(1, 4)):                                   # Valida verticalmente 
                return False
            if fila >= 3 and columna >= 3 and all(matriz[fila - i][columna - i] == base for i in range(1, 4)):              # Valida diagonal principal
                return False
            if fila >= 3 and columna < columnas - 3 and all(matriz[fila - i][columna + i] == base for i in range(1, 4)):    # Valida diagonal inversa
                return False
            return True

                                                                                                                           
        matriz = [["" for _ in range(columnas)] for _ in range(filas)]                                                  
        for fila in range(filas):
            for columna in range(columnas):
                base = random.choice(bases)
                while not es_valida(matriz, fila, columna, base):
                    base = random.choice(bases)
                matriz[fila][columna] = base
        return matriz

    
