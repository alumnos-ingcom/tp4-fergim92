################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4_ej1 import ingreso_entero

def factores_primos(numero):
    if numero < 0:
        print('ENTERO POSITIVO!')
    lista = []
    i = 2
    
    while numero >= i:
        if numero % i == 0:       
            numero /= i     #dividimos por el divisor mas chico con resto 0 y toma un nuevo valor numero
            lista.append(i) 
        else:
            i +=1  #Cuando numero no se puede seguir dividiendo por el numero mas bajo con resto 0 va a aumentar el divisor
        
    tupla = (lista)
    return tupla
    
def prueba():
    numero = ingreso_entero('Digite un numero entero positivo para devolverlo en factores primos')
    tupla_de_primos = factores_primos(numero)
    print(tupla_de_primos)
 
if __name__ == "__main__":
    prueba()