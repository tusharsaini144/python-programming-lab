# function to check elements
def check_equal(a):
  return a[1:] == a[:-1]

# lists
x = [10, 20, 30, 40,50]
y = [10, 20, 20, 20, 20]
z = [10, 10, 10, 10, 10]

# check how [1:] and [:-1] wors?
print("x: ", x)
print("x[1:]: ", x[1:])
print("x[:-1]: ", x[:-1])
print("check_equal(x): ",check_equal(x))
print()

print("y: ", y)
print("y[1:]: ", y[1:])
print("y[:-1]: ", y[:-1])
print("check_equal(y): ",check_equal(y))
print()

print("z: ", z)
print("z[1:]: ", z[1:])
print("z[:-1]: ", z[:-1])
print("check_equal(z): ",check_equal(z))
print()
