list1 = [10, 15, 20, 15, 30]
ele = 15

# Lambda function to check an element
# in the list
countFunc = lambda list1 , ele : list1.count(ele)

count = countFunc(list1, ele)

if(count):
	print("Yes, total count of", ele, "is",count)
else:
	print("No")
