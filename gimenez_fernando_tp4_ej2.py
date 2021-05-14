def suma_lenta(numero, otro_numero):
    limite = otro_numero
    if otro_numero < 0:
        limite *= -1
        
    for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i-1
            print(f'{numero-i} + (-1) = {resultado} ')
        else:
            resultado = numero + i+1
            print(f'{numero+i} + 1 = {resultado} ')
        
if __name__ == "__main__":        
    suma_lenta(-4, -10)
