#Head is 1, tail is 0
#sample space
S=[[1,1],[1,0],[0,1],[0,0]]
E1=[]
F1=[]
E2=[]
F2=[]
def intersection(A,B):
	I=[]
	for i in range(0,len(A)):
		if A[i] in B:
			I.append(A[i])
	return I
for i in range(0,len(S)):
#E: tail at one coin obviously other will be head
	if 0 in S[i] and 1 in S[i] :
		E1.append(S[i])
#F: head at one coin obviously other will be tail
	if 1 in S[i] and 0 in S[i]:
		F1.append(S[i])
#E: no tail
	if 0 not in S[i]:
		E2.append(S[i])
#F: no head
	if 1 not in S[i]:
		F2.append(S[i])
I1=intersection(E1,F1)
I2=intersection(E2,F2)

print("P(E1|F1) is",len(I1)/len(F1))
print("P(E2|F2) is",len(I2)/len(F2))
