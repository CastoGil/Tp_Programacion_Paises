# ------------------------------------------------------
# — Gestión de datos del TPI
# ------------------------------------------------------

import csv
import os
from validaciones import (
    validar_texto_no_vacio,
    validar_entero_positivo,
    validar_existencia_pais
)


# ------------------------------------------------------
# Función: Leer CSV
# ------------------------------------------------------
def leer_csv(ruta):
    
    paises = []

    if not os.path.exists(ruta):
        print(f"- No se encontró el archivo: {ruta}")
        return paises

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            
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

    return paises


# ------------------------------------------------------
# Función: Guardar CSV
# ------------------------------------------------------
def guardar_csv(paises, ruta):
    
    campos = ["nombre", "poblacion", "superficie", "continente"]

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print("- Cambios guardados correctamente en el archivo.")


# ------------------------------------------------------
# Función: Agregar país
# ------------------------------------------------------
def agregar_pais(paises):
    
    print("\n" + "=" * 35)
    print("        AGREGAR PAÍS")
    print("=" * 35)

    
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


# ------------------------------------------------------
# Función: Actualizar país
# ------------------------------------------------------
def actualizar_pais(paises):
    
    print("\n" + "=" * 35)
    print("       ACTUALIZAR PAÍS")
    print("=" * 35)

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
