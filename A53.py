import heapq
N = int(input())

T = []
for _ in range(N):
  q = input().split()
  if q[0] == '1':
    heapq.heappush(T, int(q[1]))
  elif q[0] == '2':
    print(T[0])
  elif q[0] == '3':
    heapq.heappop(T)