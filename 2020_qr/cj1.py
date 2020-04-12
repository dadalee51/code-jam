dbg=0
for T in range(int(input())):
	a=[]
	
	for _ in range(int(input())):
		a+=[list(map(int, input().split()))]		
	if dbg:print(a)
	n=len(a)
	R=[[0] for _ in range(n)]
	C=[[0] for _ in range(n)]
	k=0
	r=[0 for _ in range(n)]
	c=[0 for _ in range(n)]
	numr=0
	numc=0
	for i in range(n):
		for j in range(n):
			if i==j:
				k+=a[i][j]
			if a[i][j] in R[i]:
				r[i]+=1
			else:
				R[i]+=[a[i][j]]			
			if a[i][j] in C[j]:
				c[j]+=1
			else:
				C[j]+=[a[i][j]]
	for i in range(n):
		if r[i]>0:numr+=1
		if c[i]>0:numc+=1
	if dbg:print('R={}, r={}'.format(R,r))
	if dbg:print('C={}, c={}'.format(C,c))
	print('Case #{}: {} {} {}'.format(T+1,k,numr,numc))