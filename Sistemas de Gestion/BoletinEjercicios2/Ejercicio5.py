#Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa2(cadena):
    cadenaNueva = ""
    for i in cadena:
        cadenaNueva= i + cadenaNueva
    return cadenaNueva
cadena=input("Diga la cadena que quiere invertir: ")
print(inversa2(cadena))
