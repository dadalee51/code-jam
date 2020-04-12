import sys
#print(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#x = (2**a[1])
#print(x)

#c = [0 for i in range(x)]
#d = c[:]
#print(c)
#get 1s representation from a[1]
#sm is sum map
cmax=0
mimax=0
sm=2**a[1]-1
#print(bin(sm)) 0b1111
while sm > 0:
    lump=0
    for i in range(a[1]):
        if (1<<i & sm):
            lump+=b[i]
            if lump>a[0]:
                print('lump:',lump)
                break
    if lump < a[0]:
 #       c[sm]=1
        if lump>cmax:
            print('sm:',sm)
            cmax=lump
            mimax=sm
            print('cmax:',cmax)
            print('mimax:',mimax)
 #           d[sm]=cmax
            #print(bin(sm))
    sm=sm//100
#print(c)
#max list view
#print(d)

#print(d.index(max(d)))
#mi = d.index(max(d))
#print(bin(mi))
res=0
resa=[]
for i in range(a[1]):
    res+=(mimax>>i & 1)
    if mimax>>i & 1:
        resa+=[i]

print(res)
print(*resa)
