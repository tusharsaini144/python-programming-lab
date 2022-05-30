
# Program to print sum of key-value  pairs in dictionary
dictionary = {1: 10, 2: 20, 3: 30}
sumList = []
for key in dictionary:
	sumList.append(key + dictionary[key])

# Print the list
print("Key-value sum =",*sumList)
