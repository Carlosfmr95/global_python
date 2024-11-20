import os

#Espacio para funciones extra que usaremos 

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
    
        [1] Volver al menu
        [0] Salir del programa
              
              """)
        reintentar = input("""
    >>""")
        if(reintentar == "1"):
            limpiar_consola()
            
        elif(reintentar == "0"):
            limpiar_consola()           
        else:
            limpiar_consola()
            print("""
    Opción inválida""")


#CCCTCC-AAGCAC-GCCGTC-TGTTCA-TCTTTA-AAGTAG 