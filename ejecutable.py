import os
from clases import Detector, Radiacion, Sanador, Virus, Mutador
import sys

# FUNCION PARA VALIDAR LA MATRIZ CARGADA -------------------------------------------------------------
def validar_adn(matriz):
    # Verificar que la matriz tenga exactamente 6 elementos
    if len(matriz) != 6:
        return False
    # Verificar que cada elemento tenga 6 caracteres y solo contenga A, T, C, G
    for cadena in matriz:
        if len(cadena) != 6 or any(base not in "ATCG" for base in cadena):
            return False
    return True

# FUNCION PARA SOLICITAR LA CARGA DE LA MATRIZ -------------------------------------------------------------
def solicitar_adn():
    while True:
        # Solicitar datos
        entrada = input("""
    >> """)
        # Convertir los datos en una lista separada por comas
        matriz = [cadena.strip().upper() for cadena in entrada.split("-")]
        # Llamado a la funcion validar_adn
        if validar_adn(matriz):
            return matriz
        else:
            print("""
    Entrada inválida. Asegúrate de ingresar exactamente 6 cadenas de 6 caracteres formadas solo por A, T, C, y G.""")

# INICIO DEL PROGRAMA -----------------------------------------------------------------------------

def menu():
    #MENU --------------------------------------------------------------------------------------
    while True:
        print("""
    #######################################
                        
    # Opciones: 

    # 1- Detectar mutaciones
    # 2- Mutar ADN
    # 3- Sanar ADN
    # 4- Salir
    
    #######################################""")
        print("""
    Ingrese una opción:""")
        opcion = input("""
    >> """)
#     OPCIÓN DETECTAR MUTACIONES ------------------------------------------------------------------------
        if(opcion == "1"):
    # Si se detectan mutaciones
            if detector.detectar_mutantes():
                limpiar_consola()
                print("""
    ¡Mutaciones detectadas!""")   
    # Si no se detectan mutaciones 
            else:
                limpiar_consola()
                print("""
    No se detectaron mutaciones.""")
#     OPCIÓN MUTAR ADN --------------------------------------------------------------------------------------
        elif(opcion == "2"):
            limpiar_consola()
            print("""
    Posición inicial (fila, columna): """)
            posicion = tuple(map(int, input("""
    >> """).split(",")))
            limpiar_consola()
            print("""
    # Selecciona el tipo de mutador:
                    
    # 1- Radiación
    # 2- Virus
                    
    #Elige una opción:
                    """)
            tipo = input("""
    >> """)
            limpiar_consola()
            print("""
    # Elige la base nitrogenada (A, T, C, G): """)

            base = input("""
    >> """).upper()
            mutador = Mutador(base,posicion,matriz_adn)
    # OPCION RADIACION
            if tipo == "1":
                limpiar_consola()
                print("""
    Orientación (H para horizontal, V para vertical): """)
                orientacion = input("""
    >> """).upper()
                radiacion = Radiacion(base, posicion, matriz_adn ,orientacion)
                matriz_mutada = radiacion.crear_mutante()
    # OPCION VIRUS
            elif tipo == "2":
                limpiar_consola()
                print("""
    Orientación de diagonal (N (Normal) / I (Invertida)): """)
                tipo_diagonal = input("""
    >> """).upper()
                limpiar_consola()
                virus = Virus(base, posicion, matriz_adn , tipo_diagonal)
                matriz_mutada = virus.crear_mutante()
            print("""
    ADN después de la mutación:
                """)
            detector.matriz_adn = matriz_mutada
            mostrar_matriz(matriz_mutada)
            volver_menú()
        
#     OPCIÓN SANAR ADN --------------------------------------------------------------------------------------
        elif(opcion == "3"):
            sanador = Sanador(detector)
            limpiar_consola()
            matriz_sana = sanador.sanar_mutantes()
            mostrar_matriz(matriz_sana)
            volver_menú()
            
#     OPCIÓN SALIR --------------------------------------------------------------------------------------
        elif(opcion == "4"):
            limpiar_consola()    
            sys.exit(f"""
                        
    Finalizando. ¡Hasta pronto!
    
                    """)
        else:
            limpiar_consola()
            print("""
    Opción invalida. Intente de nuevo.
    """)
  
#----------------------------------------------------- Espacio para funciones extra que usaremos ----------------------------------------------------- 

#Función para limpiar la consola
def limpiar_consola():
   
    os.system('clear' if os.name == 'posix' else 'cls')

#Función para mostrar lo obtenido en formato matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print("\t" + " ".join(fila))


#Funciones para reintento 
 
def volver_menú():
    while(True):
        print("""
    ¿Qué desea hacer?
        (1) Volver al menu
        (0) Salir del programa""")
        opcion = input("""
    >> """)
        if(opcion == "1"):
            limpiar_consola()
            menu()
            
        elif(opcion == "0"):
            limpiar_consola()
            sys.exit(f"""
                        
    Finalizando. ¡Hasta pronto!
    
                    """)          
        else:
            limpiar_consola()
            print("""
    Opción inválida""")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# MAIN --------------------------------------------------------------------------------------         
if __name__ == "__main__":
    limpiar_consola()
# PORTADA DEL GLOBAL --------------------------------------------------------------------------------------
    print("""
    ######## 🐍 GLOBAL PYTHON 🐍 #########

    ¡Bienvenidos! 
        
    Ingresa la matriz de ADN (6 cadenas de 6 caracteres separados por '-', formadas por A, T, C, G):\n """)
    matriz_adn = solicitar_adn()
    detector = Detector(matriz_adn)
    limpiar_consola()
    print("""
    Matriz de ADN cargada...
    """)
    mostrar_matriz(matriz_adn)  
    menu()
