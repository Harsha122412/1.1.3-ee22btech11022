import numpy as np

def mean(a,b):
	return np.sum(a@b)
def Ex2(a,b):
	a2=np.square(a)
	return np.sum(a2@b)
x=np.array([0,1,2,3,4,5])
px=np.array([float(1/6),float(5/18),float(2/9),float(1/6),float(1/9),float(1/18)])

variance=Ex2(x,px)-(mean(x,px)*mean(x,px))
print("Variance of given distribution is",variance)
