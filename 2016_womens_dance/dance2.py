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
			left = K + 1
			right = -1
			if K ==1 : right = D
			else : right = K - 1
			newN = N % D
			# if N is greater than D, N = N mod D
			#after each round, if K is odd, its neigh adds two mod D
			#if K is even, its neib sub two, if lessor than 0, add D
			if K % 2 == 1:
				left += 2 * newN 
				left %= D
				right += 2 * newN 
				right %= D
			else:
				left -= 2 * newN 
				left %= D
				right -= 2 * newN 
				right %= D

			if left == 0 : left = D
			if right == 0 : right = D

			print left
			print right
			fout.write("Case #"+str(ci+1)+": " + str(left) + " " + str(right) + "\n")	
	return;

#solve here.
#solve("test")
solve("small")
solve("large")