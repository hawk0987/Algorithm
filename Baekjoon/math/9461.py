T = int(input())

p = [0 for i in range(101)]
p[0] = 1
p[1] = 1
p[2] = 1

for i in range(3, 101) :
    p[i] = p[i-3] + p[i-2]

for _ in range(T) :
    num = int(input())
    print(p[num-1])
