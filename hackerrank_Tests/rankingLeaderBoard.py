from collections import namedtuple
from random import randint
from operator import attrgetter
Fame = namedtuple('Fame','score,id,origin')
def getRank(alist):
    r=0
    lastScore=0
    for a in alist:
        if a.score!=lastScore:
            r+=1
    

def climbingLeaderboard(ranked, player):
    perspect=[]
    pool=[]
    pi=0
    for a in map(Fame._make, [[v,-1,'orig'] for k,v in enumerate(ranked)]):
        pool+=[a]
    for a in map(Fame._make, [[v,k,'players'] for k,v in enumerate(player)]):
        pool+=[a]
    
        newPool=sorted(pool,key=attrgetter('score'),reverse=True)
        print(newPool,end="-----------\n\n\n",sep='\n')
        for i,a in enumerate(newPool):
            if a.id==pi:
                perspect+=[i-1]
        pi+=1
    print(perspect)



climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])