list = [11, 22, 33, 44, 55]

# print original list
print "Original list:"
print (list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)

# print list after removing EVEN elements
print( "list after removing EVEN numbers:")
print (list)
