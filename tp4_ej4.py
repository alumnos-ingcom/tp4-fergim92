################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4_ej1 as soporte
 
def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1


def prueba():
    condiciones = """
+-------------------------------------------------+
|Retornar -1 si el primero es menor que el segundo|
|Retornar 0 si son iguales                        |
|Retornar 1 si el primero es mayor que el segundo |
+-------------------------------------------------+
"""
    print(f'Comparacion de numeros\n {condiciones}')
    numero = soporte.ingreso_entero('Ingrese el primer numero: ')
    otro_numero = soporte.ingreso_entero('Ingrese otro numero')
    
    resultado = compara(numero, otro_numero)
    
    print(f'Respuesta: {resultado}')
    
if __name__ == "__main__":
    prueba()
