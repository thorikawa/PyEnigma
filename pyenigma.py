#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
__author__ = "Takahiro Poly Horikawa"
__copyright__ = "Copyright 2015, Takahiro Poly Horikawa"
__credits__ = ["Takahiro Poly Horikawa"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Takahiro Poly Horikawa"
__email__ = "horikawa.takahiro@gmail.com"
__status__ = "Alpha"

TODO
- Support Entry Wheel
'''

class Enigma:
	def __init__(self, rotors, reflector, plugboard, turnover=True):
		self.turnover = turnover
		self.rotors = rotors
		self.reflector = reflector
		self.plugboard = plugboard

	def __str__(self):
		rotors_str = ', '.join([str(r) for r in self.rotors])
		return "{\nturnover=%s\rrotors=%s\nplugboard=%s\nreflector=%s\n}" % (self.turnover, rotors_str, self.plugboard, self.reflector)

	def getWindowCharacters(self):
		result = ""
		for i in range(len(self.rotors)):
			result += chr(self.rotors[i].window + ord('A'))
		return result

	def setWindowCharacters(self, windowCharacters):
		for i in range(len(self.rotors)):
			self.rotors[i].setWindowCharacter(windowCharacters[i])

	def setRingSettings(self, ringCharacters):
		for i in range(len(self.rotors)):
			self.rotors[i].setRingSetting(ringCharacters[i])

	def step(self):
		index = len(self.rotors) - 1
		while True:
			isTurnover = self.rotors[index].step()
			if self.turnover and isTurnover and index >= 0:
				index = index - 1
				continue
			else:
				break

	def encode(self, input, step=True):
		if len(input) == 1:
			if step:
				self.step()
			output = self.plugboard.process(input)
			for rotor in reversed(self.rotors):
				output = rotor.forward(output)
				# print "=> %s" % output
			output = self.reflector.process(output)
			# print "=> %s" % output
			for rotor in self.rotors:
				output = rotor.backward(output)
				# print "=> %s" % output
			return self.plugboard.process(output)
		else:
			result = ""
			for c in input:
				result = result + self.encode(c, step)
			return result

class Rotor:
	def __init__(self, wiring, ring, notch):
		self.wiring = wiring
		self.ring = ord(ring) - ord('A')
		self.notches = [ord(x) - ord('A') for x in notch]
		self.window = 0

	def __str__(self):
		return "{wiring=%s ring=%s}" % (self.wiring, self.ring+1)

	def setWindowCharacter(self, windowCharacter):
		self.window = ord(windowCharacter) - ord('A')

	def setRingSetting(self, ringCharacter):
		self.ring = ord(ringCharacter) - ord('A')

	def step(self):
		turnover = (self.window in self.notches)
		self.window = shift(self.window, 1)
		return turnover

	def forward(self, input):
		inputValue = ord(input) - ord('A')

		wire_start = shift(shift(inputValue, -self.ring), self.window)
		wire_end = ord(self.wiring[wire_start]) - ord('A')
		outputValue = shift(shift(wire_end, self.ring), -self.window)
		output = chr(outputValue + ord('A'))
		return output

	def backward(self, input):
		inputValue = ord(input) - ord('A')

		wire_start = shift(shift(inputValue, self.window), -self.ring)
		for i in range(0, 26):
			if ord(self.wiring[i]) - ord('A') == wire_start:
				wire_end = i
				break
		outputValue = shift(shift(wire_end, - self.window), self.ring)
		output = chr(outputValue + ord('A'))
		return output

class Reflector:
	def __init__(self, wiring):
		self.wiring = wiring

	def __str__(self):
		return str(self.wiring)

	def process(self, input):
		inputValue = ord(input) - ord('A')
		return self.wiring[inputValue]

class Plugboard:
	def __init__(self, pairs):
		self.matrix = {}
		if pairs:
			for pair in pairs.split(" "):
				if len(pair) != 2:
					continue
				self.matrix[pair[0]] = pair[1]
				self.matrix[pair[1]] = pair[0]

	def __str__(self):
		return str(self.matrix)

	def process(self, input):
		if input in self.matrix:
			return self.matrix[input]
		return input

ROTOR1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')
ROTOR2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A', 'E')
ROTOR3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A', 'V')
ROTOR4 = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'A', 'J')
ROTOR5 = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'A', 'Z')
ROTOR6 = Rotor('JPGVOUMFYQBENHZRDKASXLICTW', 'A', 'MZ')
ROTOR7 = Rotor('NZJHGRCXMYSWBOUFAIVLPEKQDT', 'A', 'MZ')
ROTOR8 = Rotor('FKQHTLXOCBJSPDZRAMEWNIUYGV', 'A', 'MZ')
ROTORS = [ROTOR1, ROTOR2, ROTOR3, ROTOR4, ROTOR5, ROTOR6, ROTOR7, ROTOR8]
REFLECTOR_A = Reflector('EJMZALYXVBWFCRQUONTSPIKHGD')
REFLECTOR_B = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
REFLECTOR_C = Reflector('FVPJIAOYEDRZXWGCTKUQSBNMHL')

def shift(input, value):
	return (input + value) % 26
