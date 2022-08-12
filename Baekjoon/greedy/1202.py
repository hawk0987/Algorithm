import heapq
import sys
N, K = map(int, sys.stdin.readline().split())

jewels = []
for _ in range(N) :
    jewels.append(list(map(int, sys.stdin.readline().split())))

bags = []
for _ in range(K) :
    bags.append(int(sys.stdin.readline()))

jewels.sort()
bags.sort()



total = 0
tmp = []

for bag in bags : # 모든 가방을 확인해보면서
    while jewels and bag >= jewels[0][0]: # 보석의 무게가 가방에 들어갈 수 있는 동안
        heapq.heappush(tmp, -jewels[0][1])  # 임시 heap에 보석의 가격을 push
        heapq.heappop(jewels) # 해당 보석은 넣을 수 있으니 제거

    if tmp :
        total += heapq.heappop(tmp)
    elif not jewels :
        break

print(-total)
