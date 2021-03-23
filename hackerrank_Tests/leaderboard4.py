#return position of the closest value to v
def bs(l,v):
    a1=0
    a2=len(l)-1
    m=(a1+a2)//2
    found=False
    while not found:
        lastm=m
        print(f'bs, v:{v},a1:{a1}, a2:{a2}, m:{m}, lastm:{lastm}')
        if v>=l[a1]:
            return a1
        elif v<=l[a2]:
            return a2+1
        elif v<=l[m] and v>l[a2]:
            a1=m
            m=(a1+a2)//2+1
        elif v<=l[a1] and v>l[m]:
            a2=m
            m=(a1+a2+1)//2
        print(f'endbs,v:{v},a1:{a1},a2:{a2},m:{m},lastm:{lastm}')
        if lastm==m:
            found=True
            return m

def climbingLeaderboard(ranked, player):
    pers=[]
    sorked=sorted(set(ranked),reverse=True)
    print(sorked)
    
    #test # print(bs(sorked,105))
    #print(a)
    for p in player:
        r=bs(sorked,p)
        print(r)
        if len(sorked)<=r:
            sorked.insert(r,p)
            pers+=[r]
        elif p == sorked[r-1]:
            pers+=[r-1]
        elif p != sorked[r]:
            sorked.insert(r,p)
            pers+=[r]
        else:
            pers+=[r]
        print(sorked)
    print(pers)
    for i,a in enumerate(pers):
        pers[i]+=1
    print(pers)
    return pers
        
    

climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])
print('--------')
climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])


