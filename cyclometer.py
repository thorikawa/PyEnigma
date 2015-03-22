#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pyenigma, string
from itertools import permutations, product
from unionfind import UnionFind

plugboard = pyenigma.Plugboard('')

for order in permutations(range(3)):
	print order
	rotors = [pyenigma.ROTORS[order[0]], pyenigma.ROTORS[order[1]], pyenigma.ROTORS[order[2]]]
	enigma = pyenigma.Enigma(rotors, pyenigma.REFLECTOR_B, plugboard)
	for ground in product(string.ascii_uppercase, repeat=3):
		# groundstr = ''.join(ground)
		# if groundstr != 'FUQ':
		#  	continue
		uf1 = UnionFind(list(string.ascii_uppercase))
		uf2 = UnionFind(list(string.ascii_uppercase))
		uf3 = UnionFind(list(string.ascii_uppercase))
		for c in string.ascii_uppercase:
			enigma.setWindowCharacters(ground)
			result = ''
			for x in range(6):
				result += enigma.encode(c)
			indices = [ord(x) - ord('A') for x in result]
			uf1.union(indices[0], indices[3])
			uf2.union(indices[1], indices[4])
			uf3.union(indices[2], indices[5])
		# print uf1.dump()
		# print uf2.dump()
		# print uf3.dump()
		counts1 = uf1.counts()
		counts2 = uf2.counts()
		counts3 = uf3.counts()
		# char1 = [len(counts1), counts1[0]]
		# char2 = [len(counts2), counts2[0]]
		# char3 = [len(counts3), counts3[0]]
		char1 = [len(counts1)] + counts1
		char2 = [len(counts2)] + counts2
		char3 = [len(counts3)] + counts3
		char = char1 + char2 + char3
		charstring = ' '.join([str(x) for x in char])
		print '%s %s' % (''.join(ground), charstring)
