from collections import deque

len_queue, N = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque()
[queue.append(i+1) for i in range(len_queue)]

total_cnt = 0
for num in nums :
    rotate_cnt = 0
    while queue[0] != num :
        queue.rotate(1)
        rotate_cnt += 1
    
    if len(queue) - rotate_cnt < rotate_cnt :
            rotate_cnt = len(queue) - rotate_cnt
    
    queue.popleft()
    total_cnt += rotate_cnt
print(total_cnt)
