################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import IngresoIncorrecto

def es_palindromo(texto):
    texto = texto.lower()          ## Pasamos la cadena a minuscula para comparar mejor  
    texto = texto.replace(" ", "") ## Eliminamos los espacios en blanco
    cantidad_caracteres = len(texto)
    coincidencias = 0
    for i in range(cantidad_caracteres):
        if texto[i] == texto[-i-1]:
            coincidencias +=1
            if coincidencias == cantidad_caracteres:
                return True

def prueba():
    texto = input('Ingrese una palabra o frase para saver si se trata de un palindromo: ')
    print(es_palindromo(texto))
    
if __name__ == "__main__":
    prueba()