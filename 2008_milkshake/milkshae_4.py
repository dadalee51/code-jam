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
		line = f.readline()
		cn=int(line)
		#print caseCnt
		for ci in range(cn):
			print "----------case ",ci
			#no. flav
			flav = int(f.readline())
			#no. cust
			cust = int(f.readline())
			#for each cust, build a set and sort it at the end of interpretation
			dn = []
			for ia in range(cust):
				c = [int(x) for x in f.readline().split()][1:]
				dn.append(c)
			#sort by len and then first malt value
			dn = sorted(dn, key=lambda x : (len(x), x[1]) )
			print dn


			fout.write("Case #"+str(ci+1)+": IMPOSSIBLE" + "\n")	
	return;

#solve here.
solve("test_in")
#solve("small_in")
#solve("large_in")