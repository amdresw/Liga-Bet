import sys
from equipos import registrar_equipo, equipo_mas_goles, equipo_mas_goles_en_contra, equipo_ultimo_puesto
from plantel import registrar_plantel
from estadisticas import registrar_estadisticas_equipo, registrar_estadisticas_jugador, jugador_mas_faltas, jugador_mas_tarjetas_amarillas

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Equipo")
        print("2. Registrar Plantel de Equipo")
        print("3. Registrar Estadísticas de Equipo")
        print("4. Registrar Estadísticas de Jugador")
        print("5. Mostrar Equipo con Más Goles a Favor")
        print("6. Mostrar Equipo con Más Goles en Contra")
        print("7. Mostrar Equipo en el Último Puesto")
        print("8. Mostrar Jugador con Más Faltas Cometidas")
        print("9. Mostrar Jugador con Más Tarjetas Amarillas")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_equipo()
        elif opcion == '2':
            registrar_plantel()
        elif opcion == '3':
            registrar_estadisticas_equipo()
        elif opcion == '4':
            registrar_estadisticas_jugador()
        elif opcion == '5':
            equipo_mas_goles()
        elif opcion == '6':
            equipo_mas_goles_en_contra()
        elif opcion == '7':
            equipo_ultimo_puesto()
        elif opcion == '8':
            jugador_mas_faltas()
        elif opcion == '9':
            jugador_mas_tarjetas_amarillas()
        elif opcion == '10':
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.")
