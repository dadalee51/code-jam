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
		caseCnt=int(line)
		#print caseCnt
		for caseIdx in range(caseCnt):
			#init datastruct
			
			#no. flav
			flav = int(f.readline())
			#no. cust
			cust = int(f.readline())
			data= {y:[] for y in range(flav)}
			custcon = {x:[] for x in range(cust)}
			max_len = -1
			#print "data is:",data
			for custIdx in range(cust): #for each customer
				af = f.readline().split()
				maf =  int(af[0])
				if max_len < maf : max_len = maf
				for i in range(int(af[0])):
					x = int(af[2*i+1])
					y = int(af[2*i+2])
					#print x, y
					data[x-1].append({custIdx:y})
					custcon[custIdx].append({x-1:y})
			answer = [-1] * flav
			custSatSum = 0
			newData = []
			for i in range(1, max_len+1):
				for k, choiceCnt in custcon.iteritems():
					if(i==len(choiceCnt)):
						print "choiceCnt",choiceCnt
						newData.append(choiceCnt)
						satFlag = False
						for sing in choiceCnt:
							for k2,v2 in sing.iteritems():
								if (answer[k2] == -1) : answer[k2] = v2 
								if (v2 == answer[k2]) :
									#print "v2 is:", v2, " answer[",k2,"] is:", answer[k2]
									satFlag = True
						if (satFlag) : 
							custSatSum+=1
							print "custSatSum",custSatSum
			print "new data:", newData

			for i in range(len(answer)):
				if (answer[i]==-1) : answer[i]=0
			print "answer" ,answer, " sati:", custSatSum					
			outStr = join(answer)
			if cust == custSatSum :
				print "Case #"+str(caseIdx+1)+": " + outStr
				fout.write("Case #"+str(caseIdx+1)+": " + outStr + "\n")
			else :
				print "Case #"+str(caseIdx+1)+": IMPOSSIBLE"
				fout.write("Case #"+str(caseIdx+1)+": IMPOSSIBLE" + "\n")	
	return;

#solve here.
#solve("test_in")
solve("small_in")
#solve("large_in")