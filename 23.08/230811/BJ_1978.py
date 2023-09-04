n = int(input())

num_list = list(map(int, input().split()))

primes = [True] * 1001
primes[0] = False
primes[1] = False

for x in range(1001):
    if primes[x] == True:
        for y in range(2, (1000 // x)+1):
            primes[x * y] = False

cnt=0

for x in num_list:
    if primes[x]==True:
        cnt+=1

print(cnt)
