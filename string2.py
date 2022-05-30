def slice(str, n):
    if len(str) < n:
        n = len(str)
    front = str[:n]
    return front


print (slice('Chocolate', 5))
print (slice('IncludeHelp', 7))
print (slice('Hello', 10)) 
