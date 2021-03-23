#count valleys
path='UUDDDDUUDDDDDUDDUUUUU'
def countingValleys(steps, path):
    #cnt+=1 every 'DU'
    cnt=0
    sea=0
    state=-1 #0 enters valley, 1,leaves.
    for i in range(steps):
        if path[i]=='U':
            sea+=1
        else:
            sea-=1
        if path[i]=='D' and sea<=0:
            state=0
        if state==0 and path[i]=='U' and sea==0:
            cnt+=1
    return cnt

print(countingValleys(len(path),path))