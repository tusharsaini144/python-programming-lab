# python-programming-lab
""" Python program to swap the position 
of dictionary items"""
myDict = {'Scala': 2, 'Javascript': 5, 'Python': 8, 'C++': 1, 'Java': 4}
i, j = 2, 4 
tupList = list(myDict.items())
tupList[i], tupList[j] = tupList[j], tupList[i]
swappedDist = dict(tupList)
print("Initial dictionary = ", end = " ")
print(myDict)
print("Dictionary after swapping = ", end = " ")
print(swappedDist)
