#Escribir una función sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
# debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    total=0
    for i in range(0, len(lista)):
           total +=lista[i]
    return total

def multip(lista):
       total = 1
       for i in range(0, len(lista)):
           total *= lista[i]
       return total
print(sum([1,2,3,4]))
print(multip([1,2,3,4]))

