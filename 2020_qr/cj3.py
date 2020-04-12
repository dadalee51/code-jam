def can_fit(list,item):
	ok=True
	for l in list:
		if item[0]<l[1]:
			ok=False
			break
	return ok

for T in range(int(input())):
	A=[]
	for i in range(int(input())):
		K=list(map(int, input().split()))
		K+=[i]
		A+=[K]
	origA=A
	#print('A',A)
	#print('sortedA',sorted(A))
	A=sorted(A)
	res=[[],[]]
	ans=''
	for a in A:
		if can_fit(res[0],a):
			res[0]+=[a]
	#		print('res[0] now:',res[0])
		elif can_fit(res[1],a):
			res[1]+=[a]
		#	print('res[1] now:',res[1])
		else:
			ans='IMPOSSIBLE'
			break
	#print('res[0] now:',res[0])
	#print('res[1] now:',res[1])
	if ans != 'IMPOSSIBLE':
		for k in origA:
			if k in res[0]:
				ans+='C'
			elif k in res[1]:
				ans+='J'
	print('Case #{}: {}'.format(T+1,ans))