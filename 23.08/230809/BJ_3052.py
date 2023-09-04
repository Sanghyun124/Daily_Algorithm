temp=[]

for _ in range(10):
    x=int(input())
    if x%42 in temp:
        pass
    else:
        temp.append(x%42)

print(len(temp))