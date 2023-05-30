#Pizza Tradicional 12000
#Pizza peperoni 14000
#Pizza all carnes 17000
#Descuento diurnos 20%
#Descuento vespertino 15%
#Descuento administrativos 5%
precio=0
total=0
opcion=0
cant_allf=0
cant_tradf=0
cant_pepf=0
cant_all=0
cant_pep=0
cant_trad=0
precio_trad=0
precio_pep=0
precio_all=0
print("Bienvenido a PizzaDuoc!")
jornada=input("Tenemos descuentos para quienes son parte de Duoc, eres:\n1.-Diurno.\n2.-Vespertino.\n3.-Administrativo.\n4.-Ninguno.\n")
while opcion!="2":
    try:
        opcion=input("¿Desea realizar una compra?\n1.-Ir a comprar.\n2.-Salir.\n")
        if opcion=="1":
            pizza=input("Tenemos 3 tipos de pizzas, estos son:\n1.-Tradicional=$12000.\n2.-Peperoni=$14000.\n3.-All carnes=$17000.\n")
            if pizza=="1":
                cant_trad=int(input("Cuantas pizzas Tradicional desea?\n"))
                precio_trad=cant_trad*12000
                total+=precio_trad
            elif pizza=="2":
                cant_pep=int(input("Cuantas pizzas Pepperoni desea?\n"))
                precio_pep=cant_pep*14000
                total+=precio_pep
            elif pizza=="3":
                cant_all=int(input("Cuantas pizzas All Carnes desea?\n"))
                precio_all=cant_all*17000
                total+=precio_all
        elif opcion=="2":
            if jornada=="1":
                desc=total*0.2
                total_fin=total*0.8
            elif jornada=="2":
                desc=total*0.15
                total_fin=total*0.85
            elif jornada=="3":
                desc=total*0.05
                total_fin=total*0.95
            elif jornada=="4":
                desc=0
                total_fin=total
            
            if total!= 0:
                print("Pedido:")
                if cant_trad>0:
                    print(f"* {cant_trad} Tradicional")
                
                if cant_pep>0:
                    print(f"* {cant_pep} Peperoni")

                if cant_all>0:
                    print(f"* {cant_all} All Carnes")
                
                print(f"Total= ${(precio_trad+precio_pep+precio_all)}")
                print(f"Descuento= ${desc}")
                print(f"Total Final= ${total_fin}")
            elif total==0:
                print("Hasta pronto!")
    except ValueError:
        print("Debe escribir un número")
    except:
        print("Error en el sistema")            