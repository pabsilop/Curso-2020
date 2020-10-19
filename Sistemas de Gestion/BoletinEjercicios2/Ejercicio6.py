#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen
# el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
cadena = "Dabale arroz a la zorra el abad"

# Imprime en ese caso "Es palindroma"
def palindromo(cadena):
    cadena = "".join(cadena.split())
    cadena =cadena.lower()
    if str(cadena) == str(cadena)[::-1]:
        print("Es palindroma")
    else:
        print("No es palindroma")
palindromo(cadena)
