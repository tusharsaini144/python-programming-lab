F=open("drinks.dat","w")

while(True):
    v=input("Enter Drink Name : ")
    
    if(v==""):
        break
    
    F.write(v+"\n")

F.close()
