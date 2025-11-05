# ------------------------------------------------------
# — Validaciones de datos
# ------------------------------------------------------

def validar_texto_no_vacio(texto):
    
    texto = texto.strip()
    if texto == "":
        print("❌ El campo no puede estar vacío.")
        return False

    for letra in texto:
        if not (letra.isalpha() or letra == " "):
            print("- Solo se permiten letras y espacios.")
            return False
    return True


def validar_entero_positivo(valor):
   
    try:
        numero = int(valor)
        if numero <= 0:
            print("- El número debe ser mayor que cero.")
            return False
        return True
    except ValueError:
        print("- Debe ingresar un número entero válido.")
        return False


def validar_existencia_pais(paises, nombre):
    
    i = 0
    while i < len(paises):
        if paises[i]["nombre"].lower() == nombre.lower():
            return True
        i += 1
    return False
