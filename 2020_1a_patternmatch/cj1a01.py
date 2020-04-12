T=int(input())
for t in range(T):
	ans=''
	XANS=[]
	xans=[]
	noans=False
	N=int(input())
	#l8eft and right possibility lists

	X=[]
	
	for n in range(N):
		Q=[]
		M=[]
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
			M+=[[k,q]]
		#print(f'M={M}')
		M=sorted(M,key=lambda p:len(p[1]),reverse=False)
		X+=[M]
		print(f'X:{X}')
	#add to list, sortable
	#X has each side of the star with progressively sorted increments.
	print(f'X={X}')
	#traverse list, if a is substring of a+1, maxString is a+1.
	Z=[[] for z in range(c+1)]
	
	print('Z was {Z}')
	for x in X:
		#split x by first nuber and assign to each group.
		print(f'x:{x}')
		for a in x:
			Z[a[0]]=[a[1]]
		print('Z:',Z)
		if noans: break
		k=1
		while k < len(x):
			print(f'...is "{x[k-1][1]}" in "{x[k][1]}"?')
			if x[k-1][1]=='' or x[k-1][1] in x[k][1]:
				xans=[x[k][1]]
				print(f'xans is now {xans}')
			else:
				noans=True
				break
			k+=1
		XANS+=[xans]
	print(XANS)
	for x in XANS:
		if x != '':
			pass
			#ans+=x
	if noans:
		ans='*'
	print('Case #{}: {}'.format(t,ans))