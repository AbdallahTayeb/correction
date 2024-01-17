import os 
import numpy as np 

a = int(os.environ["a"])
b = int(os.environ["b"])

print(a*b)
print(f'log(ab) = {np.log(a*b)}')
print(f'log(a) + log(b) = {np.log(a) + np.log(b)}')