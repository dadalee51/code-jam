

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    a=((m+s-1)%n)
    if a==0:
        a=n
    print(a)
    return a


saveThePrisoner(3, 2, 2)

    
