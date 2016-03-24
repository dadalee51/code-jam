import fileinput
import collections

def join(arr):
	outStr=""
	for i in arr:
		outStr= outStr + str(i) + " "
	return outStr.strip()


def solve(fileName):
	fout = open(fileName+".pythout", 'w')
	with open(fileName, 'r') as f:
		T = int(f.readline())
		for ci in range(T):
			print "----------case ",ci
			m = f.readline().split()
			D = int(m[0])
			K = int(m[1])
			N = int(m[2])
			v = [x+1 for x in range(D)]
			print v
			for i in range(N):
				if i%2==0:
					for j in range(D/2):
						a = v[2*j]
						v[2*j] = v[2*j+1]
						v[2*j+1] = a
				else:
					for j in range(D/2):
						a = v[2*j]
						v[2*j] = v[2*j-1]
						v[2*j-1] = a
				
			print v
			print "K %d is at " % K, v.index(K)
			one = v.index(K)+1 % D
			two = v.index(K)-1 % D
			print one
			print two

			fout.write("Case #"+str(ci+1)+": " + str(one) + " " + str(two) + "\n")	
	return;

#solve here.
solve("test")
#solve("small")
#solve("large")