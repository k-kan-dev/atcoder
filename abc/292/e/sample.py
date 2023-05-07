from collections import deque
 
N,M = map(int, input().split())
 
edge = [set() for _ in range(N+1)]
 
for i in range(M):
    u,v = map(int, input().split())
    edge[u].add(v)
 
con_cnt = 0     # 頂点間に通っているエッジの本数
 
for s in range(1,N+1):
    is_visited = [False for i in range(N+1)]    # 頂点iに訪問済みか
 
    search_deq = deque()                        # 探索候補一覧
 
    # 開始点の処理
    search_deq.append(s)
    is_visited[s] = True
 
    # 幅優先探索
    while len(search_deq)!=0:
        i = search_deq.popleft()
 
        for j in edge[i]:
            if is_visited[j] == False:
                is_visited[j] = True
                con_cnt += 1 
                search_deq.append(j)
 
print(con_cnt - M)
