
def inversion_letras(palabra, diccionario, diccionario2):

    cambiada = ""
    for letra in palabra:
        if letra >= 'A' and letra <='Z':
            for k,v in diccionario.items():
                letra = letra.replace(k, v)
            cambiada = cambiada + letra
        elif letra >= 'a' and letra <='z':
            for k,v in diccionario2.items():
                letra = letra.replace(k, v)
            cambiada = cambiada + letra
        elif letra ==  " ":
            cambiada = cambiada + " "
    return cambiada
            


def prueba():
    dic_mayus = {"A":"a", "B":"b", "C":"c", "D":"d",
               "E":"e", "F":"f", "G":"g", "H":"h",
               "I":"i", "J":"j", "K":"k", "L":"l",
               "M":"m", "N":"n", "Ñ":"ñ", "O":"o",
               "P":"p", "Q":"q", "R":"r", "S":"s",
               "T":"t", "U":"u", "V":"v", "W":"w",
               "X":"x", "Y":"y", "Z":"z"}
    dic_min = {"a":"A", "b":"B", "c":"C", "d":"D",
               "e":"E", "f":"F", "g":"G", "h":"H",
               "i":"I", "j":"J", "k":"K", "l":"L",
               "m":"M", "n":"N", "ñ":"Ñ", "o":"O",
               "p":"P", "q":"Q", "r":"R", "s":"S",
               "t":"T", "u":"U", "v":"V", "w":"W",
               "x":"X", "y":"Y", "z":"Z"}
                   
    texto = str(input("Ingrese su texto: "))
    cambio = inversion_letras(texto, dic_mayus, dic_min)
    print(f" El texto original era '{texto}' se modifico a '{cambio}'")

if __name__== "__main__":
    prueba()