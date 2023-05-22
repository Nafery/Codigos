lista = [15, "Nombre", 3.1415, True]

print(lista[1])

usuario=["usernameTest1","pass123","correo@correo.com","edad"]

numeros=[10,50,100,255,500]
#append= Agrega un objeto en la última posición
numeros.append(1000)
print(numeros)
#Extend= Agrega un arreglo al final de la lista
extra=[75,350,999]
numeros.extend(extra)
print(numeros)
#insert= Agrega valor en posicion específica
numeros.insert(6,5000)
print(numeros)
#Remove= Entrego valor, se busca y elimina
numeros.remove(50)
print(numeros)
#pop= Elimina el último registro
#pop(i)=Elimina la posición del número
numeros.pop()
print(numeros)
numeros.pop(3)
#reverse= invierte el orden de la lista
numeros.reverse()
print(numeros)
#sort=Ordena los valores de menor a mayor
#sort(reverse=True)= Ordena los valores de mayor a menor
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)