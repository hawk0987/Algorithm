cook_sec = int(input())
a = 0
b = 0
c = 0

if cook_sec >= 300 :
    a += cook_sec // 300
    cook_sec -= a*300
    b += cook_sec // 60
    cook_sec -= b*60
    c += cook_sec // 10
    cook_sec -= c*10
elif cook_sec >= 60 :
    b += cook_sec // 60
    cook_sec -= b*60
    c += cook_sec // 10
    cook_sec -= c*10
else :
    c += cook_sec // 10
    cook_sec -= c*10

if cook_sec > 0 :
    print(-1)
else :
    print(a, b, c)
