V = {0, 1, 2, 3, 4, 5, 6, 7}

edges = [
	(0, 1, 4),
	(0, 2, 8),
	(1, 2, 1),
	(2, 0, 3),
	(2, 3, 2),
	(3, 4, 2),
	(4, 5, 3),
	(5, 3, 1),
	(5, 6, 4),
	(6, 7, 2),
]

def build_directed(edges):
	G = {v: [] for v in V}
	for u, v, w in edges:
		G[u].append((v, w))
	return G

def build_undirected(edges):
	Gu = {v: [] for v in V}
	seen = set()
	for u, v, w in edges:
		e = (min(u, v), max(u, v))
		if e in seen:
			continue
		seen.add(e)
		Gu[u].append(v)
		Gu[v].append(u)
	return Gu

def print_graph(G, V=V, comment=""):
	V = list(V)
	if len(comment) > 0:
		print(comment, ":", sep="")
	for v in G:
		print(v, ": ", end="")
		if not G[v]:
			print("None", end="")
		else:
			for u in G[v]:
				if type(u) == tuple:
					print("({}, {})".format(
						u[0], u[1], #V[u[0]], V[u[1]]
					), end=" ")
				else:
					print(V[u], end=" ")
		print()
	print()

# 1
def dfs(Gu, start=0, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	order = [start]
	for u in Gu[start]:
		if u not in visited:
			order += dfs(Gu, u, visited)
	return order

def components(Gu):
	visited = set()
	comps = []
	for v in sorted(V):
		if v not in visited:
			tmp = dfs(Gu, v, visited)
			comps.append(sorted(tmp))
	return comps

G = build_directed(edges)
Gu = build_undirected(edges)
print_graph(G, comment="original G")
print_graph(Gu, comment="original Gu")

print("dfs(Gu) from 0={}\ncomponents(Gu)={}".format(
	dfs(Gu),
	components(Gu)
))
Gu_copy = {v: [u for u in Gu[v] if {v, u} != {5, 6}] for v in V}
print("components(Gu) without (5, 6)={}".format(
	components(Gu_copy)
))

# 2
def kosaraju(G):
	def dfs1(v):
		visited.add(v)
		for u, i in G[v]:
			if u not in visited:
				dfs1(u)
		order.append(v)
			
	def dfs2(v, comps, Gt):
		visited.add(v)
		comps.append(v)
		for u in Gt[v]:
			if u not in visited:
				dfs2(u, comps, Gt)

	visited = set()
	order = []
	for v in sorted(V):
		if v not in visited:
			dfs1(v)
	
	Gt = {v: [] for v in G}
	for u in G:
		for e, i in G[v]:
			Gt[e].append(u)

	visited = set()
	sccs = []
	for v in reversed(order):
		if v not in visited:
			comp = []
			dfs2(v, comp, Gt)
			sccs.append(sorted(comp))
	return sccs

print("kosaraju(G)={}".format(
	kosaraju(G) # res = {0, 1, 2}, {3, 4, 5}, {6}, {7}
))

# 3
timer = 0
tin, low = {}, {}
bridges, points = set(), set()

def dfs_bridges(v, parent, Gu):
	global timer
	tin[v] = low[v] = timer
	timer += 1
	child_count = 0
	for u in Gu:
		if u == parent:
			continue
		if u in tin:
			low[v] = min(low[v], low[u])
		else:
			child_count += 1
			dfs_bridges(u, v, Gu)
			low[u] = min(low[v], low[u])
			if low[u] > tin[v]:
				bridges.add(
					(min(v, u), max(v, u))
				)
			if parent is not None and low[u] >= tin[v]:
				points.add(v)
	if parent is None and child_count > 1:
		points.add(v)

for v in sorted(V):
	if v not in tin:
		dfs_bridges(v, None, Gu)
bridges = sorted(bridges)
points = sorted(points)

print("bridges(G)={}, points(G)={}".format(
	bridges, # bridges = {2, 3}, {5, 6}, {6, 7}
	points
))
for v in sorted(V):
    print("{}: tin={}, low={}".format(
		v, tin[v], low[v]
	))

Gu_no_bridge = {v: [u for u in Gu[v] if (min(v, u), max(v, u)) != (5, 6)] for v in V}
print("components(Gu) without bridge={}".format(
	components(Gu_no_bridge)
))

# 4
def topology_sort():
	pass

# res = {0, 1, 2} → {3, 4, 5} → {6} → {7}

# 5
import heapq as hp
INF = 1e5

def dijkstra_heap(G, start=0):
	dist = {v: INF for v in V}
	parent = {v: None for v in V}
	dist[start] = 0
	heap = [(0, start)] # hp.heap()
	return dist, parent

dist, parent = dijkstra_heap(G)
print("dist={}".format(
	dist # res = [0, 4, 5, 7, 9, 12, 16, 18]
))

path, current = [], 7
while current is not None:
    path.append(current)
    current = parent[current]
path.reverse()
print("minpath={} : {}".format(
	sum(path), # res = 18
	path       # res = 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7
))

# 6
def bellman_ford(G):
	pass

# 7
def floyd_warshall(G):
	pass

