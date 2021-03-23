'''
6
100 90 90 80 75 60
5
50 65 77 90 102
'''

from bisect import bisect
n = int(input().strip())
scores = sorted(set(map(int, input().split())))
m = int(input().strip())
alice = map(int, input().split())

print(scores)

print(alice)

print(scores[::-1])
for k in alice:
    print("k:",k,"len(scores):",len(scores),"bisect(scores, k):",bisect(scores, k))
    #print(len(scores) - bisect(scores, k) + 1)