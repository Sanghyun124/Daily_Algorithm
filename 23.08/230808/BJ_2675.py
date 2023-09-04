t = int(input())
for _ in range(t):
    ary = list(input().split())
    s = ''
    for x in ary[1]:
        for _ in range(int(ary[0])):
            s += x
    print(s)
