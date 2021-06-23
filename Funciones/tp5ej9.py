################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factorion(digitos):
    contador = 0
    sumador = 0
    random = str
    factoriones = list()

    for i in range(0, 1499999):
        sumador = 0
        random = str(i)
        for j in random:
            sumador = sumador + digitos[int(j)]
            if sumador == int(i):
                factoriones.append(i)
                
    return factoriones

def prueba():
    factoriales = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    factoriones = factorion(factoriales)
    print(f"'{factoriones}' Son los factoriones entre '0' y '1499999'")
if  __name__ == "__main__":
    prueba()