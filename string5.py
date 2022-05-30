# function definition that will return 
# reverse string/digits 
def reverse(n):
    # to convert the integer value into string
    s=str(n) 
    p=s[::-1]
    return p 

# now, input an integer number
num = int(input('Enter a positive value: '))

# Calling the function and printing the result 
print('The reverse integer:',reverse(num))
