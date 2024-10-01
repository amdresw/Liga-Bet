equipos = {}

def registrar_equipo():
    try:
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        if nombre_equipo in equipos:
            raise ValueError("El equipo ya está registrado.")
        equipos[nombre_equipo] = {
            'jugadores': [],
            'cuerpo_tecnico': [],
            'goles_a_favor': 0,
            'goles_en_contra': 0,
            'posicion': 0
        }
        print(f"Equipo '{nombre_equipo}' registrado con éxito.")
    except ValueError as e:
        print(e)

def equipo_mas_goles():
    equipo = max(equipos.items(), key=lambda x: x[1]['goles_a_favor'], default=None)
    if equipo:
        print(f"El equipo con más goles a favor es '{equipo[0]}' con {equipo[1]['goles_a_favor']} goles.")
    else:
        print("No hay equipos registrados.")

def equipo_mas_goles_en_contra():
    equipo = max(equipos.items(), key=lambda x: x[1]['goles_en_contra'], default=None)
    if equipo:
        print(f"El equipo con más goles en contra es '{equipo[0]}' con {equipo[1]['goles_en_contra']} goles en contra.")
    else:
        print("No hay equipos registrados.")

def equipo_ultimo_puesto():
    equipo = min(equipos.items(), key=lambda x: x[1]['posicion'], default=None)
    if equipo:
        print(f"El equipo en el último puesto es '{equipo[0]}' en la posición {equipo[1]['posicion']}.")
    else:
        print("No hay equipos registrados.")
