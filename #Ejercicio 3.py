#Ejercicio 3
num=0
lista=[]
cont=0
suma=0
promedio=0
while cont!=10:
    num=int(input("Ingrese un número: "))
    lista.append(num)
    suma+=num
    cont+=1
print(f"Los números ingresados son: {lista}")
promedio=suma/10
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")
