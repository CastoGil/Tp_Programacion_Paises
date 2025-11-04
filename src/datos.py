import csv
from validaciones import (
    validar_texto_no_vacio,
    validar_entero_positivo,
    validar_existencia_pais
)

# ------------------------------------------------------
# FUNCIONES DE LECTURA Y GUARDADO
# ------------------------------------------------------

def leer_csv(ruta):
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # Validar formato correcto de cada línea del CSV
            if (
                not fila["nombre"].strip() or
                not fila["poblacion"].isdigit() or
                not fila["superficie"].isdigit() or
                not fila["continente"].strip()
            ):
                print(" Línea con formato inválido en el CSV omitida.")
                continue

            pais = {
                "nombre": fila["nombre"].strip(),
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"].strip()
            }
            paises.append(pais)

    return paises


def guardar_csv(paises, ruta):
    """Guarda los datos actualizados en el archivo CSV."""
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print(" Cambios guardados correctamente en el archivo.")


# ------------------------------------------------------
# FUNCIONES DE GESTIÓN DE DATOS
# ------------------------------------------------------

def agregar_pais(paises):
    """Permite agregar un nuevo país si no existe."""
    print("\n=== AGREGAR PAÍS ===")

    nombre = input("Ingrese nombre del país: ").strip()
    if not validar_texto_no_vacio(nombre):
        return

    if validar_existencia_pais(paises, nombre):
        print(" El país ya existe en la lista.")
        return

    poblacion = input("Ingrese población: ").strip()
    if not validar_entero_positivo(poblacion):
        return

    superficie = input("Ingrese superficie (km²): ").strip()
    if not validar_entero_positivo(superficie):
        return

    continente = input("Ingrese continente: ").strip()
    if not validar_texto_no_vacio(continente):
        return

    pais = {
        "nombre": nombre.title(),
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente.title()
    }

    paises.append(pais)
    print(f"{nombre.title()} agregado correctamente.")


def actualizar_pais(paises):
    """Permite modificar los datos de un país existente."""
    print("\n=== ACTUALIZAR PAÍS ===")

    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    if not validar_texto_no_vacio(nombre):
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            nueva_poblacion = input("Ingrese nueva población: ").strip()
            if validar_entero_positivo(nueva_poblacion):
                pais["poblacion"] = int(nueva_poblacion)

            nueva_superficie = input("Ingrese nueva superficie (km²): ").strip()
            if validar_entero_positivo(nueva_superficie):
                pais["superficie"] = int(nueva_superficie)

            print(f" {pais['nombre']} actualizado correctamente.")
            return

    print(" País no encontrado.")
