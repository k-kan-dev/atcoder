from collections import deque

# input
N, M = map(int, input().split())

edge = [set() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u].add(v)

count = 0

for s in range(1, N+1):
    is_visited = [False for _ in range(N+1)]

    search_deq = deque()
    
    search_deq.append(s)
    is_visited[s] = True
    
    while len(search_deq) != 0: #BFS
        i = search_deq.popleft()
        for j in edge[i]:
            if is_visited[j] == False:
                is_visited[j] = True
                count += 1
                search_deq.append(j)

print(count - M)
