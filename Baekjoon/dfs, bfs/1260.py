from collections import deque

nodes, lines, start = map(int, input().split())
graph = [[] * i for i in range((nodes+1))]
for i in range(lines) :
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                q.append(i)
                visited[i] = True

visited = [False] * (nodes+1)
dfs(graph, start, visited)
print()
visited = [False] * (nodes+1)
bfs(graph, start, visited)
