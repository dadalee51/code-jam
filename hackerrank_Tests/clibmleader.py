def climbingLeaderboard(ranked, player):
    pers=[]
    a=set()
    for i in ranked:
        a.add(i)
    b=sorted(a,reverse=True)
    #print(b)
    for p in player:
        found=False
        for i,c in enumerate(b):
            if p>=c:
                pers+=[i+1]
                b.append(p)
                found=True
                break
        if not found:
            pers+=[len(b)+1]
        #print(b)
        #print('=-===',pers)
                
    #print(pers)
    return pers

climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])
