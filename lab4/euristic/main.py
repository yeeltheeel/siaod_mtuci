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

# 1
class DSU:
	def __init__(self):
		self.parent = []
		self.size = []

	def find(v):
		if self.parent[v] != v:
			self.parent[v] = find(self.parent[v])
		return self.parent[v]

	def union(a, b):
		a = find(a)
		b = find(b)
		if a == b:
			return False
		return True

def crascal(a, b):
	pass

# 2
def get_neigbours(a):
	pass

def bfs(S, G):
	pass

# 3
# Manhattan_h = abs(r - goal_r) + abs(c - goal_c)
# Euclidean_h = sqrt((r - goal_r)**2 + (c - goal_c)**2)

def manhattan(a, b):
	h = 0
	return h

def euclidean(a, b):
	h = 0
	return h


g = [ (0, 0), (6, 0), (6, 6), (7, 9), (11, 9) ]

# 4
import heapq as hp

OPEN = []
CLOSED = []

# 5

# 6
P = 1
PE = 5
extr = [ (6, 2), (6, 3), (6, 4), (6, 5), (6, 6) ]
 