# Crea un programa que almacene en una lista la nota de los alumnos de un grupo de SGE,
# y posteriormente calcule y visualice el número de notas que aparecen dentro de los siguientes intervalos:
# [0 , 5) Insuficiente
# [5 , 6) Aprobado
# [6, 7) Bien
# [7 , 9) Notable
# [9 , 10] Sobresaliente
listaNotas=[3,7,1,9,8,3,5,7,3,2,6,9,3,2,5,1,10]

def visualizarNotas(listaNotas):
    insuficientes=0
    aprobados=0
    bien=0
    notable=0
    sobresaliente=0
    for i in listaNotas:
        if listaNotas[i] >=0 and listaNotas[i] <5:
            insuficientes+=1
        elif listaNotas[i] >=5 and listaNotas[i] <6:
            aprobados+=1
        elif listaNotas[i] >=6 and listaNotas[i] <7:
            bien+=1
        elif listaNotas[i] >=7 and listaNotas[i] <9:
            notable+=1
        elif listaNotas[i] >=9 and listaNotas[i] <=10:
            sobresaliente+=1
    print(f"Insuficientes: {insuficientes}")
    print(f"Aprobados: {aprobados}")
    print(f"Bien: {bien}")
    print(f"Notables: {notable}")
    print(f"Sobresalientes: {sobresaliente}")

visualizarNotas(listaNotas)
