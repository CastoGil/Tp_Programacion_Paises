# ------------------------------------------------------
# — Funciones de ordenamiento manual
# ------------------------------------------------------

def ordenar_paises(paises, clave, descendente=False):
    
    n = len(paises)
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:

            # Bloque ascendente o descendente
            if descendente:
                if paises[i][clave] < paises[j][clave]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux
            else:
                if paises[i][clave] > paises[j][clave]:
                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux

            j += 1
        i += 1


def mostrar_menu_ordenamiento(paises):
    
    print("=" * 40)
    print("         ORDENAR PAÍSES")
    print("=" * 40)
    print("""
1. Por nombre (A-Z)
2. Por nombre (Z-A)
3. Por población (ascendente)
4. Por población (descendente)
5. Por superficie (ascendente)
6. Por superficie (descendente)
""")

    opcion = input("Seleccione una opción (1-6): ").strip()

    
    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("- Opción inválida. Intente nuevamente.")
        opcion = input("Seleccione una opción (1-6): ").strip()

    # Aplicar ordenamiento
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

    
    print("\nLista ordenada correctamente:\n")
    print(f"{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
    print("-" * 70)
    i = 0
    while i < len(paises):
        pais = paises[i]
        print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")
        i += 1
    print("-" * 70)
    print(f"Total de países ordenados: {len(paises)}\n")
