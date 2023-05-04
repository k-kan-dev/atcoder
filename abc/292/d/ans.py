class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * (n+1)
        self.rank = [0] * (n+1)
        self.edge = [0] * (n+1)
        self.size = [1] * (n+1)

    def root(self, x):
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        # already connected
        if rx == ry:
            self.edge[rx] += 1
            return False

        # uniting by setting same parent
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.edge[rx] += self.edge[ry] + 1
        self.size[rx] += self.size[ry]

        return True

    def issame(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False

    def tree_size(self, x):
        return self.size[self.root(x)]

    def edges(self, x):
        return self.edge[self.root(x)]

N, M = map(int, input().split())
sides = []
for _ in range(M):
    sides.append(tuple(map(int, input().split())))
    
uf = UnionFind(N)
for side in sides:
    uf.unite(side[0], side[1])

for i in range(1, N+1):
    if uf.tree_size(i) != uf.edges(i):
        print("No")
        exit()

print("Yes")
