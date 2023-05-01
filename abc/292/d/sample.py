class UnionFind():
	def __init__(self, n):
		self.n = n
		self.parent = [-1] * (n + 1)
		self.rank = [0] * (n + 1)
		self.siz = [1] * (n + 1)
		self.edg = [0] * (n + 1)
	
	def root(self, x):
		if self.parent[x] == -1:
			return x
		else:
			self.parent[x] = self.root(self.parent[x])
			return self.parent[x]
	
	def unite(self, x, y):
		rx = self.root(x)
		ry = self.root(y)
 
		if rx == ry:
			self.edg[rx] += 1
			return False
		
		if self.rank[rx] < self.rank[ry]:
			rx, ry = ry, rx
		self.parent[ry] = rx
 
		if self.rank[rx] == self.rank[ry]:
			self.rank[rx] += 1
		
		self.siz[rx] += self.siz[ry]
		self.edg[rx] += self.edg[ry] + 1
 
		return True
	
	def size(self, x):
		return self.siz[self.root(x)]
	
	def edge(self, x):
		return self.edg[self.root(x)]
 
N, M = map(int, input().split())
arrUV = [list(map(int, input().split())) for i in range(M)]
 
uf = UnionFind(N)
for u, v in arrUV:
	uf.unite(u, v)
 
for i in range(1, N + 1):
	if uf.size(i) != uf.edge(i):
		print("No")
		exit()
 
print("Yes")
