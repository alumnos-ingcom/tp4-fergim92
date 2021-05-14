################
# Fernando Gimenez - @fergim92
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def convertir_a_fahrrenheit(centigrados):
    try:
        centigrados = float(centigrados)
    except ValueError as err:
        raise IngresoIncorrecto("Estas pasando como parametro algo que no es un numero!!!") from err
    
    fahr= (centigrados * 1.8) + 32
    print(f'{centigrados} grados Centigrados son {fahr} Fahrenheits')

def convertir_a_centigrados(fahrenheit):
    try:
        fahrenheits = float(fahrenheit)
    except ValueError as err:
        raise IngresoIncorrecto("Estas pasando como parametro algo que no es un numero!!!") from err
    
    centigrados = (fahrenheit - 32) / 1.8
    centigrados = round(centigrados,2)
    print(f'{fahrenheit} Fahrenheits son {centigrados} grados Centigrados')
    
    
if __name__ == "__main__":
    convertir_a_fahrrenheit(1)
    convertir_a_centigrados(33.8)
    