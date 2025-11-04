from datos import leer_csv, agregar_pais, actualizar_pais, guardar_csv
from ordenamiento import mostrar_menu_ordenamiento
# from busquedas import buscar_pais
# from filtros import filtrar_menu
# from estadisticas import mostrar_estadisticas

# ------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------
def mostrar_menu():
    print("""
========================================
     GESTIÓN DE PAÍSES EN PYTHON
========================================
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Guardar cambios
8. Salir
---------------------------------------
          """)
    
def main ():
    ruta = "data/paises.csv"
    paises= leer_csv(ruta)
    
    if len(paises)==0:
        print("No se pudieron cargar los paises (verifique el CSV).")
        return
    
    opcion= ""
    while opcion !="8":
        mostrar_menu()
        opcion= input("Seleccione una opcion: ").strip()
        
        if   opcion=="1": agregar_pais(paises)
        elif opcion=="2": actualizar_pais(paises)
        # elif opcion=="3": buscar_pais(paises)
        # elif opcion=="4": filtrar_menu(paises)
        elif opcion=="5": mostrar_menu_ordenamiento(paises)
        # elif opcion=="6": mostrar_estadisticas(paises)
        elif opcion=="7": guardar_csv(paises, ruta)
        elif opcion=="8": 
            print("Programa finalizado correctamente. ¡Hasta luego!")
        else:
            print("Opcion invalida. Intente nuevamente.")
            
if __name__=="__main__":
    main()