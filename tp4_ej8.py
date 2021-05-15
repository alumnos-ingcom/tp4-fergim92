################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4_ej1 as soporte

class IngresoIncorrecto(Exception):
    pass

def ordenar_mayor_a_menor(uno, dos, tres):
    
    

        
    
# def ordenar_menor_a_mayor(uno, dos, tres):
    
            
def prueba():
    print('Ingrese 3 numeros para ordenarlos de menor a mayor y luego de mayor a menor')
    uno = soporte.ingreso_entero('Numero 1: ')
    dos = soporte.ingreso_entero('Numero 2: ')
    tres = soporte.ingreso_entero('Numero 3: ')
    
    ordenar_mayor_a_menor(uno, dos, tres)
    
      
if __name__ == "__main__":        
    prueba()
    

