#Ejercicio 2
num=1
lista=[]

while num!=0:
    try:
        num=int(input("Ingrese un número: "))
        lista.append(num)
        lista.sort()
        print(f"{lista}")

    except ValueError:
        print("Ingrese un número")