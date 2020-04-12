for T in range(int(input())):
	A=list(map(int,input().split()))
	N=A[0]
	trace=A[1]
	#print(N,trace)
	ps=[i for i in range(1,N+1)]
	lt=[]
	for _ in range(N):
		ps=ps[1:]+ps[:1]
		lt+=[ps[::]]
	#print(lt)
	ts=0
	for i,v in enumerate(lt):
		for j,w in enumerate(v):
			if i==j:
				ts+=w
				break
	if ts==trace:
		print('Case #{}: POSSIBLE'.format(T+1))
		for l in lt:
			for k in l:
				print(k,end=' ')
			print()
				pass
	else:
		print('Case #{}: IMPOSSIBLE'.format(T+1))
		
				