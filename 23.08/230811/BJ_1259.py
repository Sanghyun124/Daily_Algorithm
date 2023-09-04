from copy import deepcopy

while True:
    s=input()
    if s=='0':
        break

    temp=deepcopy(s)
    if temp[::-1]==s:
        print('yes')
    else:
        print('no')