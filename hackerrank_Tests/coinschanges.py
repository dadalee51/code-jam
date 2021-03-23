a=int(input('What amount?'))
coins=[1,2,3]
acc=[[0 for i in range(a+1)] for j in coins]
#print(acc)
for i,k in enumerate(acc): #coin type
    for p,q in enumerate(k): #amount
        #print(i,p,q,coins[i])
        if p % coins[i] ==0:
            acc[i][p]+=1
        if i>0 and p<coins[i]:
            acc[i][p]=acc[i-1][p]
        if i>0 and p>=coins[i]:
            acc[i][p]=acc[i-1][p]+acc[i][p-coins[i]]
ans=-1 
for u in acc:
    print(u)
    ans=u[-1]

print('this many ways:',ans)

def tra(p):
    for a in p:
