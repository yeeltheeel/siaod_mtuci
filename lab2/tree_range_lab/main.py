# 1
class Node:
	def __init__(self, val, il=None, ir=None):
		self.key = val
		self.left = il
		self.right = ir

	def __str__(self):
		return f"{self.key}"

	def __repr__(self):
		return self.__str__()

bin_tree = Node(
	8,
	Node(4, Node(2), Node(6)),
	Node(12, Node(10), Node(14))
)

print('root={}, right_child={}, leaf={}'.format(
		bin_tree, 
		bin_tree.right, 
		bin_tree.right.right
	))
print()

# 2
def insert(root, key):
	if root is None:
		return Node(key)
	if key < root.key:
		root.left = insert(root.left, key)
	elif key > root.key:
		root.right = insert(root.right, key)
	return root

new_bin_tree = None
for val in [8, 4, 12, 2, 6, 10, 14]:
	new_bin_tree = insert(new_bin_tree, val)
print('root={}, right_child={}, leaf={}'.format(
		new_bin_tree, 
		new_bin_tree.left, 
		new_bin_tree.left.right
	))
print()

# 3
def search(root, key):
	visited = 0
	current = root
	while current is not None:
		visited += 1
		if key == current.key:
			return current, visited
		if key < current.key:
			current = current.left 
		else:
			current = current.right
	return None, visited

print('near root: {}\nouter level: {}\nnot existing: {}'.format(
	search(new_bin_tree, 8),
	search(new_bin_tree, 14),
	search(new_bin_tree, 100)
))
print()

# 4
def preorder(root):
	if root is not None:
		return [root.key] + preorder(root.left) + preorder(root.right)
	return []

def inorder(root):
	if root is not None:
		return inorder(root.left) + [root.key] + inorder(root.right)
	return []

def postorder(root):
	if root is not None:
		return postorder(root.left) + postorder(root.right) + [root.key]
	return []

print('preorder: {}\ninorder: {}\npostorder: {}'.format(
	preorder(new_bin_tree),
	inorder(new_bin_tree),
	postorder(new_bin_tree)
))
print()

# 5
def delete(root, key):
	if root is None:
		return None
	if key < root.key:
		root.left = delete(root.left, key)
	elif key > root.key:
		root.right = delete(root.right, key)
	else:
		if root.left is None:
			return root.right
		if root.right is None:
			return root.left
		min_node = root.right
		while min_node.left is not None:
			min_node = min_node.left
		root.key = min_node.key
		root.right = delete(root.right, min_node.key)
	return root

new_bin_tree_rem = delete(new_bin_tree, 14)
print('removed leaf:', inorder(new_bin_tree_rem))
new_bin_tree_rem = delete(new_bin_tree_rem, 12)
print('removed element with single child:', preorder(new_bin_tree_rem))
new_bin_tree_rem = delete(new_bin_tree_rem, 4)
print('removed element with two children:', preorder(new_bin_tree_rem))
print()

# 6
vals = [
	[8, 4, 12, 2, 6, 10, 14],
	[2, 4, 6, 8, 10, 12, 14]
]

def height(root):
	if root is not None:
		return 1 + max(height(root.left), height(root.right))
	return -1

for val in vals:
	bin_tree = None
	for v in val:
		bin_tree = insert(bin_tree, v)
	print('height of {} is {}'.format(
		preorder(bin_tree),
		height(bin_tree)
	))
print()

# 7
def node_height(node):
	if node is not None:
		return 1 + max(node_height(node.left), node_height(node.right))
	return -1

def balance_factor(node):
	if node is not None:
		return node_height(node.left) - node_height(node.right)
	return 0

def rotate_right(root):
	new_root = root.left
	root.left = new_root.right
	new_root.right = root
	return new_root

def rotate_left(root):
	new_root = root.right
	root.right = new_root.left
	new_root.left = root
	return new_root

def balance(node, key):
	if node is None:
		return Node(key)
	if key < node.key:
		node.left = balance(node.left, key)
	elif key > node.key:
		node.right = balance(node.right, key)
	else:
		return node

	bf = balance_factor(node)
	# LL
	if bf > 1 and key < node.left.key:
		return rotate_right(node) 
	# RR                    
	if bf < -1 and key > node.right.key:
		return rotate_left(node)          
	# LR
	if bf > 1 and key > node.left.key:                
		node.left = rotate_left(node.left)
		return rotate_right(node)
	# RL
	if bf < -1 and key < node.right.key:              
		node.right = rotate_right(node.right)
		return rotate_left(node)
	return node

vals = [
	[30, 20, 10 ], 
	[10, 20, 30]
]

for val in vals:
	bin_tree = None
	for v in val:
		bin_tree = balance(bin_tree, v)
	print('balanced {} is {}'.format(
		val,
		preorder(bin_tree)
	))
print()

vals = [
	[30, 10, 20], 
	[10, 30, 20]
]

for val in vals:
	bin_tree = None
	for v in val:
		bin_tree = balance(bin_tree, v)
	print('double rotation of {} is {}'.format(
		val,
		preorder(bin_tree)
	))
print()

# 8
from random import randint 
from time import perf_counter

BIG_NUM = int(1e5)
vals = [randint(1, 100) for i in range(BIG_NUM)]

def range_sum_naive(data, left, right):
	s = 0
	for i in range(left, right + 1):
		s += data[i]
	return s

K = 1000
ranges = []
for k in range(K):
	l = randint(0, BIG_NUM - 1)
	ranges.append(
		[l, randint(l, BIG_NUM - 1)]
	)

