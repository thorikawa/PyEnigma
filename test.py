#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest, pyenigma

class TestFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test1(self):
		plugboard = pyenigma.Plugboard('')
		rotors = [pyenigma.ROTOR1, pyenigma.ROTOR2, pyenigma.ROTOR3]
		enigma = pyenigma.Enigma(rotors, pyenigma.REFLECTOR_B, plugboard, turnover=True)
		enigma.setWindowCharacters('AAA')
		enigma.setRingSettings('AAA')
		self.failUnlessEqual(enigma.encode('AAAAA'), 'BDZGO')
		enigma.setWindowCharacters('AAA')
		enigma.setRingSettings('AAA')
		self.failUnlessEqual(enigma.encode('BDZGO'), 'AAAAA')

if __name__ == '__main__':
	unittest.main()
