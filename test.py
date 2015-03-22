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

	# more practical test case
	# message from http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Messages
	# and http://wiki.franklinheath.co.uk/index.php/Enigma/Sample_Decrypts
	def test3(self):
		input = 'GCDSEAHUGWTQGRKVLFGXUCALXVYMIGMMNMFDXTGNVHVRMMEVOUYFZSLRHDRRXFJWCFHUHMUNZEFRDISIKBGPMYVXUZ'
		output = 'FEINDLIQEINFANTERIEKOLONNEBEOBAQTETXANFANGSUEDAUSGANGBAERWALDEXENDEDREIKMOSTWAERTSNEUSTADT'

		plugboard = pyenigma.Plugboard('AM FI NV PS TU WZ')
		rotors = [pyenigma.ROTOR2, pyenigma.ROTOR1, pyenigma.ROTOR3]
		enigma = pyenigma.Enigma(rotors, pyenigma.REFLECTOR_A, plugboard, turnover=True)
		enigma.setRingSettings('XMV')

		enigma.setWindowCharacters('ABL')
		self.failUnlessEqual(enigma.encode(input), output)

		enigma.setWindowCharacters('ABL')
		self.failUnlessEqual(enigma.encode(output), input)

if __name__ == '__main__':
	unittest.main()
