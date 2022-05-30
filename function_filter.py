#  program to filter even value  
def filtereven(data):
    even=[]
    for n in data:
        if n%2==0:
            even.append(n)
    return even
# List of fibonacci values
fibo = [0,1,1,2,3,5,8,13,21,34,55]

print("List of fibonacci values :",fibo)
evenFibo = filtereven(fibo)
print("List of even fibonacci values :",evenFibo)
