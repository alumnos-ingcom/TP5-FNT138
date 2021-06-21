
def promedio_movil(lista, cant_valores):
    salida, promedio_movil = [0], []
    for i, x in enumerate(lista, 1):
        salida.append(salida[i - 1] + x)
        if i >= cant_valores:
            a = ((salida[i] - salida[i - cant_valores])/cant_valores)        
            promedio_movil.append(a)
    return promedio_movil

def prueba():
    cantidad = int(input("Cantidad de valores a tomar en cada promedio: "))
    
    ingreso =[int(input("Numero para la lista: "))]    
    respuesta = input("¿Desea agregar mas valores a la lista? s/n: ")
    while respuesta == 's' or respuesta =='S':
        ingreso.append(int(input("Numero para la lista:")))
        respuesta = input("¿Desea agregar mas valores a la lista? s/n: ")
    while respuesta == 'n' or respuesta =='N':
        print(f"Su lista quedo asi '{ingreso}'")
        break
    promedio = promedio_movil(ingreso, cantidad)
    print(f" El promedio movil de '{ingreso}' en {cantidad} valores es de '{promedio}'")
        
    
    
    
if __name__ == "__main__":
    prueba()