#Python code to find the number occurring odd number of times using lambda expression and reduce() function
# python-programming-lab
from functools import reduce

def findElement(list1):
	print (reduce(lambda x, y: x ^ y, list1))

# Main function
if __name__ == "__main__":
	list1 = [10, 20, 10, 30, 30, 20, 20]
	findElement(list1)
