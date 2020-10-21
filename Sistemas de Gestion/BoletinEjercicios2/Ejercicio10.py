#Crea un programa en el que el usuario introduzca una frase y el programa calcule el número de palabras de dicha frase.
# Pista grande: para contar palabras podemos contar las veces que pasamos de un carácter
# que no es del alfabeto a uno que sí lo es. Para saber si un carácter es una letra,
# en Python tenemos la función string.isalpha().
texto="Esto es una frase de ejemplo para el ejercicio número diez de python que nos ayuda a contar las palabras que contiene una frase."
def contarPalabras(texto):
    palabras=texto.split()
    i=0
    while i < len(palabras):
        palabra=palabras[i]
        if palabra==".":
            ("")
        i+=1
    print("Número de palabras: ",i)

contarPalabras(texto)
