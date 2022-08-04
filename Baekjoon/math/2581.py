M = int(input())
N = int(input())
li = []

for num in range(M, N+1) :
    if num==1 :
        continue

    for i in range(2, int(num**0.5)+1) :
            if num%i == 0 :
                break
    
    else :
        li.append(num)

if not li :
    print(-1)
else :
    print(sum(li))
    print(min(li))
