Write a NumPy program to shuffle numbers between 0 and 10 (inclusive).
import numpy as np
x = np.arange(10)
np.random.shuffle(x)
print(x)
print("Same result using permutation():")
print(np.random.permutation(10))
