# python program to check whether a string 
# contains only digits or not 

# variables declaration & initializations
str1 = "8789"
str2 = "Hello123"
str3 = "123Hello"
str4 = "123 456"    #contains space 

# checking
print("str1.isdigit(): ", str1.isdigit())
print("str2.isdigit(): ", str2.isdigit())
print("str3.isdigit(): ", str3.isdigit())
print("str4.isdigit(): ", str4.isdigit())

# checking & printing messages
if str1.isdigit():
    print("str1 contains a number")
else:
    print("str1 does not contain a number")

if str2.isdigit():
    print("str2 contains a number")
else:
    print("str2 does not contain a number")

if str3.isdigit():
    print("str3 contains a number")
else:
    print("str3 does not contain a number")

if str4.isdigit():
    print("str4 contains a number")
else:
    print("str4 does not contain a number")
