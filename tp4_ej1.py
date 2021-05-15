################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass

def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero
    

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    for i in range(cantidad_reintentos):
        ingreso = input(f'intento {i+1}: ')
        try:
            entero = int(ingreso)
            break
        except ValueError as err:
            print('No es un numero entero!')
        if i == (cantidad_reintentos -1):
            raise IngresoIncorrecto("Cantidad de intentos agotada!") from err
    return entero

    
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    print(f'{mensaje}\nEntre {valor_minimo} y {valor_maximo}')
    entero = input('Numero entero a evaluar: ')
    
    try:
        entero = int(entero)
    except ValueError as err:
        raise IngresoIncorrecto("No esta ingresando numeros enteros!!!") from err
    
    if (entero <= valor_maximo) or (entero >= valor_minimo):
        print('Tu numero esta en el rango')
    else:
        print('No esta en el rango solicitado')
    
def prueba():
    print(f'Ingreso de números enteros\n')
    mensaje = 'Ingrese un numero entero:'
    numero1 = ingreso_entero(mensaje)
    
    print('\nIngresar un numero entero. Tiene reintentos limitados')
    mensaje = 'Ingrese el numero'
    numero2 = ingreso_entero_reintento(mensaje, cantidad_reintentos=5)
    
    mensaje ='\nIngreso de un número entero entre dos valores'
    ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10)


if __name__ == "__main__":
    prueba()
    
    
    
    
    
    
    
    
    
    
    
    
    
    