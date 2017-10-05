# python 3.6

import numpy as np 

arr = np.random.normal(size=100)
vfunc = np.vectorize(lambda x: x if x > 0 else 0)
print(vfunc(arr))