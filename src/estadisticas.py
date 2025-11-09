# ------------------------------------------------------
# — Estadísticas
# ------------------------------------------------------

def calcular_estadisticas(paises):
   
    if len(paises) == 0:
        return None
    
    max_poblacion = paises[0]["poblacion"]
    min_poblacion = paises[0]["poblacion"]
    max_pais = paises[0]["nombre"]
    min_pais = paises[0]["nombre"]

    suma_poblacion = 0
    suma_superficie = 0

    cant_america = 0
    cant_europa = 0
    cant_asia = 0
    cant_oceania = 0
    cant_africa = 0

    
    for pais in paises:
        
        if pais["poblacion"] > max_poblacion:
            max_poblacion = pais["poblacion"]
            max_pais = pais["nombre"]
        if pais["poblacion"] < min_poblacion:
            min_poblacion = pais["poblacion"]
            min_pais = pais["nombre"]

        
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        
        continente = pais["continente"].lower()
        if continente == "america" or continente == "américa":
            cant_america += 1
        elif continente == "europa":
            cant_europa += 1
        elif continente == "asia":
            cant_asia += 1
        elif continente == "oceania" or continente == "oseania" or continente == "oceanía":
            cant_oceania += 1
        elif continente == "africa" or continente == "áfrica":
            cant_africa += 1

   
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

   
    return {
        "max_pais": max_pais,
        "max_poblacion": max_poblacion,
        "min_pais": min_pais,
        "min_poblacion": min_poblacion,
        "promedio_poblacion": promedio_poblacion,
        "promedio_superficie": promedio_superficie,
        "cant_america": cant_america,
        "cant_europa": cant_europa,
        "cant_asia": cant_asia,
        "cant_oceania": cant_oceania,
        "cant_africa": cant_africa
    }


def mostrar_estadisticas(paises):
    
    datos = calcular_estadisticas(paises)
    if datos is None:
        print("- No hay países cargados para calcular estadísticas.")
        return
    
    print("=" * 40)
    print("         ESTADÍSTICAS GENERALES")
    print("=" * 40)
    print(f"País con mayor población: {datos['max_pais']} ({datos['max_poblacion']})")
    print(f"País con menor población: {datos['min_pais']} ({datos['min_poblacion']})")
    print(f"Promedio de población: {datos['promedio_poblacion']:.2f}")
    print(f"Promedio de superficie: {datos['promedio_superficie']:.2f} km²")
    print("\nCantidad de países por continente:")
    print(f"- América: {datos['cant_america']}")
    print(f"- Europa:  {datos['cant_europa']}")
    print(f"- Asia:    {datos['cant_asia']}")
    print(f"- Oceanía: {datos['cant_oceania']}")
    print(f"- África:  {datos['cant_africa']}")
    print("-" * 40)
