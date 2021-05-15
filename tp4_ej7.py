################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4_ej1 as soporte

def division_lenta(dividendo, divisor):
    cociente = 0
    
    if dividendo < divisor:
        mensaje = print('Es una division de enteros!!el dividendo tiene que ser mayor al divisor!!')
        return mensaje
        
    if dividendo > 0 and divisor > 0:         #(+)(+) =(+)
        while dividendo >= divisor:
            dividendo -= divisor
            cociente +=1
        resto = dividendo
    
    elif (dividendo < 0) and (divisor > 0 ):  #(-)(+) =(-)
        dividendo *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente -=1
        resto = dividendo
    
    elif (divisor < 0) and (dividendo > 0):   #(+)(-) =(-)
        divisor *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente -=1
        resto = dividendo
    
    else:                                     #(-)(-) =(+)
        divisor *= -1
        dividendo *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente +=1
        resto = dividendo
    
    print(f'El cociente de la division es: {cociente}')
    print(f'El resto de la division es: {resto}')
    
def prueba():
    dividendo = soporte.ingreso_entero('Ingrese el dividendo: ')
    divisor = soporte.ingreso_entero('Ingrese el divisor: ')
    division_lenta(dividendo, divisor)
    
    
if __name__ == "__main__":
    prueba()