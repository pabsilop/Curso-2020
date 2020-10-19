
print("Indique las palabras que quiere introducir en la lista cuando quiera parar de meter palabras escriba FIN ")
listaPalabras=[]
palabraDada=""
while palabraDada!="FIN":
    palabraDada=input("Di una palabra: ")
    listaPalabras.append(palabraDada)
print("Orden alfabético")
listaPalabras.sort(key = str.lower)
print(listaPalabras)
print("Orden de menos a más carácteres")
listaPalabras.sort(key= len)
print(listaPalabras)
