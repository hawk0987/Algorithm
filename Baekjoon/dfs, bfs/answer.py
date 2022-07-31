nodes = int(input())
lines = int(input())
graph = [[] * i for i in range((nodes+1))]
for i in range(lines) :
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    graph[node1].sort()
    graph[node2].sort()

visited = [False] * (nodes+1)
def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            visited[i] = True
            dfs(graph, i, visited)
    
dfs(graph, 1, visited)
print(sum(visited)-1)
