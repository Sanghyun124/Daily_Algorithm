n=int(input())
scores=list(map(int,input().split()))

scores.sort()

max_score=scores[-1]

res=0

for x in range(len(scores)):
    res+=scores[x]/max_score*100

print(res/len(scores))