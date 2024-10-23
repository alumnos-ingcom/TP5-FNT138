def cambio_binario(numero):
    binario = ""
    if numero > 0:
        while numero > 0:
            if (numero % 2 == 0):
                binario = "0" + binario
            else:
                binario = "1" + binario
            numero = int(numero/2)
        return binario
    elif numero == 0:
        return 0
    else:
        return "invalido"
    
    
def prueba():
    numero = int(input("numero: "))
    cambio = cambio_binario(numero)
    print(cambio)
    
if __name__ == "__main__":
    prueba()