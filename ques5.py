r1=int(input())
r2=int(input())
c1=int(input())
c2=int(input())
r1,c1=dimension(A)
r2,c2=dimension(B)
if c1==r2:
	result=[[0,0,0],
		[0,0,0],
		[0,0,0]]
	for i in range(r1):
		for j in range(c2):
			for k in range(c1):
				result[i][j]+=A[i][k]*B[k][j]
else:
	print('dimension not match')
print(result)
