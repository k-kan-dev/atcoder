from collections import deque

class Dijkstra:
    def __init__(self, n):
        self.n = n
        self.graph = [[False for _ in range(n)] for _ in range(n)] 
        self.count = 0

    def unite(self, x, y, w = 1):
        self.graph[x][y] = w
        self.graph[y][x] = w

    def calc(self, x):
        # init
        dist_to_v = [float('inf')] * self.n
        sv = x
        dist_to_v[sv] = 0 # start point
        v_done = set([sv])
        v_undifined = set(range(self.n)) - v_done

        while True:
            for ev, w in enumerate(self.graph[sv]):
                if w and (ev in v_undifined):
                    # update
                    if dist_to_v[sv] + w < dist_to_v[ev]:
                        dist_to_v[ev] = dist_to_v[sv] + w

                    else:
                        pass

            ### for next iterate
            # 未確定の中から距離が最も小さい地点を選んで、その距離をその地点の最小距離として確定します。
            if len(v_undifined) == 0:
                break

            min_w, min_v = min([(dist_to_v[idx], idx) for idx in v_undifined]) # next_v start from min_v among connecting_v
            sv = min_v
            v_done.add(sv)
            v_undifined = v_undifined - v_done
        return dist_to_v


N, M = map(int, input().split())
sides = [tuple(map(int, input().split())) for x in range(M)]

# init
dk = Dijkstra(N)
for u, v, w in sides:
    dk.unite(u-1, v-1, w)

print(dk.graph)
ans = dk.calc(1-1)
print(ans)