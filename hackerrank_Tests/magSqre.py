# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    flipsched=[0,1,0,1,2,0,1,0,1]
    minac=100#start with large number
    for f in flipsched:
        ac=0
        for i in range(3):
            for j in range(3):
                ac+=abs(t[i][j]-s[i][j])
        minac = min(ac,minac)
        flip(t,f)
        print('minac:',minac)
    return minac
def flip(t,direction):
    if direction==0:
        temp=t[2]
        t[2]=t[0]
        t[0]=temp
    elif direction==1:
        for i in range(len(t)):
            temp=t[i][2]
            t[i][2]=t[i][0]
            t[i][0]=temp
    elif direction==2: #diagonal
        temp=t[0][1]
        t[0][1]=t[1][0]
        t[1][0]=temp
        temp=t[1][2]
        t[1][2]=t[2][1]
        t[2][1]=temp
        temp=t[0][2]
        t[0][2]=t[2][0]
        t[2][0]=temp
    #print("new t:",t)
    for a in t:
        print(a)
    print('====',direction)
s=[[1,6,8],[2,5,7],[3,4,9]]
t=[[8,3,4],[1,5,9],[6,7,2]]
          

formingMagicSquare(s)