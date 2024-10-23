def distancias(numero1, numero2):
    if numero1 <= 0 and numero2 <= 0:#los dos negativos
        if numero1 < numero2:#cual es menor
            distancia = numero2 - numero1
        else:
            distancia = numero2 - numero1
            
    elif numero1 >= 0 and numero2 >= 0:
        if numero1 < numero2:#cual es menor
            distancia = numero2 - numero1
        else:
            distancia = numero2 - numero1
        
    elif numero1 < 0 and numero2 > 0:
        distancia = numero2 - (numero1)
    
    elif numero1 >  0 and numero2 < 0:
        distancia = numero2 - numero1
    

        
    return distancia
    
    
def prueba():
    inicial = int(input("Numero: "))
    final = int(input("Numero: "))
    distancia = distancias(inicial, final)
    print(f" la distancia entre '{inicial}' y '{final}' es de '{distancia}'")

if __name__ == "__main__":
    prueba()