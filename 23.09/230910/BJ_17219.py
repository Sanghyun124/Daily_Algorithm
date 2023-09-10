# import sys
#
# input = sys.stdin.readline
#
# newDict={}

# n,m=map(int,input().split())
# for _ in range(n):
#     temp=list(input().split())
#     t=0
#     print(temp)
#     for x in range(len(temp[0])):
#         t+=(x+1)*(ord(temp[0][x])*ord(temp[0][x]))
#     newDict[t]=temp[1]
#
# print(newDict)
#
# for _ in range(m):
#     temp=input().rstrip()
#     t=0
#     print(temp)
#     for x in range(len(temp)):
#         t += (x+1) * (ord(temp[x]) * ord(temp[x]))
#     print(newDict[t])

import sys

input = sys.stdin.readline

newDict={}

n,m=map(int,input().split())
for _ in range(n):
    temp=list(input().split())
    newDict[temp[0]]=temp[1]

for _ in range(m):
    temp=input().rstrip()
    print(newDict[temp])