# 1 Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def mayorDeTres(a,b,c):
    if(a>b and a>c):
        print(f"{a} es mayor que {b} y que {c}")
    elif(b>a and b>c):
        print(f"{b} es mayor que {a} y que {c}")
    elif(c>a and c>b):
        print(f"{c} es mayor que {a} y que {b}")

print("Introduzca tres números y se le devolverá el mayor: ")

a = input("Número 1: ")
b = input("Número 2: ")
c = input("Número 3: ")

mayorDeTres(a,b,c)