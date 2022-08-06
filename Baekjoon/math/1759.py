L, C = map(int, input().split())
str_li = list(map(str, input().split()))
str_li.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
temp = []
visited = [False for i in range(C)]

def dfs(start, cnt) :
    # 지정한 글자가 되었을 때
    if cnt==L :
        v = 0
        c = 0
        # 찾은 암호 temp
        for i in temp :
            if i in vowels :
                v += 1
            else :
                c += 1
        # 모음1개이상 자음2개이상 확인
        if  v >= 1 and c >= 2 :
            for i in temp :
                print(i, end='')
            print()
        return
    
    #dfs 알고리즘
    for i in range(start, C) :
        if not visited[i] :
            visited[i] = True
            temp.append(str_li[i])
            dfs(i+1, cnt +1)
            temp.pop()
            visited[i] = False

dfs(0, 0)
