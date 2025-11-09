# ------------------------------------------------------
# — Validaciones de datos
# ------------------------------------------------------

def validar_texto_no_vacio(texto):
    """Verifica que el texto no esté vacío y solo contenga caracteres válidos."""
    texto = texto.strip()
    if texto == "":
        print("- El campo no puede estar vacío.")
        return False

    # Se permiten letras, espacios, guiones y apóstrofes
    for letra in texto:
        if not (letra.isalpha() or letra == " " or letra == "-" or letra == "'"):
            print("- Solo se permiten letras, espacios, guiones o apóstrofes.")
            return False

    return True


def validar_entero_positivo(valor):
    """Verifica que el valor sea un número entero positivo."""
    if not valor.isdigit():
        print("- Debe ingresar un número entero válido.")
        return False

    numero = int(valor)
    if numero <= 0:
        print("- El número debe ser mayor que cero.")
        return False

    return True


def validar_existencia_pais(paises, nombre):
    """Comprueba si un país ya existe en la lista."""
    i = 0
    while i < len(paises):
        if paises[i]["nombre"].lower() == nombre.lower():
            return True
        i += 1
    return False
