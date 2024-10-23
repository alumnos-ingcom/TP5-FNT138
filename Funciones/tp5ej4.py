################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def perfectos(numero):
    encontrados = 0
    divisor = 1
    suma = 0
    while True: #simula el Do
        if numero%divisor == 0:
            suma = suma+ divisor
        divisor = divisor +1
        if not (divisor < numero): break #sale del loop
    if suma == numero:
        return True
    else:
        return False
    
    
def prueba():
    arg = int(input("Numero: "))
    numero_perfecto = perfectos(arg)
    print(f"{arg} es {numero_perfecto}")
    
if __name__ == "__main__":
    prueba()