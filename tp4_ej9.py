################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_entero 

def es_primo(numero):
    divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        return true         #########
    

def prueba():
    numero = ingreso_entero('Digite un numero para saber si es primo')
    print(es_primo(numero))

if __name__ == "__main__":
    prueba()