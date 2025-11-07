# ------------------------------------------------------
# — Búsqueda de países por nombre
# ------------------------------------------------------

def buscar_pais(paises):
    print("\n" + "=" * 40)
    print("         BUSCAR PAÍS")
    print("=" * 40)

    termino = input("Ingrese el nombre o parte del país a buscar: ").strip().lower()

    if termino == "":
        print("- No se ingresó ningún término de búsqueda.")
        return


    resultados = []
    i = 0

    while i < len(paises):
        if termino in paises[i]["nombre"].lower():
                resultados.append(paises[i])
        i += 1

    if len(resultados) == 0:
        print("- No se encontraron países que coincidan con la búsqueda.")
    else:
        print(f"\n{'Nombre':15} | {'Población':>12} | {'Superficie (km²)':>16} | {'Continente':>12}")
        print("-" * 70)
        for pais in resultados:
            print(f"{pais['nombre']:15} | {pais['poblacion']:12} | {pais['superficie']:16} | {pais['continente']:>12}")