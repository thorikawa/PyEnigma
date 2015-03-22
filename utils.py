

def index(x):
	if ord(x) >= ord('a'):
		return ord(x) - ord('a')
	else:
		return ord(x) - ord('A')

class Permutation:
	def __init__(self, string=None, nums=None):
		if nums != None:
			self.perm = nums
		else:
			self.perm = [index(x) for x in string]

	def __str__(self):
		return ''.join([chr(x + ord('A')) for x in self.perm])

	def __mul__(a, b):
		return Permutation(nums=[b.get(a.get(i)) for i in range(26)])

	def __invert__(obj):
		def r(t):
			for i in range(26):
				if obj.get(i) == t:
					return i
			return -1
		return Permutation(nums=[r(x) for x in range(26)])

	def get(self, i):
		return self.perm[i]

	def cycles(self):
		flags = [0] * 26
		res = []
		for i in range(26):
			cur = i
			cycle = []
			while flags[cur] == 0:
				cycle.append(cur)
				flags[cur] = 1
				cur = self.perm[cur]
			if len(cycle) == 0:
				continue
			res.append([chr(x + ord('A')) for x in cycle])
		return res

	@staticmethod
	def rotation(n):
		return Permutation(nums=[(x + n) % 26 for x in range(26)])
