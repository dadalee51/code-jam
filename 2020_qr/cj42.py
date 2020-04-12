class t2m:
	def __init__(self,trace,matrix):
		self.t=trace
		self.m=matrix
	def __repr__(self):
		return self.t+''+self.m
class s2d:
	def __init__(self):
		
		
def make_sqr(sd,N,out):
	for _ in range(N):
		sd=sd[1:]+sd[:1]
		out+=[sd[::]]
	return out

#swap two number in a line
def swap_ij(list,i,j):
	a=list[i]
	list[i]=list[j]
	list[j]=a
	return list

def swap_row(list,i,j):
	tr=[]
	tr=list[i]
	list[i]=list[j]
	list[j]=tr
	return list

def swap_col(list,i,j,N):	
	tc=[]
	for r in range(N):
		tc[r]=list[r][i]
		list[r][i]=list[r][j]
		list[r][j]=tc[r]
	
def rotate_rnd(list,dir=1):
	if dir==1:#left
		list=list[1:]+list[:1]
	else:#right
		list=list[:1]+list[1:]
	return list

def get_trace(list,N):
	sum=0
	sum2=0
	for i in range(N):
		for j in range(N):
			if i==j:
				sum+=list[i][j]
			if i==N-j:
				sum2+=list[i][j]
	return sum,sum2

for T in range(int(input())):
	A=list(map(int,input().split()))
	N=A[0]
	trace=A[1]
	print(N,trace)
	#create a base case.
	lt=[]
	ps=[i for i in range(1,N+1)]
	lt=make_sqr(ps,N,lt)
	
	print('lt:',lt)
	print('trace:',get_trace(lt,N))
	for i in range(N):
		for j in range(N):
			if i < j:
				