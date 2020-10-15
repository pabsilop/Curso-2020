# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def trueOfalse(caracter):
    if caracter=='a' or 'e' or 'i' or 'o' or 'u':
        return True
    else:
        return False

caracter="c"
print(trueOfalse(caracter))

