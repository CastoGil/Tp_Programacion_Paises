# ------------------------------------------------------
# — Gestión de datos del TPI
# ------------------------------------------------------

import csv
from validaciones import (
    validar_texto_no_vacio,
    validar_entero_positivo,
    validar_existencia_pais
)


def leer_csv(ruta):
    """Lee el archivo CSV y devuelve una lista de países válidos."""
    paises = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    if (
                        not fila["nombre"].strip()
                        or not fila["poblacion"].isdigit()
                        or not fila["superficie"].isdigit()
                        or not fila["continente"].strip()
                    ):
                        print("- Línea con formato inválido en el CSV omitida.")
                        continue

                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)

                except (KeyError, ValueError):
                    print("- Error procesando una línea. Se omitió.")
                    continue

    except FileNotFoundError:
        print(f"- No se encontró el archivo: {ruta}")
    except PermissionError:
        print(f"- No hay permisos para leer el archivo.")
    except Exception as e:
        print(f"- Error inesperado al leer CSV: {e}")

    return paises


def guardar_csv(paises, ruta):
   
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for pais in paises:
                escritor.writerow(pais)

        print("- Cambios guardados correctamente en el archivo.")
    except Exception as e:
        print(f"- Error al guardar el archivo: {e}")


def agregar_pais(paises):
    
    print("\n=== AGREGAR PAÍS ===")

    try:
        nombre = input("Ingrese nombre del país: ").strip()
        while not validar_texto_no_vacio(nombre):
            nombre = input("Ingrese nombre del país: ").strip()

        if validar_existencia_pais(paises, nombre):
            print("- El país ya existe en la lista.")
            return

        poblacion = input("Ingrese población: ").strip()
        while not validar_entero_positivo(poblacion):
            poblacion = input("Ingrese población: ").strip()

        superficie = input("Ingrese superficie (km²): ").strip()
        while not validar_entero_positivo(superficie):
            superficie = input("Ingrese superficie (km²): ").strip()

        continente = input("Ingrese continente: ").strip()
        while not validar_texto_no_vacio(continente):
            continente = input("Ingrese continente: ").strip()

        pais = {
            "nombre": nombre.title(),
            "poblacion": int(poblacion),
            "superficie": int(superficie),
            "continente": continente.title()
        }

        paises.append(pais)
        print(f"- {nombre.title()} agregado correctamente.")

    except Exception as e:
        print(f"- Error inesperado al agregar país: {e}")


def actualizar_pais(paises):
   
    print("\n=== ACTUALIZAR PAÍS ===")

    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    while not validar_texto_no_vacio(nombre):
        nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    i = 0
    encontrado = False
    while i < len(paises):
        if paises[i]["nombre"].lower() == nombre.lower():
            encontrado = True

            nueva_poblacion = input("Ingrese nueva población: ").strip()
            
            while not validar_entero_positivo(nueva_poblacion):
                nueva_poblacion = input("Ingrese nueva población: ").strip()
            paises[i]["poblacion"] = int(nueva_poblacion)

            nueva_superficie = input("Ingrese nueva superficie (km²): ").strip()
            
            while not validar_entero_positivo(nueva_superficie):
                nueva_superficie = input("Ingrese nueva superficie (km²): ").strip()
            paises[i]["superficie"] = int(nueva_superficie)

            print(f"- {paises[i]['nombre']} actualizado correctamente.")
            break
        i += 1

    if not encontrado:
        print("- País no encontrado.")
