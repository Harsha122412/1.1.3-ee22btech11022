from scipy.stats import bernoulli
import numpy as np
x = bernoulli.rvs(size=(12, 1000000),p=0.1)
c1 = np.sum(x, axis=0)
c= np.sum(c1 == 9)
probability =c / 1000000
print(probability)
