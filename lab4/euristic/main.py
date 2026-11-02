V = { 'A', 'B', 'C', 'D', 'E', 'F', 'G' }
edges = [
	(0, 1, 4),
	(0, 2, 3),
	(1, 2, 1),
	(1, 3, 2),
	(2, 3, 4),
	(2, 4, 2),
	(3, 4, 3),
	(3, 5, 2),
	(4, 5, 3),
	(4, 6, 6),
	(5, 6, 1)
]

N = 12
# S - start, G - target, . - empty, # - obstacle
field = [
	'S..#........',
	'.#.#.######.',
	'.#...#......',
	'.###.#.####.',
	'.....#....#.',
	'.#####.##.#.',
	'.......##...',
	'.#####....#.',
	'.#...####.#.',
	'.#.#......#.',
	'...#.####...',
	'####......G.'
]
S = (0, 0)
G = (11, 10)

names = sorted(V)

# 1
class DSU:
	def __init__(self, vertex_cnt):
		self.parent = list(range(vertex_cnt))
		self.size = [1] * vertex_cnt

	def find(self, v):
		if self.parent[v] != v:
			self.parent[v] = self.find(self.parent[v])
		return self.parent[v]

	def union(self, a, b):
		a = self.find(a)
		b = self.find(b)
		if a == b:
			return False
		if self.size[a] < self.size[b]:
			a, b = b, a
		self.parent[b] = a
		self.size[a] += self.size[b]
		return True

def kruskal(edges, vertex_cnt):
	dsu = DSU(vertex_cnt)
	mst = []
	total = 0
	for u, v, w in sorted(edges, key=lambda e: e[2]):
		if dsu.union(u, v):
			mst.append((u, v, w))
			total += w
			if len(mst) == vertex_cnt - 1:
				break
	return mst, total

edge_list = [(w, u, v) for (u, v, w) in edges]
mst, total = kruskal(edge_list, len(V))
for w, u, v in mst:
	print(f'{names[u]} - {names[v]} : {w}')
print('total_weight={}'.format(total))

# 2
from collections import deque

def get_neighbours(a):
	row, col = a
	res = []
	# down, up, right, left
	for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		new_row = row + delta_row
		new_col = col + delta_col
		if 0 <= new_row < N and 0 <= new_col < N and field[new_row][new_col] != '#':
			res.append((new_row, new_col))
	return res

def reconstruct_path(parent, goal):
	path = []
	node = goal
	while node is not None:
		path.append(node)
		node = parent[node]
	path.reverse()
	return path

def bfs(S, G, cell_cost=None):
	queue = deque([S])
	parent = {S: None}
	dist = {S: 0}
	processed = 0
	while queue:
		cur = queue.popleft()
		processed += 1
		if cur == G:
			break
		for neighbour in get_neighbours(cur):
			if neighbour  not in parent:
				parent[neighbour] = cur
				if cell_cost is None:
					cur_cost = 1
				else:
					cur_cost = cell_cost(neighbour)
				dist[neighbour] = dist[cur] + cur_cost
				queue.append(neighbour)

	if G not in parent:
		return None, None, processed
	return reconstruct_path(parent, G), dist[G], processed

def render(path):
	grid = [list(row) for row in field]
	for (row, col) in path:
		if grid[row][col] == '.':
			grid[row][col] = '*'
	return '\n'.join(''.join(row) for row in grid)

path, steps, processed = bfs(S, G)
print('steps={}, processed={}'.format(steps, processed))
print(render(path))

# 3
# Manhattan_h = abs(r - goal_r) + abs(c - goal_c)
# Euclidean_h = sqrt((r - goal_r)**2 + (c - goal_c)**2)
from math import hypot

def manhattan(a, b):
	h = abs(a[0] - b[0]) + abs(a[1] - b[1])
	return h

def euclidean(a, b):
	h = hypot(a[0] - b[0], a[1] - b[1])
	return h

g = [ (0, 0), (6, 0), (6, 6), (7, 9), (11, 9) ]
for p in g:
	print('p={}: manhattan={} euclidean={}'.format(
		p,
		manhattan(p, G), 
		round(euclidean(p, G), 3)
	))

# 4
import heapq as hp

