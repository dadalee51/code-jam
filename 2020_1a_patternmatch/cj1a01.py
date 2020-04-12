T=int(input())
for t in range(T):
	limN=20
	ans=''
	XANS=[]
	xans=[]
	noans=False
	N=int(input())
	X=[[]for _ in range(limN)]
	for n in range(N):
		Q=[]
		timer=0
		S=input()
		#merge any multiple * into one.
		P=''
		for k,s in enumerate(S):
			if k+1 < len(S):
				if S[k]==S[k+1]=='*':
					continue
				else:
					P+=s
			else:
				P+=s
		S=P		
		#sanitised S.
		c=S.count('*')
		#create number of lists according to num of stars.
		for i in range(c+1):
			Q=list(S.split('*'))			
		for k,q in enumerate(Q):
			X[k]+=[q]
	X=[x for x in X if x!=[]]
	print(f'X={X}')
	#output
	Z=[[] for z in range(limN)]
	print(f'Z was {Z}')
	
	#if first or last non-compatNumSeq-existsEmpty > 1 then impossible.
	#else if lenX is > 2 then any block in btwn can be joined together.
	for i,x in enumerate(X):
		if i==0 or i==len(X)-1:
			if x:print(f'x:{x}')
			B=sorted(x,key=lambda p:len(p),reverse=False)
			if B:print(f'B:{B}')
			for j,b in enumerate(B):
				if j > 0:
					if B[j-1] in B[j]:
						Z[i]=B[j]
						print(f'Z update{Z}')
					else:
						noans=True
			if Z[i]: print(f'Z[{i}]:{Z[i]},noans:{noans}')
			if noans: break
		elif len(X)>2:
			Z[i]+=x
			print(f'Z is lenx>2 {Z}')
		else:
			print(f'Z else update {Z}')
			Z[i]+=x
	
	if noans:
		ans='*'
	else:
		print(f'Z is now {Z}')
		for z in Z:
			if z!=[]:
				ans+=z
	print('Case #{}: {}'.format(t+1,ans))