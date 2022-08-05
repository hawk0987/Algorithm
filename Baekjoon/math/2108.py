import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []
for i in range(N) :
    li.append(int(sys.stdin.readline()))

li.sort()
a = int(round(sum(li)/N, 0))
d = li[-1]-li[0]
b = li[N//2]

cnt_li = Counter(li).most_common(2)
if N >1 :
    if cnt_li[0][1] == cnt_li[1][1] :
        c = cnt_li[1][0]
    else :
        c = cnt_li[0][0]
else :
    c = cnt_li[0][0]

print(a)
print(b)
print(c)
print(d)
