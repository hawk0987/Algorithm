import heapq
import sys

N = int(sys.stdin.readline())
study_time = []
for _ in range(N) :
    study_time.append(list(map(int, sys.stdin.readline().split())))
study_time.sort()

using_room = []
heapq.heappush(using_room, study_time[0][1])

for i in range(1, N) :
    if study_time[i][0] < using_room[0] :
        heapq.heappush(using_room, study_time[i][1])
    else :
        heapq.heappop(using_room)
        heapq.heappush(using_room, study_time[i][1])

print(len(using_room))
