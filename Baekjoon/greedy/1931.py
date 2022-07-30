N = int(input())
time = []
for i in range(N) :
    a, b = map(int, input().split())
    time.append([a, b])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

count = 0
before_end = 0
for start, end in time :
    if start >= before_end:
        before_end = end
        count += 1
            
print(count)
