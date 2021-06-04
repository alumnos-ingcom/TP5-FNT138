################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def fibo():
    term_uno = 0
    term_dos = 1
    while term_uno <= 1000:
        print(term_uno)
        print(term_dos)
        term_uno = term_uno+term_dos
        term_dos = term_dos+term_uno
    
def prueba():
    print(fibo())
if __name__ == "__main__":
    prueba()