################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4_ej1 as soporte
import tp4_ej6 as soporte2

class IngresoIncorrecto(Exception):
    pass

def ordenar_mayor_a_menor(uno, dos, tres):
    lista = [uno, dos, tres]
    suma = uno + dos + tres
    maxim = soporte2.maximo(lista)   
    mini = soporte2.minimo(lista)
    n_medio = suma - mini - maxim
    tupla = (maxim, n_medio, mini)
        
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    lista = [uno, dos, tres]
    suma = uno + dos + tres              #sumamos los 3 numeros
    maxim = soporte2.maximo(lista)       #maximo de la lista usando la funcion del ejercicio anterior
    mini = soporte2.minimo(lista)        #minimo de la lista usando la funcion del ejercicio anterior
    n_medio = suma - mini - maxim        # a la suma total le restamos maximo y minimo y obtenemos el tercer numero que falta
    tupla = (mini, n_medio, maxim)
        
    return tupla
    
            
def prueba():
    print('Ingrese 3 numeros para ordenarlos de menor a mayor y luego de mayor a menor')
    uno = soporte.ingreso_entero('Numero 1: ')
    dos = soporte.ingreso_entero('Numero 2: ')
    tres = soporte.ingreso_entero('Numero 3: ')
    
    print('Ordenados de mayor a menor')
    tupla = ordenar_mayor_a_menor(uno, dos, tres)
    print(tupla)
    
    print('Ordenados de menor a mayor')
    tupla2 = ordenar_menor_a_mayor(uno, dos, tres)
    print(tupla2)
    
if __name__ == "__main__":        
    prueba()
    

