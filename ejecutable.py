import funciones_extra
from clases import Detector, Radiacion, Sanador, Virus, Mutador
import sys

# INICIO DEL PROGRAMA -----------------------------------------------------------------------------
def main():
    # FUNCION PARA VALIDAR LA MATRIZ CARGADA
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
                print("Entrada inválida. Asegúrate de ingresar exactamente 6 cadenas de 6 caracteres formadas solo por A, T, C, y G.")

# PORTADA DEL GLOBAL --------------------------------------------------------------------------------------
    print("""
    ######## 🐍 GLOBAL PYTHON 🐍 #########

    ¡Bienvenidos! 
        
    Ingresa la matriz de ADN (6 cadenas de 6 caracteres separados por '-', formadas por A, T, C, G):\n """)

    matriz_adn = solicitar_adn()
    detector = Detector(matriz_adn)
    funciones_extra.limpiar_consola()  

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
    >>""")
#     OPCIÓN DETECTAR MUTACIONES ------------------------------------------------------------------------
        if(opcion == "1"):
    # Si se detectan mutaciones
            if detector.detectar_mutantes():
                funciones_extra.limpiar_consola()
                print("""
    ¡Mutaciones detectadas!""")   
    # Si no se detectan mutaciones 
            else:
                funciones_extra.limpiar_consola()
                print("""
    No se detectaron mutaciones.""")
#     OPCIÓN MUTAR ADN --------------------------------------------------------------------------------------
        elif(opcion == "2"):
            funciones_extra.limpiar_consola()
            print("""
    Posición inicial (fila, columna): """)
            posicion = tuple(map(int, input("""
    >>""").split(",")))
            funciones_extra.limpiar_consola()
            print("""
    # Selecciona el tipo de mutador:
                    
    # 1- Radiación
    # 2- Virus
                    
    #Elige una opción:
                    """)
            tipo = input("""
    >>""")
            funciones_extra.limpiar_consola()
            print("""
    # Elige la base nitrogenada (A, T, C, G): """)

            base = input("""
    >>""").upper()
            mutador = Mutador(base,posicion,matriz_adn)
    # OPCION RADIACION
            if tipo == "1":
                funciones_extra.limpiar_consola()
                print("""
    Orientación (H para horizontal, V para vertical): """)
                orientacion = input("""
    >>""").upper()
                radiacion = Radiacion(base, posicion, matriz_adn ,orientacion)
                matriz_mutada = radiacion.crear_mutante()
    # OPCION VIRUS
            elif tipo == "2":
                funciones_extra.limpiar_consola()
                print("""
    Orientación de diagonal (N (Normal) / I (Invertida)): """)
                tipo_diagonal = input("""
    >>""").upper()
                funciones_extra.limpiar_consola()
                virus = Virus(base, posicion, matriz_adn , tipo_diagonal)
                matriz_mutada = virus.crear_mutante()
            # if(matriz_adn == matriz_mutada):
            #     main()
            
            print("""
    ADN después de la mutación:
                """)
            detector.matriz_adn = matriz_mutada
            funciones_extra.mostrar_matriz(matriz_mutada)
        
#     OPCIÓN SANAR ADN --------------------------------------------------------------------------------------
        elif(opcion == "3"):
            sanador = Sanador(detector)
            funciones_extra.limpiar_consola()
            matriz_sana = sanador.sanar_mutantes()
            funciones_extra.mostrar_matriz(matriz_sana)
            
#     OPCIÓN SALIR --------------------------------------------------------------------------------------
        elif(opcion == "4"):    
            sys.exit(f"""

    {funciones_extra.mostrar_matriz(detector.matriz_adn)}
                        
    Finalizando. ¡Hasta pronto!
                    """)
        else:
            funciones_extra.limpiar_consola()
            print("""
    Opción invalida. Intente de nuevo.
    """)
        
# MAIN --------------------------------------------------------------------------------------         
if __name__ == "__main__":
    funciones_extra.limpiar_consola()
    main()
