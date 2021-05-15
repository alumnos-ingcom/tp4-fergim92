################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4_ej1 as soporte

def signo(numero):
    if numero > 0:
        print('El numero es positivo')
    elif numero < 0:
        print('El numero es negativo')
    else:
        print('El numero es 0')


def prueba():
    print('Numeros positivos y negativos')
    numero = soporte.ingreso_entero('Ingrese un numero')
    signo(numero)


if __name__ == "__main__":
    prueba()
    
    