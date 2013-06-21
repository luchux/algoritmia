#Binary Tree with left child, right child.
class BinaryTree():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __unicode__(self):
		return self.data

#Depth first search.
def dfs_basic(tree):
	nodes = []

	if tree is not None:
		nodes.append(tree.data)
		nodes.extend(dfs_basic(tree.left))
		nodes.extend(dfs_basic(tree.right))

	return nodes

#Depth first search efficient to retrieve nodes data yielded.
def dfs_yield(tree):
	if tree is not None:
		yield tree.data

		for node_data in dfs_yield(tree.left):
			yield node_data

		for node_data in dfs_yield(tree.right):
			yield node_data

#Birth first search.
def bfs_basic(tree):
	nodes = []

	if tree is not None:

		if tree.left is not None:
			nodes.append(tree.left.data)

		if tree.right is not None:
			nodes.append(tree.right.data)

		nodes.extend(bfs_basic(tree.left))
		nodes.extend(bfs_basic(tree.right))

	return nodes

#array = [16,14,10,8,7,9,3,2,4,1]

# Tree: Trie
class Trie():

	def __init__(self):
		self.trie = None

	def make_trie(self, words):
		root = dict()
		for word in words:
			current_dict = root
			for letter in word:
				current_dict = current_dict.setdefault(letter, {})
			current_dict = current_dict.setdefault('_end', '_end')
		self.trie = root

	def in_trie(self, word):
		current_dict = self.trie
		for letter in word:
			if letter in current_dict:
				current_dict = current_dict[letter]
			else:
				return False
		else:
			if '_end' in current_dict:
				return True
			else:
				return False

	def in_trie_partial(current_dict,actual_word):
		pass

	def printme(self):
		print self.trie

def test_trie():
	words = ['hola', 'chau', 'hoja']
	t = Trie()
	t.make_trie(words)
	print t.printme()


#Heap datastructure.
class Heap():
	def __init__(self, array):
		self.array = array

	def length(self):
		return len(self.array)

	def remove_first(self):
		self.array = self.array[1:]

	#get(i): return value of array[i]
	def get(self, i):
		return self.array[i]

	def swap(self, i, j):
		self.array[i], self.array[j] = self.array[j], self.array[i]

	#return index left child of i-th
	def left(self, i):
		try:
			assert i <= self.length()
		except:
			print 'i not in array'

		try:
			assert (2*i + 1) <= self.length()
		except:
			return -1
		return (2*i + 1)

	#return index right child of i-th
	def right(self,i):
		try:
			assert i < self.length()
		except:
			print 'i not in array'

		try:
			assert (2*i + 2) < self.length()
		except:
			return -1
		return (2*i + 2)

	def parent(self, i):
		try:
			assert i <= self.length()
		except:
			print 'i not in array'
		return (i-1)/2

	#max_heapify(i): assumes left(i) and right(i) max_heapify,
	#and assert max_heaipfy for i
	def max_heapify(self,i):
		ileft = self.left(i)
		iright = self.right(i)
		largest = i

		if ileft < self.length() and self.get(ileft) > self.get(largest):
			largest = ileft

		if iright < self.length() and self.get(iright) > self.get(largest):
			largest = iright

		if largest != i:
			self.swap(i, largest)
			self.max_heapify(largest)

	def build_max_heap(self):
		for i in range((self.length()/2)-1, -1, -1):
			self.max_heapify(i)

	#heap_sort(): sort the array using max_heapify property
	#TODO: sort in line, now is using extra datastructure, destroying heap, restoring heap sorted.
	def heap_sort(self):

		self.build_max_heap()
		sorted_array = []

		for i in range((self.length()-1), 0, -1):
			sorted_array.append(self.get(0))
			self.remove_first()
			self.max_heapify(0)

		sorted_array.extend(self.array)
		self.array = sorted_array

		return self.array

def play_with_trees():
	tree = BinaryTree(1, BinaryTree(2, BinaryTree(3), BinaryTree(4)), BinaryTree(5, BinaryTree(6), BinaryTree(7)))

	print dfs_basic(tree)
	print bfs_basic(tree)

	for node in dfs_yield(tree):
		print node

def play_with_heaps():
	array = [14,16,10,18,7,9,3,2,4,1]
	heap = Heap(array)
	heap.heap_sort()
	print heap.array


if __name__ == '__main__':
	test_trie()
