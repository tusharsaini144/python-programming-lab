# Python program to sort dictionary key and values list

# Creating a list with list as values
myDict = {'john' : [70, 82, 55], 'ram' : [92, 99, 98], 'jane' : [65, 34, 76]}
print("Initially the dictionary is " + str(myDict))

# Sorting dictionary
sortedDict = dict()
for key in sorted(myDict):
	sortedDict[key] = sorted(myDict[key])

# Printing sorted dictionary 
print("Dictionary after sort of key and list value : " + str(sortedDict))
