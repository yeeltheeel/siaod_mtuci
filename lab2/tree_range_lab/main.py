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
	Node(8),
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
	pass

vals = [
	[30, 20, 10 ], 
	[10, 20, 30]
]

for val in vals:
	print('height of {} is {}'.format(
		preorder(bin_tree),
		height(bin_tree)
	))

vals = [
	[30, 10, 20], 
	[10, 30, 20]
]

# 8
from random import randint 

BIG_NUM = int(1e5)
vals = [randint(1, 100) for i in range(BIG_NUM)]

def range_sum_naive(data, left, right):
	pass

# 9
def build_prefix(data):
	pass

def range_sum_prefix(prefix, left, right):
	pass

# 10
class FenwickTree:
	def __init__(self):
		pass
	
	def update(self, index, delta):
		pass 
	
	def prefix_sum(self, index):
		pass

	def range_sum(self, left, right):
		pass

# 11
class SegmentTree:
	def __init__(self):
		pass

	def query(self, left, right):
		pass

	def update(self, index, value):
		pass

# 12

# 13