def greedy(S, G, h=manhattan):
	open_heap = [(h(S, G), 0, S)]
	counter = 1
	parent = {S: None}
	opened = {S}   # OPEN
	closed = set() # CLOSED
	processed = 0
	while open_heap:
		_, _, cur = hp.heappop(open_heap)
		if cur in closed:
			continue
		opened.discard(cur)
		closed.add(cur)
		processed += 1
		if cur == G:
			break
		for neighbour in get_neighbours(cur):
			if neighbour in closed:
				continue
			if neighbour not in parent:
				parent[neighbour] = cur
				hp.heappush(open_heap, (
						h(neighbour, G), 
						counter, neighbour
					))
				counter += 1
				opened.add(neighbour)

	if G not in parent:
		return None, None, processed
	path = reconstruct_path(parent, G)

	return path, len(path) - 1, processed

path, steps, processed = greedy(S, G, manhattan)
print('steps={} processed={}'.format(steps, processed))
print(render(path))

# 5
def aast(S, G, h=manhattan, cell_cost=None):
	g = {S: 0}
	f = {S: h(S, G)}
	parent = {S: None}
	open_heap = [(f[S], 0, S)]
	counter = 1
	closed = set()
	processed = 0

	while open_heap:
		_, _, cur = hp.heappop(open_heap)
		if cur in closed:
			continue
		closed.add(cur)
		processed += 1
		if cur == G:
			break
		for neighbour in get_neighbours(cur):
			if neighbour in closed:
				continue
			if cell_cost is None:
				cur_cost = 1
			else:
				cur_cost = cell_cost(neighbour)
			tent_dist = g[cur] + cur_cost
			if neighbour not in g or tent_dist < g[neighbour]:
				g[neighbour] = tent_dist
				f[neighbour] = tent_dist + h(neighbour, G)
				parent[neighbour] = cur
				hp.heappush(open_heap, (
					f[neighbour], 
					counter, 
					neighbour
				))
				counter += 1

	if G not in g:
		return None, None, processed
	return reconstruct_path(parent, G), g[G], processed

path, cost, processed = aast(S, G, manhattan)
print('manhatten: cost={} processed={}'.format(cost, processed))
print(render(path))
path, cost, processed = aast(S, G, euclidean)
print('euclidean: cost={} processed={}'.format(cost, processed))

# 6
def dijkstra(S, G, cell_cost=None):
	dist = {S: 0}
	parent = {S: None}
	heap = [(0, 0, S)]
	counter = 1
	closed = set()
	processed = 0

	while heap:
		cur_dist, _, cur = hp.heappop(heap)
		if cur in closed:
			continue
		closed.add(cur)
		processed += 1
		if cur == G:
			break
		for neighbour in get_neighbours(cur):
			if neighbour in closed:
				continue
			if cell_cost is None:
				cur_cost = 1
			else:
				cur_cost = cell_cost(neighbour)
			new_dist = cur_dist + cur_cost
			if neighbour not in dist or new_dist < dist[neighbour]:
				dist[neighbour] = new_dist
				parent[neighbour] = cur
				hp.heappush(heap, (
					new_dist, 
					counter, 
					neighbour
				))
				counter += 1

	return reconstruct_path(parent, G), dist.get(G), processed

P = 1
PE = 5
high_cost = [ (6, 2), (6, 3), (6, 4), (6, 5), (6, 6) ]

def cell_cost(cell):
	if cell in high_cost:
		return PE
	else:
		return P

path_bfs, _, proc_bfs = bfs(S, G)
cost_bfs = sum(cell_cost(c) for c in path_bfs[1:])
print('bfs: cost={} for len={}, processed={} '.format(
	cost_bfs,
	len(path_bfs) - 1,
	proc_bfs
))

path_d, cost_d, proc_d = dijkstra(S, G, cell_cost)
print('dijkstra: cost={} for len={}, processed={} '.format(
	cost_d,
	len(path_d) - 1,
	proc_d
))

path_g, cost_g, proc_g = greedy(S, G, manhattan)
print('greedy: cost={} for len={}, processed={} '.format(
	cost_g,
	len(path_g) - 1,
	proc_g
))

path_a, cost_a, proc_a = aast(S, G, manhattan, cell_cost)
print('a*_m: cost={} for len={}, processed={} '.format(
	cost_a,
	len(path_a) - 1,
	proc_a
))

path_a, cost_a, proc_a = aast(S, G, euclidean, cell_cost)
print('a*_e: cost={} for len={}, processed={} '.format(
	cost_a,
	len(path_a) - 1,
	proc_a
))
 