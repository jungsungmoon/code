import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N+1)

nodes = []

def dfs(depth):
    if depth == M:
        print(*nodes)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            nodes.append(i)
            
            dfs(depth+1)
            
            nodes.pop()
            visited[i] = 0
            
dfs(0)
