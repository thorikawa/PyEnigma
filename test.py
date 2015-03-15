#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest, pyenigma

class TestFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test1(self):
		rotor1 = pyenigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')
		rotor2 = pyenigma.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A', 'E')
		rotor3 = pyenigma.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A', 'V')
		reflector = pyenigma.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
		plugboard = pyenigma.Plugboard('')
		rotors = [rotor1, rotor2, rotor3]
		enigma = pyenigma.Enigma(rotors, reflector, plugboard)
		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('AAAAA'), 'BDZGO')
		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('BDZGO'), 'AAAAA')

if __name__ == '__main__':
	unittest.main()
