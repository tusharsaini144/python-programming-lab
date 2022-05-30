# Define a function to convert
# celsius temperature to Fahrenheit
def Celsius_to_Fahrenheit(c) :
    
    f = (9/5)*c + 32
    
    return f
    
# Define a function to convert
# Fahrenheit temperature to Celsius
def Fahrenheit_to_Celsius(f) :
    
    c = (5/9)*(f - 32)
    
    return c
    

# Driver Code
if __name__ == "__main__" :
    
    c = 36
    print(c, "degree celsius is equal to:",Celsius_to_Fahrenheit(c),"Fahrenheit")
    
    f = 98
    print(f,"Fahrenheit is equal to:",Fahrenheit_to_Celsius(f),"degree celsius")
