# ------------------------------------------------------
# — Filtrar países 
# ------------------------------------------------------
from validaciones import validar_texto_no_vacio, validar_entero_positivo

def filtrar_paises(paises, tipo):
    filtrados = []
    if tipo == "continente":
        tipo_continente = input("Elija por cual continente quiere filtrar (America, Europa, Asia, Oseania o Africa): ").strip()
        while not validar_texto_no_vacio(tipo_continente):
            tipo_continente = input("Elija por cual continente quiere filtrar (America, Europa, Asia, Oseania o Africa): ").strip()


        for pais in paises:
            if pais["continente"].lower() == tipo_continente.lower():
                filtrados.append(pais)
        
        if len(filtrados) == 0:
            print("No se encontraron países con esos criterios.")
        else:
            print(f"\n{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
            print("-" * 70)
        for pais in filtrados:
            print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")


    elif tipo == "poblacion": 
        maximo_poblacion = input("Elija el criterio maximo de poblacion: ")
        minimo_poblacion = input("Elija el criterio minimo de poblacion: ")

        while not validar_entero_positivo(maximo_poblacion):
            maximo_poblacion = input("Elija el criterio maximo de poblacion: ")
        while not validar_entero_positivo(minimo_poblacion):
            minimo_poblacion = input("Elija el criterio minimo de poblacion: ")

        maximo_poblacion = int(maximo_poblacion)
        minimo_poblacion = int(minimo_poblacion)
        
        for pais in paises:
            if pais["poblacion"] <= maximo_poblacion and pais["poblacion"] >= minimo_poblacion:
                filtrados.append(pais)
           
        if len(filtrados) == 0:
            print("No se encontraron países con esos criterios.")
        else:
            print(f"\n{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
            print("-" * 70)
        for pais in filtrados:
            print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")


    elif tipo == "superficie": 
        maximo_superficie = input("Elija el criterio maximo de superficie: ")
        minimo_superficie = input("Elija el criterio minimo de superficie: ")

        while not validar_entero_positivo(maximo_superficie):
            maximo_superficie = input("Elija el criterio maximo de superficie: ")
        while not validar_entero_positivo(minimo_superficie):
            minimo_superficie = input("Elija el criterio minimo de superficie: ")

        maximo_superficie = int(maximo_superficie)
        minimo_superficie = int(minimo_superficie)
        
        for pais in paises:
            if pais["superficie"] <= maximo_superficie and pais["superficie"] >= minimo_superficie:
                filtrados.append(pais)
           
        if len(filtrados) == 0:
            print("No se encontraron países con esos criterios.")
        else:
            print(f"\n{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
            print("-" * 70)
        for pais in filtrados:
            print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")



def filtrar_menu(paises):
    
    
    print("=" * 40)
    print("         FILTRAR PAÍSES")
    print("=" * 40)
    print("""
    1. Por continente 
    2. Por rango de poblacion
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
   