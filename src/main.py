# ------------------------------------------------------
# Menú Principal - Gestión de Países
# ------------------------------------------------------

from datos import leer_csv, agregar_pais, actualizar_pais, guardar_csv
from ordenamiento import mostrar_menu_ordenamiento
from busquedas import buscar_pais
from filtros import filtrar_menu, filtrar_paises
from estadisticas import mostrar_estadisticas, calcular_estadisticas


def mostrar_menu():
    print("=" * 40)
    print("   GESTIÓN DE PAÍSES EN PYTHON")
    print("=" * 40)
    print("""
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Guardar cambios
8. Salir
""")
    print("-" * 40)


def main():
    """Ejecuta el programa principal."""
    ruta = "../data/paises.csv"
    paises = leer_csv(ruta)

    if len(paises) == 0:
        print("- No se pudieron cargar los países. Verifique el CSV.")
        return

    opcion = ""

    # Bucle principal bloqueante
    while opcion != "8":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        # Validación bloqueante para opción válida
        while opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("- Opción inválida. Intente nuevamente.")
            opcion = input("Seleccione una opción (1-8): ").strip()

        # Lógica de opciones
        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_menu(paises)

        elif opcion == "5":
            mostrar_menu_ordenamiento(paises)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            guardar_csv(paises, ruta)

        elif opcion == "8":
            
            print("\n¿Desea guardar los cambios antes de salir? (s/n)")
            guardar = input("→ ").strip().lower()
            if guardar == "s":
                guardar_csv(paises, ruta)
            print("\nGracias por utilizar el sistema de gestión de países.")
            print("-" * 40)
            break

if __name__ == "__main__":
    main()
