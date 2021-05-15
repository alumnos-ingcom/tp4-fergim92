################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4_ej1 as soporte

class IngresoIncorrecto(Exception):
    pass

def suma_lenta(numero, otro_numero):
  
    limite = otro_numero     
    if otro_numero < 0:             # Para no tener problemas con los numeros negativos en el rango del ciclo for
        limite *= -1
        
    for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i-1
            print(f'{numero-i} + (-1) = {resultado} ')
        else:
            resultado = numero + i+1
            print(f'{numero+i} + 1 = {resultado} ')
    return resultado
            
def prueba():
   print('Ingrese 2 numeros para sumarlos')
   numero = soporte.ingreso_entero('Ingrese un numero: ')
   otro_numero = soporte.ingreso_entero('Ingrese otro numero: ')
   suma_lenta(numero, otro_numero)
      
if __name__ == "__main__":        
    prueba()
    
