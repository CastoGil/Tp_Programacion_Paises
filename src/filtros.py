# ------------------------------------------------------
# — Filtrar países 
# ------------------------------------------------------
from validaciones import validar_texto_no_vacio, validar_entero_positivo

def filtrar_paises(paises, tipo):
    filtrados = []

    
    if tipo == "continente":
        tipo_continente = input("Elija por cuál continente quiere filtrar (América, Europa, Asia, Oceanía o África): ").strip()

        while not validar_texto_no_vacio(tipo_continente):
            tipo_continente = input("Elija por cuál continente quiere filtrar (America, Europa, Asia, Oceania o Africa): ").strip()

        tipo_continente = tipo_continente.lower()

        i = 0
        while i < len(paises):
            continente = paises[i]["continente"].lower()

            
            if (
                (tipo_continente in ["america", "américa"] and continente in ["america", "américa"]) or
                (tipo_continente in ["europa"] and continente in ["europa"]) or
                (tipo_continente in ["asia"] and continente in ["asia"]) or
                (tipo_continente in ["oceania", "oceanía", "oseania"] and continente in ["oceania", "oceanía", "oseania"]) or
                (tipo_continente in ["africa", "áfrica"] and continente in ["africa", "áfrica"])
            ):
                filtrados.append(paises[i])
            i += 1

    
    elif tipo == "poblacion":
        minimo_poblacion = input("Ingrese el valor mínimo de población: ").strip()
        while not validar_entero_positivo(minimo_poblacion):
            minimo_poblacion = input("Ingrese el valor mínimo de población: ").strip()

        maximo_poblacion = input("Ingrese el valor máximo de población: ").strip()
        while not validar_entero_positivo(maximo_poblacion):
            maximo_poblacion = input("Ingrese el valor máximo de población: ").strip()

        minimo_poblacion = int(minimo_poblacion)
        maximo_poblacion = int(maximo_poblacion)

        # Intercambiar si el usuario los ingresa al revés
        if minimo_poblacion > maximo_poblacion:
            aux = minimo_poblacion
            minimo_poblacion = maximo_poblacion
            maximo_poblacion = aux

        for pais in paises:
            if pais["poblacion"] >= minimo_poblacion and pais["poblacion"] <= maximo_poblacion:
                filtrados.append(pais)

  
    elif tipo == "superficie":
        minimo_superficie = input("Ingrese el valor mínimo de superficie (km²): ").strip()
        while not validar_entero_positivo(minimo_superficie):
            minimo_superficie = input("Ingrese el valor mínimo de superficie (km²): ").strip()

        maximo_superficie = input("Ingrese el valor máximo de superficie (km²): ").strip()
        while not validar_entero_positivo(maximo_superficie):
            maximo_superficie = input("Ingrese el valor máximo de superficie (km²): ").strip()

        minimo_superficie = int(minimo_superficie)
        maximo_superficie = int(maximo_superficie)

        # Intercambiar si el usuario los ingresa al revés
        if minimo_superficie > maximo_superficie:
            aux = minimo_superficie
            minimo_superficie = maximo_superficie
            maximo_superficie = aux

        for pais in paises:
            if pais["superficie"] >= minimo_superficie and pais["superficie"] <= maximo_superficie:
                filtrados.append(pais)

    
    if len(filtrados) == 0:
        print("\n- No se encontraron países con esos criterios.")
    else:
        print(f"\n{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
        print("-" * 70)
        for pais in filtrados:
            print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")
        print("-" * 70)
        print(f"Total de países encontrados: {len(filtrados)}\n")



# ------------------------------------------------------
# Menú de filtros
# ------------------------------------------------------
def filtrar_menu(paises):
    print("=" * 40)
    print("         FILTRAR PAÍSES")
    print("=" * 40)
    print("""
    1. Por continente 
    2. Por rango de población
    3. Por rango de superficie
    """)

    opcion = input("Seleccione una opción (1-3): ").strip()
    while opcion not in ["1", "2", "3"]:
        print("- Opción inválida. Intente nuevamente.")
        opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        filtrar_paises(paises, "continente")
    elif opcion == "2":
        filtrar_paises(paises, "poblacion")
    elif opcion == "3":
        filtrar_paises(paises, "superficie")
