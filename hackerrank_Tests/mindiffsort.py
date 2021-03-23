def pickingNumbers(a):
    a.sort()
    print(a)
    mcnt=0
    for i in range(len(a)-1):
        cnt=0
        for j in range(i,len(a)):
            if a[i]==a[j] or a[i]==a[j]-1:
                print(a[i],a[j])
                cnt+=1
        mcnt=max(cnt,mcnt)
    print(mcnt)
    return mcnt

pickingNumbers([1,2,3,3,3,3,3,3,3,2,2,2,2,2,4,24,234,234,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])