################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4_ej1 import ingreso_entero

def maximo(lista):
    maxx = -999999
    cantidad_elementos = len(lista)
    
    for i in range(cantidad_elementos):
        if lista[i] > maxx:
            maxx = lista[i]
    return maxx


def minimo(lista):
    minimo = 999999
    cantidad_elementos = len(lista)
    
    for i in range(cantidad_elementos):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo
   
def prueba():
    print('Digite una lista de numeros enteros')
    cantidad_numeros = ingreso_entero('¿Cuantos numeros tendra su lista?')
    
    if cantidad_numeros <= 0:
        mensaje = print('La cantidad de numeros de su lista no puede ser menor o igual a 0')
        return mensaje
    
    lista = []
    for i in range(cantidad_numeros):
        n = ingreso_entero(f'Ingrese el numero {i+1}/{cantidad_numeros}')
        lista.append(n)
    
    min_lista = minimo(lista)
    print(f'El minimo de la la lista es: {min_lista}')
    max_lista = maximo(lista)
    print(f'El maximo de la la lista es: {max_lista}')
   
if __name__ == "__main__":
    prueba()
    
    