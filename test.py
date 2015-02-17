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
		self.failUnlessEqual(enigma.encodeString('AAAAA'), 'BDZGO')

	def test2(self):
		# test different ring setting
		rotor1 = pyenigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'B', 'Q')
		rotor2 = pyenigma.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'B', 'E')
		rotor3 = pyenigma.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'B', 'V')
		reflector = pyenigma.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
		plugboard = pyenigma.Plugboard('')
		rotors = [rotor1, rotor2, rotor3]
		enigma = pyenigma.Enigma(rotors, reflector, plugboard)
		self.failUnlessEqual(enigma.encodeString('AAAAA'), 'EWTYX')

	def test3(self):
		# test plugboard
		rotor1 = pyenigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')
		rotor2 = pyenigma.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A', 'E')
		rotor3 = pyenigma.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A', 'V')
		reflector = pyenigma.Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
		plugboard = pyenigma.Plugboard('ZY GO')
		rotors = [rotor1, rotor2, rotor3]
		enigma = pyenigma.Enigma(rotors, reflector, plugboard)
		self.failUnlessEqual(enigma.encodeString('AAAAA'), 'BDYOG')

if __name__ == '__main__':
	unittest.main()
