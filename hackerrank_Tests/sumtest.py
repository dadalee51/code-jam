#how to calculate the various sums of 2 and 3s?
cnt=0
for i in range(20):
    for j in range(20):
        print(i*2+j*3,end='')
        if i*2+j*3 == 16:
            print('*',end='')
            cnt+=1
        else:
            print(' ',end='')
    print('')
    
print(cnt)