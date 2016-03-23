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
			#d
			d=int(f.readline())
			#e
			e=[int(x) for x in f.readline().split()]
			print d, e
			ans = []
			while e:
				x = e.pop(0)
				for i in e:
					print "x=",x, ",i=" , i
					if i * 3 / 4 == x :
						ans.append(x)
						e.remove(i)
						break
			print ans


			ans = join(ans)
			fout.write("Case #"+str(ci+1)+": " + ans + "\n")	
	return;

#solve here.
#solve("test_in")
#solve("small_in")
solve("large")