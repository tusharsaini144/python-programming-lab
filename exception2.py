# Python program to illustrate ValueError Exception 

# Try Block Starts
try:
    # Taking input from the user ... 
    # The input strictly needs to be an integer value
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    # Adding the two numbers and printing their result.
    numSum = num1 + num2
    print("The sum of the two numbers is ",numSum)
    
# except block 
except ValueError as ex:
    print(ex)
