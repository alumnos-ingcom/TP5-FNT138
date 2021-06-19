################
# Fede Trujillo - @FNT138
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def cifrado_cesar(texto, rotacion):
    cifrado = ""
    
    for i in texto:
        
        if i >='A' and i <= 'Z':            
            caracter = ord(i)
            indice = ord(i) - ord("A")                    
            nuevo_indice = (indice + rotacion) % 26                     
            caracter_cifrado = nuevo_indice + ord("A")
            nuevo_caracter = chr(caracter_cifrado)            
            cifrado = cifrado + nuevo_caracter
            
        elif i >='a' and i<= 'z':
            caracter = ord(i)
            indice = ord(i) - ord("a")            
            nuevo_indice = (indice + rotacion) % 26            
            caracter_cifrado = nuevo_indice + ord("a")
            caracter_nuevo = chr(caracter_cifrado)            
            cifrado = cifrado + caracter_nuevo
        elif i >= '0' and i<= '9':
            caracter = ord(i)
            indice = ord(i) - ord("0")            
            nuevo_indice = (indice + rotacion) % 10          
            caracter_cifrado = nuevo_indice + ord("0")
            caracter_nuevo = chr(caracter_cifrado)            
            cifrado = cifrado + caracter_nuevo
            
        elif i == ' ':
            cifrado = cifrado + ' '
            
    return cifrado


def descifrado_cesar(texto, rotacion):
    descifrado = ""
    
    for i in texto:
        
        if i >='A' and i <= 'Z':            
            caracter = ord(i)            
            indice = ord(i) - ord("A")                    
            nuevo_indice = (indice - rotacion) % 26                     
            caracter_descifrado = nuevo_indice + ord("A")
            nuevo_caracter = chr(caracter_descifrado)            
            descifrado = descifrado + nuevo_caracter
            
        elif i >='a' and i<= 'z':            
            caracter = ord(i)            
            indice = ord(i) - ord("a")                    
            nuevo_indice = (indice - rotacion) % 26                     
            caracter_descifrado = nuevo_indice + ord("a")
            nuevo_caracter = chr(caracter_descifrado)            
            descifrado = descifrado + nuevo_caracter
            
        elif i >= '0' and i<= '9':
            caracter = ord(i)
            indice = ord(i) - ord("0")            
            nuevo_indice = (indice - rotacion) % 10          
            caracter_cifrado = nuevo_indice + ord("0")
            caracter_nuevo = chr(caracter_cifrado)            
            descifrado = descifrado + caracter_nuevo
            
        elif i == ' ':
            descifrado = descifrado + ' '
            
    return descifrado


def prueba():   
    ingreso = input("Numero de rotacion:")
    try:
        desplazamiento = int(ingreso)
    except ValueError as err:
        raise Exception(f"'{ingreso}' no era un número valido!") from err
    
    ingreso_texto = input("Texto a cifrar: ")    
    try:
        cadena_texto = str(ingreso_texto)
    except ValueError as err:
        raise Exception(f" '{ingreso_texto}' no era un texto valido!") from err
    
    # CIFRADO
    cifrado = cifrado_cesar(cadena_texto, desplazamiento)
    print("Cifrado")
    print(  cifrado)
    
    #DESCIFRADO
    descifrado = descifrado_cesar(cifrado, desplazamiento)
    print("Descifrado")
    print(descifrado)
    
    
if __name__ == "__main__":
    prueba()