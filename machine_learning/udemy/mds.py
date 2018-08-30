import numpy as np
from sklearn import manifold
import matplotlib.pyplot as plt
# %matplotlib inline
datum = np.loadtxt('park_time.csv', delimiter=",", usecols=range(1,11))
print(datum)