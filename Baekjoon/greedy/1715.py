import sys
import heapq

N = int(sys.stdin.readline())
cards = []
for _ in range(N) :
    heapq.heappush(cards, int(sys.stdin.readline()))

if N == 1 :
    print(0)
else :
    total = 0
    while len(cards) > 1 :
        min1 = heapq.heappop(cards)
        min2 = heapq.heappop(cards)
        total += min1 + min2
        heapq.heappush(cards, min1 + min2)

    print(total)
