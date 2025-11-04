# ------------------------------------------------------
# Validaciones
# ------------------------------------------------------

def validar_texto_no_vacio(texto):
    texto=texto.strip()
    if texto=="":
        print("El texto no puede estar vacio.")
        return False
    return True

def validar_entero_positivo(valor):
    if not valor.isdigit():
        print("Debe ingresar un número entero positivo.")
        return False
    if int(valor) <= 0:
        print(" El número debe ser mayor que cero.")
        return False
    return True

def validar_existencia_pais(paises, nombre):
    """Verifica si un país ya existe en la lista (coincidencia insensible a mayúsculas)."""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True  
    return False 