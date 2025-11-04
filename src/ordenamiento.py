# ------------------------------------------------------
# Funciones de Ordenamiento
# ------------------------------------------------------
def ordenar_paises(paises, clave, descendente=False):
    
    n = len(paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if descendente:
                if paises[i][clave] < paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
            else:
                if paises[i][clave] > paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
                    
                    
def mostrar_menu_ordenamiento(paises):
    print(""" 
=== ORDENAR PAÍSES ===
1. Por nombre (A-Z)
2. Por nombre (Z-A)
3. Por población (ascendente)
4. Por población (descendente)
5. Por superficie (ascendente)
6. Por superficie (descendente)
""")
    
    opcion = input("Seleccione una opción: ").strip()

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
    else:
        print(" Opción inválida.")
        return

    print("------ Lista ordenada correctamente.-------")
    for pais in paises:
        print(f"{pais['nombre']:15} | Pob: {pais['poblacion']:10} | Sup: {pais['superficie']:10}")