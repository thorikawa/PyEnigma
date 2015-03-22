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
		enigma.setRingSettings('AAA')

		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('AAAAA'), 'BDZGO')
		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('BDZGO'), 'AAAAA')

	# test for different ring settings
	# from wikipedia example: http://en.wikipedia.org/wiki/Enigma_rotor_details#Ring_setting
	def test2(self):
		plugboard = pyenigma.Plugboard('')
		rotors = [pyenigma.ROTOR1, pyenigma.ROTOR2, pyenigma.ROTOR3]
		enigma = pyenigma.Enigma(rotors, pyenigma.REFLECTOR_B, plugboard, turnover=True)
		enigma.setRingSettings('BBB')

		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('AAAAA'), 'EWTYX')
		enigma.setWindowCharacters('AAA')
		self.failUnlessEqual(enigma.encode('EWTYX'), 'AAAAA')

if __name__ == '__main__':
	unittest.main()
