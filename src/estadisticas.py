# ------------------------------------------------------
# — Estadisiticas
# ------------------------------------------------------


def calcular_estadisticas(paises):
   

    max_poblacion = paises[0]["poblacion"]
    menor_poblacion = paises[0]["poblacion"]
    suma_poblacion = 0
    suma_superficie = 0

    cant_america =0 
    cant_europa =0 
    cant_asia = 0
    cant_oseania = 0
    cant_africa = 0

    for pais in paises:
        if pais["poblacion"] > max_poblacion:
            max_poblacion = pais["poblacion"]
        if pais["poblacion"] < menor_poblacion:
            menor_poblacion = pais["poblacion"]

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"].lower()
        if continente == "américa":
            cant_america += 1
        elif continente == "europa":
            cant_europa += 1
        elif continente == "asia":
            cant_asia += 1
        elif continente == "oceania":
            cant_oseania += 1
        elif continente == "áfrica":
            cant_africa += 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    return {
        "max_poblacion": max_poblacion,
        "menor_poblacion": menor_poblacion,
        "promedio_poblacion": promedio_poblacion,
        "promedio_superficie": promedio_superficie,
        "cant_america": cant_america,
        "cant_europa": cant_europa,
        "cant_asia": cant_asia,
        "cant_oseania": cant_oseania,
        "cant_africa": cant_africa
    }


def mostrar_estadisticas(paises):
    datos = calcular_estadisticas(paises)
    print(f"""
    🌍 País con mayor población: {datos['max_poblacion']}
    🏳️ País con menor población: {datos['menor_poblacion']}
    📊 Promedio de población: {round(datos['promedio_poblacion'], 2)}
    📐 Promedio de superficie: {round(datos['promedio_superficie'], 2)} km²

    Cantidad de países por continente:
    - América: {datos['cant_america']}
    - Europa: {datos['cant_europa']}
    - Asia: {datos['cant_asia']}
    - Oceanía: {datos['cant_oseania']}
    - África: {datos['cant_africa']}
    """)