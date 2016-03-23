import json
print "testing big numbers and bitwise in python"
print "1.", 1<<128
print "2.", -1 <<1
print "3.", 1 & -1
print "4.", -1 & 1
print bin(33)
for x in range(0, 3):
    print "We're on time %d" % (x)
larVal = 1 << 2
for x in xrange(larVal):
    print x
else:
    print 'Final x = %d' % (x)

t = 12345, 54321, 'hello!'
myDic_01 = dict([(t,"on now"),('sape', 4139), ('guido', 4127), ('jack', 4098)])
myDic_02 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print myDic_01[(t)]
#json.dumps(myDic_01) --doesnt work
print json.dumps(myDic_02)
print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print json.JSONEncoder().encode({"foo": ["bar", "baz"]})
"""doesnt work because sublime text"""
#s = raw_input('--> ')
#print s 

s = "hello world"
ss = set(s)
print ss
ss.remove('o')
print ss
sss = set("is a good thing 599")
print sss & set("i am a bad dog")

print set("good day today".split())

listA = "today good day apple seeding".split()
print listA
listA.reverse()
print listA
print "sorting listA:"
print sorted(listA)

#sort dictionaries
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print sorted_x

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print sorted_x



