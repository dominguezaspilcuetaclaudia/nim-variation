cantidad=int(input("cantidad:"))
ganador="false"
j1=int(input("resta:"))
while ganador !="true":
    if j1!=1 or j1 !=2:
        j1=int(input("resta 1 o 2:"))
    if j1==1 or j1 ==2:
      cantidad=cantidad-j1
    if cantidad ==0:
        
        ganador="true"
if ganador=="true":
    print("ganaj1")

    
