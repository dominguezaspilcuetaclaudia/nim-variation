ganador="false"
u1=input("escribe tu nombre jugador 1:")
u2=input("escribe tu nombre jugador 2:")
print("Hola,",u1,"y",u2,".","El juego consiste en escoger una cantidad de piedras;Los jugadores van a ir restando 1 o 2 piedras del número inicial y el primero que logre que hayan 0 piedras, gana.")
cantidad=int(input("escojan la cantidad de piedras:"))
while ganador=="false":
    print(u1,"escoge que tirar:")
    j1=int(input())
    while j1>=3 or j1<=0:
        print(u1,"recueda que debe ser 1 o 2")
        j1=int(input("tira de nuevo:")) 
    if cantidad==1:
        while j1>1:
            print(u1,",no puedes tirar más de 1 si solo hay una piedra.Por favor, escoge 1")
            j1=int(input())
    cantidad=cantidad-j1
    print("ahora hay",cantidad,"piedra(s)")
    if cantidad==0:
        print("Felicidades",u1,"ganaste")
        ganador="true"
    if cantidad>0:    
        print(u2,"es tu turno de jugar") 
        j2=int(input())
        while j2>=3 or j2<=0:
            print(u2,"recueda que debe ser 1 o 2")
            j2=int(input("tira de nuevo:"))
        if cantidad==1:
            while j2>1:
                print(u2,",no puedes tirar más de 1 si solo hay una piedra.Por favor, escoge 1")
                j2=int(input())
        cantidad=cantidad-j2
        print("ahora hay",cantidad,"piedra(s)")
        if cantidad==0:
            ganador="true"
            print("felicidades,",u2,"ganaste.")
