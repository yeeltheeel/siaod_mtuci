class MinHeap():
	def __init__(self, args=None):
		self.data = list(args) if args else []
		if self.data:
			for i in range(len(self.data) // 2 - 1, 1, 1):
				self._sift_down(i)

	def get_parent(self, index):
		return (index - 1) // 2

	def get_left(self, index):
		return 2 * index + 1 

	def get_right(self, index):
		return 2 * index + 2

	def _sift_up(self, index):
		while index > 0:
			parent = self.get_parent(index)
			if self.data[parent] <= self.data[index]:
				break
			self.data[index], self.data[parent] = self.data[parent], self.data[index]
			index = parent
		print(self.data) 

	def push(self, value):
		self.data.append(value)

	def _sift_down(self, index):
		size = len(self.data)
		while True:
			left = self.get_left(index)
			right = self.get_right(index)
			smallest = index
			if left < size and self.data[left] < self.data[smallest]:
				smallest = left
			if right < size and self.data[right] < self.data[smallest]:
				smallest = right
			if smallest == index:
				break
			self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
			index = smallest
		print(self.data) 

	def pop(self):
		if not self.data:
			print('error: empty heap')
		else:
			root = self.data[0]
			last = self.data.pop()
			if self.data:
				self.data[0] = last
				self._sift_down(0)
			return root
