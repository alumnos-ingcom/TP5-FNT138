################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def par_impar(numero):
    """
    Indica si un numero es par o impar
    """
    decimal = float(numero)
    numero = int(numero / 2)
    decimal = (decimal / 2)
    
    if numero < decimal:
        return False
    else:
        return True

def prueba():
    """Toda la interacción con el usuario va acá"""
    numero_ingreso = int(input("numero: "))
    numero = par_impar(numero_ingreso)
    
    print(f"{numero_ingreso} es {numero}")

if __name__ == "__main__":
    prueba()