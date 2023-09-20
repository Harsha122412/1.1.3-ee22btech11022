from scipy.stats import bernoulli
import numpy as np

x =[]
num=0
for i in range(0,12):
	x.append(bernoulli.rvs(size=10000,p=0.1))
for i in range(0,10000):
	c=0
	for j in range(0,12):
		if x[j][i]==1:
			c=c+1
	if c==9:
		num=num+1
print(num/10000)
