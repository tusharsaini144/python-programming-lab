# Python program to shuffle dictionary Values...
myDict = {'Scala': 2, 'Javascript': 1, 'Python': 8, 'C++': 1, 'Java': 4}

# extracting unique values using set comprehension
uniqueValues = list({val for val in myDict.values() })
print("Dictionary = ", end = " ")
print(myDict)
print("Unique Values = ", end = " ")
print(uniqueValues)
