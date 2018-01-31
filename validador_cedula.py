""" funcion de validar """
import math

def cedula_es_valida(cedula):
    """ funcion de validar """
    if len(cedula) != 10:
        return "No valida: debe ser de 10 digitos"
    else:
        if int(cedula[0:2]) > 24:
            return "No valida: Los primeros dos digitos no pertenecen a una provincia"
        if int(cedula[2]) > 6:
            return "No valida: el tercer digito debe ser menor a 6"
        coeficientes = '212121212'
        resultado = [0] * 9
        for i in range(0, 9):
            producto = int(cedula[i]) * int(coeficientes[i])
            if producto >= 10:
                producto -= 9
            resultado[i] = producto
        digito = int(math.ceil(sum(resultado)/10.0))*10 - sum(resultado)
        if digito != int(cedula[9]):
            return "No valida: no coincide el digito validador"
        return "Valida"
