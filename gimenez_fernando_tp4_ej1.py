################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass


def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
         entero = int(ingreso)
    except ValueError as err:
         raise IngresoIncorrecto("No era un número!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    print(f'{mensaje}\nTiene {cantidad_reintentos} intentos')
    for i in range(cantidad_reintentos):
        ingreso = input(f'intento {i+1}: ')
        try:
            entero = int(ingreso)
            return entero
        except ValueError as err:
            print('No es un numero entero')
            
        if i == (cantidad_reintentos -1):
            raise IngresoIncorrecto("No era un número!") from err
            return entero 
            

def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    print(f'{mensaje}{valor_minimo} y {valor_maximo}: ')
    ingreso = input()
    try:
        entero = int(ingreso)
        if (entero > valor_maximo) or (entero < valor_minimo):
            print('No esta en el rango solicitado')
    except ValueError as err:
        raise IngresoIncorrecto("No era un numero!") from err
    return entero

    


if __name__ == "__main__":
    print('Funcion 1.Ingreso de numeros enteros')
    ingreso_entero('Ingrese un numero entero')
    
    print('\nFuncion 2.Ingresar un número entero y vuelva a solicitarlo en caso de ingresar un valor incorrecto')
    ingreso_entero_reintento('Ingrese un numero entero', cantidad_reintentos=5)
 
    print('\nFuncion 3.Ingresar un número entre 2 rangos')
    ingreso_entero_restringido('Ingrese un numero entre ',valor_minimo=0, valor_maximo=10)
    
    
    
    
    
    
    
    
    
    
    
    