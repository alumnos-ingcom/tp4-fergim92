################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def suma_lenta(numero, otro_numero):
    print('Funcion de suma lenta de 2 numeros enteros pasados por parametro')
    try:
        n1 = int(numero)
        n2 = int(otro_numero)
    except ValueError as err:
        raise IngresoIncorrecto("Estas pasando como parametro algo que no es un numero!!!") from err
    
    limite = otro_numero    
    if otro_numero < 0:
        limite *= -1
        
    for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i-1
            print(f'{numero-i} + (-1) = {resultado} ')
        else:
            resultado = numero + i+1
            print(f'{numero+i} + 1 = {resultado} ')
        
if __name__ == "__main__":        
    suma_lenta(0, 10)
