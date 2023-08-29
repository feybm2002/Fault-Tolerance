# Maria Fernanda Barroso Monroy
# Actividad 2 - Parte 2
# Fault-Tolerance

import logging # Libreria para el logeo de errores

# Configuración del logeo de errores en un archivo llamado "registro_errores.log"
logging.basicConfig(filename='registro_errores.log', level=logging.ERROR)
# Inicio de una Assertions
def dividir(a, b):
    try: # Se agrega un try-cath
        # Usamos un assertion para asegurarnos de que b no sea 0
        assert b != 0, "Error: No se puede dividir por cero."
        
        # Realizamos la división y retornamos el resultado
        return a / b
    except AssertionError as e:
        # Si la assertion falla, capturamos la excepción y la registramos
        logging.error(str(e))
        return None
    except ZeroDivisionError:
        # Manejamos el caso de división por cero
        logging.error("Error: División por cero.")
        return None

# try-catch para los datos que ingrese el usuario
try:
    num1 = float(input("Ingrese un número: "))
    num2 = float(input("Ingrese otro número: "))
    
    resultado = dividir(num1, num2)
    
    if resultado is not None:
        print("Resultado:", resultado)
    else:
        print("Hubo un error en la división.")
except ValueError:
    logging.error("Error: Ingrese valores numéricos válidos.")

