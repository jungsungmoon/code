# from itertools import combinations
# from collections import deque
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    visited = [[0] * M for _ in range(N)]
    
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def dfs(x, y):
        visited[y][x] = 1
        
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            
            if (nx >= 0) and (nx < M) and (ny >= 0) and (ny < N):
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    dfs(nx, ny)
                    
    worms = 0
    
    for x in range(M):
        for y in range(N):
            if (graph[y][x] == 1) and (visited[y][x] == 0):
                dfs(x, y)
                worms += 1
            
    print(worms)