st = perf_counter()
for r in ranges:
	s = range_sum_naive(vals, r[0], r[1])
fn = perf_counter()
print('range_sum_naive elapsed={:.4f}s'.format(
	fn - st
))
print()

# 9
def build_prefix(data):
	prefix = [0] * (len(data) + 1)
	for i, val in enumerate(data):
		prefix[i + 1] = prefix[i] + val
	return prefix

def range_sum_prefix(prefix, left, right):
	return prefix[right + 1] - prefix[left]

st = perf_counter()
prefix = build_prefix(vals)
fn = perf_counter()
print('build_prefix elapsed={:.4f}s'.format(
	fn - st
))

st = perf_counter()
for r in ranges:
	s = range_sum_prefix(prefix, r[0], r[1])
fn = perf_counter()
print('range_sum_prefix elapsed={:.4f}s'.format(
	fn - st,
))
print()

# 10
class FenwickTree:
	def __init__(self, data=None):
		if data:
			self.n = len(data)
		else:
			self.n = 0
		self.tree = [0] * (self.n + 1)
		if data:
			for i, val in enumerate(data):
				self.update(i, val)
	
	def update(self, index, delta):
		i = index + 1 
		while i <= self.n:
			self.tree[i] += delta
			i += i & -i
	
	def prefix_sum(self, index):
		i = index + 1
		s = 0
		while i > 0:
			s += self.tree[i]
			i -= i & -i 
		return s

	def range_sum(self, left, right):
		if left == 0:
			return self.prefix_sum(right)
		return self.prefix_sum(right) - self.prefix_sum(left - 1)

fen_tree = FenwickTree(vals)
for l, r in ranges[:5]:
    print('fenwick range_sum={}s, sum={}s for range[{}, {}]'.format(
		fen_tree.range_sum(l, r), 
		sum(vals[l:r+1]),
		l, r
	)) 
print()

# 11
class SegmentTree:
	def __init__(self, data):
		n = len(data)
		self.n = n
		self.data = data
		self.tree = [0] * (2 * self.n)
		for i in range(n):
			self.tree[n + i] = data[i]
		for i in range(n - 1, 0, -1):
			self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

	def query(self, left, right):
		res = 0
		l = left + self.n
		r = right + self.n
		while l <= r:
			if l & 1:
				res += self.tree[l]
				l += 1
			if not (r & 1):
				res += self.tree[r]
				r -= 1
			l //= 2
			r //= 2
		return res

	def update(self, index, value):
		self.data[index] = value
		i = index + self.n
		self.tree[i] = value
		i //= 2
		while i >= 1:
			self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
			i //= 2

seg_tree = SegmentTree(vals)
for l, r in ranges[:5]:
    print('seg_tree={} for range[{}, {}]'.format(
		seg_tree.query(l, r),
		l, r
	)) 
print()

# 12
class SegmentTreeMMS(SegmentTree):
	NEUTRAL = (0, float('inf'), float('-inf'))

	def __init__(self, data):
		super().__init__(data)
		n = self.n
		for i in range(n):
			val = data[i]
			self.tree[n + i] = (val, val, val)
		for i in range(n - 1, 0, -1):
			a = self.tree[2 * i]
			b = self.tree[2 * i + 1]
			self.tree[i] = (
				a[0] + b[0], 
				min(a[1], b[1]), 
				max(a[2], b[2])
			)

	def query(self, left, right):
		res_l = self.NEUTRAL
		res_r = self.NEUTRAL
		l = left + self.n
		r = right + self.n
		while l <= r:
			if l & 1:
				a = res_l
				b = self.tree[l]
				res_l = (
					a[0] + b[0], 
					min(a[1], b[1]), 
					max(a[2], b[2])
				)
				l += 1
			if not (r & 1):
				a = self.tree[r]
				b = res_r
				res_r = (
					a[0] + b[0], 
					min(a[1], b[1]), 
					max(a[2], b[2])
				)
				r -= 1
			l //= 2
			r //= 2
			a = res_l
			b = res_r
		return (
			a[0] + b[0], 
			min(a[1], b[1]), 
			max(a[2], b[2])
		)

	def update(self, index, value):
		self.data[index] = value
		i = index + self.n
		self.tree[i] = (value, value, value)
		i //= 2
		while i >= 1:
			a = self.tree[2 * i]
			b = self.tree[2 * i + 1]
			self.tree[i] = (
				a[0] + b[0], 
				min(a[1], b[1]), 
				max(a[2], b[2])
			)
			i //= 2

seg_tree_mms = SegmentTreeMMS(vals)
for l, r in ranges[:5]:
    print('seg_tree_mms={} for range[{}, {}]'.format(
		seg_tree_mms.query(l, r),
		l, r
	)) 
print()

# 13
K = 1000
sensor_ids = list(set([randint(1, 100) for i in range(20)]))
sensor_tree = None
sensors = dict()
for sid in sensor_ids:
	data = [randint(0, 100) for i in range(K)]
	sensors[sid] = {
		'sid': sid,
		'data': data,
		'fen_tree': FenwickTree(data),
		'seg_tree': SegmentTreeMMS(data)
	}
	sensor_tree = insert(sensor_tree, sid)
print('sid_tree={}'.format(inorder(sensor_tree)))
sid = sensor_ids[5]
l = 100
r = 300
print('for sid={} range_sum_naive={}, range_sum={}'.format(
	sid,
	range_sum_naive(sensor_tree[sid].data, l, r),
	sensor_tree[sid].fen_tree(l, r),
))