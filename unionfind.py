
class UnionFind:
	def __init__(self, data):
		self.data = data
		self.parent = [-1] * len(data)

	def union(self, i, j):
		root1 = self.find(i)
		root2 = self.find(j)
		if root1 != root2:
			self.parent[root2] = self.parent[root1] + self.parent[root2]
			self.parent[root1] = root2

	def find(self, i):
		if self.parent[i] < 0:
			return i
		else:
			self.parent[i] = self.find(self.parent[i])
			return self.parent[i]

	def roots(self):
		result = []
		for x in range(len(self.data)):
			if self.parent[x] < 0:
				result.append(x)
		return result

	def count(self, i):
		i = self.find(i)
		return -self.parent[i]

	def counts(self):
		res = []
		for r in self.roots():
			res.append(self.count(r))
		res.sort(reverse=True)
		return res

	def dump(self):
		all = []
		for r in self.roots():
			res = []
			for x in range(len(self.data)):
				if self.find(x) == r:
					res.append(self.data[x])
			all.append(res)
		return all