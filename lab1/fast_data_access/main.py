import timeit as tmt
# from time import perf_counter
from random import randint
import heapq as hp
from hash_table import HashTable
from binary_heap import MinHeap

big_num = int(1e5) # >=1e5
a = int(1e2)

def get_time(func, n=big_num):
	timer = tmt.Timer()
	total = tmt.timer.timeit(number=n)
	return total

# 2
def task2():
	def linear_search(numbers, target):
		for i in range(len(numbers)):
			if numbers[i] == target:
				return i
		return -1

	array_int = [randint(-a, a) for i in range(big_num)]

# 3
def task3():
	def id_search(values, target):
		for val in values:
			if val[0] == target:
				return target
		return -1

	array_dict = [(i, randint(-a, a)) for i in range(big_num)]
	st = 0
	md = big_num // 2
	fn = big_num - 1
	id_search(array_dict, st)
	id_search(array_dict, md)
	id_search(array_dict, fn)

	new_dict = dict(array_dict)

# 4
def task4():
	print('hash({}) = {}, hash({}) = {}, hash({}) = {}\nhash({}) = {}, hash({}) = {}'.format(
		0, hash(0), 
		5, hash(5), 
		-5, hash(-5), 
		'aaaaaa', hash('aaaaaa'),
		'uwu', hash('uwu')
		))

	def bucket_index(key, table_size):
		return hash(key) % table_size

# 5
def task5():
	pass

# 6
def task6():
	pass

# 7
def task7():
	array = [2, 5, 7, 9, 11, 10, 15] 
	heap = MinHeap(array)

# 8
def task8():
	pass

# 9
def task9():
	pass

# 10
def task10():
	heap = []
	hp.heapify(heap)

# 11
def task11():
	array_int = [randint(-a, a) for i in range(big_num)]
	for K in [10, 100, 1000]:
		pass

# 12
def task12():
	def top_k_heap(data):
		pass

# 13
def task13():
	contestants = []

if __name__ == "__main__":
	task2()
	task3()
	task4()
	task5()
	task6()
	task7()
	task8()
	task9()
	task10()
	task11()
	task12()
	task13()

