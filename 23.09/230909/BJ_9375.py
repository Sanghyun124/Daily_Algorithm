import sys

input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    newDict={}
    ans=1
    for _ in range(n):
        c=list(input().split())
        if c[1] in newDict.keys():
            newDict[c[1]].append(c[0])
        else:
            newDict[c[1]]=[c[0]]
    for key in newDict.keys():
        ans *= len(newDict[key]) + 1
    print(ans-1)

