import sys

input=sys.stdin.readline

class minHeap:

    def __init__(self):
        self.q=[0]

    def insert(self,x):
        # 맨 마지막에 원소 추가
        self.q.append(x)
        #부모보다 클 때 까지 이동
        idx=len(self.q)-1 # 현재 인덱스
        while 1< idx:
            #부모와 비교 (부모 : 현재 // 2):완전이진트리 기반이므로
            if self.q[idx] < self.q[idx//2]: # 부모가 더 크면 swap
                self.swap(idx,idx//2)
                idx=idx//2
            else: # 부모가 더 작으면 끝
                break

    def delete(self):
        # 배열이 비었을때
        if len(self.q)==1:
            return 0
        # 맨 처음이랑 맨 마지막 swap
        self.swap(1,-1)
        # 맨 마지막이 최소이므로 pop
        _min=self.q.pop()
        #재정렬
        self.sort()
        return _min

    def swap(self, i1, i2):
        self.q[i1],self.q[i2] = self.q[i2],self.q[i1]

    def sort(self):
        _idx = 1

        while len(self.q) > 1:
            _next = _idx
            if _idx * 2 < len(self.q) and self.q[_idx * 2] < self.q[_next]:
                _next = _idx * 2

            if _idx * 2 + 1 < len(self.q) and self.q[_idx * 2 + 1] < self.q[_next]:
                _next = _idx * 2 + 1

            if _next != _idx :
                self.swap(_idx, _next)
                _idx = _next

            else:
                break


n=int(input())

heap=minHeap()

for _ in range(n):
    x=int(input())
    if x==0:
        print(heap.delete())
    else:
        heap.insert(x)
