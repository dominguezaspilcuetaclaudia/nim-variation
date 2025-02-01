import random 
jugar="true"
u1=input("Hola!, escribe tu nombre:")
print("Hola,",u1,"El juego consiste en restar 1 o 2 piedras del número inicial de piedras y el primero que logre que hayan 0 piedras, gana.")
while jugar=="true":
    cantidad=random.randint(2,10) *3
    print("Comenzamos con:",cantidad,"piedras")
    ganador="false"
    while ganador=="false":
        print(u1,",escoge que tirar:")
        while "true":
            try:
                j1=int(input())
                while j1>=3 or j1<=0:
                    print("recuerda que solo puedes tirar 1 o 2")
                    j1=int(input("Por favor,tira de nuevo:")) 
                break
            except Exception as e:
                    print("lo siento, solo puedes poner  1 o 2")
            if cantidad==1:
                while j1>1:
                    print(u1,",no puedes tirar más de 1 si solo hay una piedra.Por favor, escoge 1")
                    j1=int(input())
        cantidad=cantidad-j1
        print("ahora hay",cantidad,"piedra(s)")
        if cantidad==0:
            print("Felicidades",u1,",tu ganaste esta ronda")
            ganador="true"
            print("te gustaría volver a jugar?")
            print("escribe si o no")
            a=input()
            while "true":
                if a=="si":
                    jugar="true"
                    break
                if a=="no":
                    jugar="false"
                    break
                if a !="no" or a !="si":
                    print("Por favor, escribe si o no")
                    a=input()
        if cantidad>0:    
            print("es mi tu turno de jugar") 
            yo=cantidad%3
            if yo<2:
                yo=1
            if yo>=2:
                yo=2
            if cantidad==2:
                yo=2
            if cantidad==1:
                yo=1
            print("elijo tirar:",yo)
            cantidad=cantidad-yo
            print("ahora hay",cantidad,"piedra(s)")
            if cantidad==0:
                ganador="true"
                print("Yo gané :D.¿te gustaría volver a jugar conmigo?")
                print("escribe si o no")
                a=input()
                while "true":
                    if a=="si":
                        jugar="true"
                        break
                    if a=="no":
                        jugar="false"
                        break
                    if a !="no" or a !="si":
                        print("Por favor, escribe si o no")
                        a=input()
print("Gracias por haber jugado conmigo")       

                               