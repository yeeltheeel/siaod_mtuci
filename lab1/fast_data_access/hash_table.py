class HashTable():
	def __init__(self):
		self.bucket_num = 0
		self.empty_array_list = []
		self.elem_counter = 0

	def set(self, key, value):
		pass

	def get(self, key):
		pass

	def remove(key):
		pass

	def load_factor(self):
		if self.bucket_num > 0:
			return self.elem_counter / self.bucket_num
		return 0

	def collision_count(self):
		pass
