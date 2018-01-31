"""
Éxamen de software
Código que valida CI
"""
import math

def cedula_es_valida(cedula):
    """
	Ejecución de función cedula_es_valida
	"""
    if(len(cedula) != 10):
        return "No valida: debe ser de 10 digitos"
    else:
        if(int(cedula[0:2]) > 24):
            mensaje = "Error, los primeros 2 digitos no son a una provincia"
            return mensaje
        if(int(cedula[2]) > 6):
            return "No valida: el tercer digito debe ser menor a 6"
        coeficientes = '212121212'
        resultado = [0]*9
        for index in range(9):
            producto = int(cedula[index])*int(coeficientes[index])
            if producto >= 10:
                producto -= 9
            resultado[index] = producto
        n = int(math.ceil(sum(resultado)/10.0))*10	
        digito_validador =  n - sum(resultado)
        if(digito_validador != int(cedula[9])):
            return "No valida: no coincide el digito validador"
        return "Valida"