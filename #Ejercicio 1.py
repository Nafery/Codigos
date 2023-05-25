#Ejercicio 1
numero=int(input("ingrese un numero: "))
lista=[]
for i in range (1,11):
    tabla=numero*i
    lista.append(tabla)

contador=1
for x in lista:
    print(f"Posicion {contador} es: {x}")
    contador+=1