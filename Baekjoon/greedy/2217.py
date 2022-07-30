N = int(input())
ropes = []

for i in range(N) :
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)
weight = ropes[0]

for i in range(1, len(ropes)) :
    if ropes[i] * (i+1) >= weight:
        weight = ropes[i] * (i+1)

print(weight)
