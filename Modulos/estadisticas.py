from equipos import equipos

def registrar_estadisticas_equipo():
    try:
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        if nombre_equipo not in equipos:
            raise ValueError("El equipo no está registrado.")
        goles_a_favor = int(input("Ingrese los goles a favor del equipo: "))
        goles_en_contra = int(input("Ingrese los goles en contra del equipo: "))
        equipos[nombre_equipo]['goles_a_favor'] += goles_a_favor
        equipos[nombre_equipo]['goles_en_contra'] += goles_en_contra
        print(f"Estadísticas actualizadas para el equipo '{nombre_equipo}'.")
    except ValueError as e:
        print("Error:", e)

def registrar_estadisticas_jugador():
    try:
        nombre_equipo = input("Ingrese el nombre del equipo al que pertenece el jugador: ")
        if nombre_equipo not in equipos:
            raise ValueError("El equipo no está registrado.")
        nombre_jugador = input("Ingrese el nombre del jugador: ")
        jugadores = equipos[nombre_equipo]['jugadores']
        jugador = next((j for j in jugadores if j['nombre'] == nombre_jugador), None)
        if jugador is None:
            raise ValueError("El jugador no está registrado en este equipo.")
        
        goles = int(input("Ingrese los goles anotados por el jugador: "))
        tarjetas_amarillas = int(input("Ingrese las tarjetas amarillas recibidas: "))
        tarjetas_rojas = int(input("Ingrese las tarjetas rojas recibidas: "))
        faltas = int(input("Ingrese las faltas cometidas: "))

        jugador['goles_anotados'] += goles
        jugador['tarjetas_amarillas'] += tarjetas_amarillas
        jugador['tarjetas_rojas'] += tarjetas_rojas
        jugador['faltas_cometidas'] += faltas

        print(f"Estadísticas actualizadas para el jugador '{nombre_jugador}'.")
    except ValueError as e:
        print("Error:", e)

def jugador_mas_faltas():
    jugadores = [j for equipo in equipos.values() for j in equipo['jugadores']]
    jugador = max(jugadores, key=lambda x: x['faltas_cometidas'], default=None)
    if jugador:
        print(f"El jugador con más faltas cometidas es '{jugador['nombre']}' con {jugador['faltas_cometidas']} faltas.")
    else:
        print("No hay jugadores registrados.")

def jugador_mas_tarjetas_amarillas():
    jugadores = [j for equipo in equipos.values() for j in equipo['jugadores']]
    jugador = max(jugadores, key=lambda x: x['tarjetas_amarillas'], default=None)
    if jugador:
        print(f"El jugador con más tarjetas amarillas es '{jugador['nombre']}' con {jugador['tarjetas_amarillas']} tarjetas.")
    else:
        print("No hay jugadores registrados.")
