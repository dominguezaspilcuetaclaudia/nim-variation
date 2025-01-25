u1=input("escribe tu nombre jugador 1:")
u2=input("escribe tu nombre jugador 2:")
print("Hola,",u1,"y",u2,".","El juego consiste en escoger un número. Los jugadores van a ir restando 1 o 2 de dicho número y el primero que logre que sea 0, gana.")
cantidad=int(input("Escojan el número con el que desean jugar"))
ganador="false"
while ganador:
    print("Hola  tu resta") 
    j1=int(input())
    if j1!=1 or j1!=2:
        j1=int(input("ingresa 1 o 2:"))
    if cantidad - j1!=0 and j1==1 or j1==2:
        cantidad=cantidad-j1
        j2=int(input("haz tu jugada"))
        if j2==1 or j2==2 and cantidad-j2!=0:
            cantidad=cantidad-j2
    elif cantidad- j1==0:
        ganador="true"
        print(u1,"ganó")
    elif cantidad -j2==0:
        ganador="true"
        print(u2,"ganó")
    else:
        print("tiene que ser 1 o 2")
