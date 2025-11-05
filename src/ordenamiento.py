# ------------------------------------------------------
# — Funciones de ordenamiento manual
# ------------------------------------------------------

def ordenar_paises(paises, clave, descendente=False):
   
    n = len(paises)
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if descendente:
                if paises[i][clave] < paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
            else:
                if paises[i][clave] > paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
            j += 1
        i += 1


def mostrar_menu_ordenamiento(paises):
    
    print("""
========================================
        ORDENAR PAÍSES
========================================
1. Por nombre (A-Z)
2. Por nombre (Z-A)
3. Por población (ascendente)
4. Por población (descendente)
5. Por superficie (ascendente)
6. Por superficie (descendente)
----------------------------------------
""")

    opcion = input("Seleccione una opción (1-6): ").strip()
    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("- Opción inválida. Intente nuevamente.")
        opcion = input("Seleccione una opción (1-6): ").strip()

    if opcion == "1":
        ordenar_paises(paises, "nombre")
    elif opcion == "2":
        ordenar_paises(paises, "nombre", True)
    elif opcion == "3":
        ordenar_paises(paises, "poblacion")
    elif opcion == "4":
        ordenar_paises(paises, "poblacion", True)
    elif opcion == "5":
        ordenar_paises(paises, "superficie")
    elif opcion == "6":
        ordenar_paises(paises, "superficie", True)

    print("\n Lista ordenada correctamente:\n")
    print(f"{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16}")
    print("-" * 50)
    for pais in paises:
        print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16}")
