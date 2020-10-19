#Escribir una función que tome un carácter y devuelva True si es una vocal
# , de lo contrario devuelve False.
def evaluarCaracter(caracter):
    if(caracter=="a" or caracter=="A"):
        print("True")
    elif(caracter=="e" or caracter=="E"):
        print("True")
    elif(caracter=="i" or caracter=="I"):
        print("True")
    elif(caracter=="o" or caracter=="O"):
        print("True")
    elif(caracter=="u" or caracter=="U"):
        print("True")
    else:
        print("False")
caracter=input("Introduzca una letra: ")
evaluarCaracter(caracter)
