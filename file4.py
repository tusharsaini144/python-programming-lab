#Python program to count the number of lines in a file
F=open("drinks.dat","r")

count=0

while(True):
    b=F.read(1)
    if(b=='\n'):
        count+=1
    if(b==""):
        break
    print(b,end="")

print("Line Count " , count)

F.close()
