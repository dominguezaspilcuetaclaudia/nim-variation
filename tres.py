ganador="false"
cantidad=10
while ganador=="false":
    j1=input("resta 1")
    if j1!=1 or j1!=1:
        j1=input("tiene que ser 1 o 2")
    if j1==1 or j1==2:
        cantidad=cantidad-j1
        if cantidad==o:
            ganador=="true"
            print("gana1")
        if cantidad!=0:
            j2=input(resta2)
            if j2!=1 or j2!=2:
                j2=input("tiene que ser 1 o2")
            if j2==1 or j2==2:
                cantidad=cantidad-j2
                if cantidad==0:
                    ganador=="true"
                    print("gana 2")