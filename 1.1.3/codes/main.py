import numpy as np

np.set_printoptions(precision=2)
A= np.array([1,-1])
B= np.array([-4,6])
C= np.array([-3,-5])

Mat = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])

rank = np.linalg.matrix_rank(Mat)

if (rank<=2):
	print("Hence proved that points A,B,C in a triangle are collinear")
else:
	print("The given points are not collinear")
