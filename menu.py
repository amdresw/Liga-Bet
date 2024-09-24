import os

def MostrarMenu():
    os.system('cls')
    titulo= '''
        *************************
        *** LIGA BETPLAY MENU ***
        *************************
'''
    opciones = "1. Agregar equipo\n2. Registar plantel\n3. Programar partido\n4. Registar resultado\n5. Salir"
    print(opciones)