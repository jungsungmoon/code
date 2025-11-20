# from itertools import combinations
from collections import deque
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

max_num = 100000

visited = [0] * (max_num+1)

def bfs():
    q = deque([N])
    
    while q :
        node = q.popleft()
        if node == K:
            print(visited[node])
            break
        for next_node in (node-1, node+1, 2*node):
            if 0 <= next_node <= max_num and not visited[next_node]:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
                
bfs()
