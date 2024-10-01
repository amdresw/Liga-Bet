from equipos import equipos

def registrar_plantel():
    try:
        nombre_equipo = input("Ingrese el nombre del equipo al que pertenece el plantel: ")
        if nombre_equipo not in equipos:
            raise ValueError("El equipo no está registrado.")
        
        tipo = input("¿Desea registrar un Jugador o un Cuerpo Técnico? (J/C): ").lower()
        if tipo == 'j':
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            equipos[nombre_equipo]['jugadores'].append({
                'nombre': nombre_jugador,
                'goles_anotados': 0,
                'tarjetas_amarillas': 0,
                'tarjetas_rojas': 0,
                'faltas_cometidas': 0
            })
            print(f"Jugador '{nombre_jugador}' registrado en el equipo '{nombre_equipo}'.")
        elif tipo == 'c':
            nombre_tecnico = input("Ingrese el nombre del miembro del cuerpo técnico: ")
            rol = input("Ingrese el rol del cuerpo técnico (Técnico, Asistente, etc.): ")
            equipos[nombre_equipo]['cuerpo_tecnico'].append({
                'nombre': nombre_tecnico,
                'rol': rol
            })
            print(f"Cuerpo técnico '{nombre_tecnico}' con rol '{rol}' registrado en el equipo '{nombre_equipo}'.")
        else:
            print("Opción inválida.")
    except ValueError as e:
        print(e)
