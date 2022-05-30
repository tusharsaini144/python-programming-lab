import time

F=open("names.dat","r")

while(True):
	data=F.readline()
	if(data==""):break

	print(data,end='')

	time.sleep(1)
F.close()
