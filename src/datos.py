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
            # Verificar si la fila está completamente vacía
            fila_vacia = True
            for clave in fila:  
                valor = fila[clave]
                if valor.strip() != "":
                    fila_vacia = False
                    break
            if fila_vacia:
                continue  
            
            # Validar formato de cada campo
            nombre = fila["nombre"].strip()
            poblacion = fila["poblacion"].strip()
            superficie = fila["superficie"].strip()
            continente = fila["continente"].strip()

            if (
                nombre == ""
                or poblacion == ""
                or superficie == ""
                or continente == ""
                or not poblacion.isdigit()
                or not superficie.isdigit()
            ):
                print(f"- Línea con formato inválido omitida : {fila}")
                continue

            pais = {
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente.capitalize()
                   }

            paises.append(pais)

    if len(paises) == 0:
        print("- No se encontraron países válidos en el CSV.")
    else:
        print(f"- Se cargaron {len(paises)} países correctamente.")

    return paises


# ------------------------------------------------------
# Función: Guardar CSV
# ------------------------------------------------------
def guardar_csv(paises, ruta):
    
    if len(paises) == 0:
        print("- No hay países cargados para guardar. Operación cancelada.")
        return

    campos = ["nombre", "poblacion", "superficie", "continente"]

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        i = 0
        while i < len(paises):
            escritor.writerow(paises[i])
            i += 1

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

    continente = continente.strip().capitalize()

    pais = {
        "nombre": nombre.title(),
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
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

            paises[i]["nombre"] = paises[i]["nombre"].strip().title()

            print(f"- {paises[i]['nombre']} actualizado correctamente.")
            break
        i += 1

    if not encontrado:
        print("- País no encontrado.")
