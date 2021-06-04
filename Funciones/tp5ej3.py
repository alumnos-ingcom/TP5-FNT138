################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def tribo():
    term_uno = 1
    term_dos = 1
    term_tres = 1
    secuencia = list()
    while term_tres <= 1000:
        secuencia.append(term_uno)
        secuencia.append(term_dos)
        secuencia.append(term_tres)        
        term_uno = term_uno+term_dos+term_tres
        term_dos = term_dos+term_uno+term_tres
        term_tres = term_tres + term_dos +term_uno
    return secuencia
    
def prueba():
    print("MUESTRA LOS NUMEROS MENORES A 1000 DE LA SECUENCIA DE TRIBONACCI")
    print(tribo())
    
if __name__ == "__main__":
    prueba()