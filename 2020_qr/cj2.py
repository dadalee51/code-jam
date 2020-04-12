import re
for T in range(int(input())):
	a=input()
	out=''
	prep=0
	post=0
	s=0 #state from -1 to 9
	if a[0]!='0': a='0'+a ; prep=1
	if a[-1]!='0':a=a+'0' ; post=1
	for v in a:
		d=int(v)-s
		if d>0:
			for b in range(d):
				out+='('
		if d<0: 
			for b in range(abs(d)):
				out+=')'
		out+=v
		
		s=int(v)
	#print(out)
	if prep: out=out[1:]
	if post: out=out[:-1]
	print('Case #{}: {}'.format(T+1,out))
	
	