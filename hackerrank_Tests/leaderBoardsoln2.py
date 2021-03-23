'''
6
100 100 100 100 100 100 90 90 80 75 60
5
50 65 77 90 102

'''

#!/bin/python3


#n = int(input().strip())
#scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
#m = int(input().strip())
#alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
scores=[100,100,100,100,100,90,90,80,75,60]
alice=[50,65,77,90,102]

scores = sorted(list(set(scores)))[::-1]
print("scores:",scores)
back = len(scores) - 1
print("back:",back,"scores[back]:",scores[back])
for a in alice:
    while back >= 0 and a > scores[back]:
        #print(f'back is {back} geq than 0 and a is greater than the one we are looking at:',scores[back])
        back -= 1
    if scores[back] == a:
        print(back + 1)
    else:
        print(back + 2)