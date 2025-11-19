from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (N+1)

def dfs(node):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            
dfs(1)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)
                
bfs(1)

print(sum(visited)-1)
