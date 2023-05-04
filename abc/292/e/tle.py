class SimpleGraph:
    def __init__(self, n):
        self.n = n
        self.edg = [[False for _ in range(n)] for _ in range(n)] 
        self.count = 0

    def unite(self, x, y):
        self.edg[x][y] = True
        return True

    def check(self, x):
        updated = False
        for i in range(self.n):
            if self.edg[x][i]:
                for j in range(self.n):
                    if x == j:
                        continue
                    if self.edg[i][j] and (not self.edg[x][j]):
                        self.unite(x, j)
                        self.count += 1
                        updated = True
        return updated

N, M = map(int, input().split())
sides = [tuple(map(int, input().split())) for x in range(M)]

# init
sg = SimpleGraph(N)
for u, v in sides:
    sg.unite(u-1, v-1)

# print(f"before edg:{st.edg}")
# process
while True:
    flg = False
    for i in range(N):
        flg = (sg.check(i) or flg)

    if not flg:
        break

print(sg.count)

# print(f"after edg:{st.edg}")
