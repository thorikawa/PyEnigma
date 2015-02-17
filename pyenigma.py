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

def main():
	rotor1 = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')
	rotor2 = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A', 'E')
	rotor3 = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A', 'V')
	reflector = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
	plugboard = Plugboard('')
	rotors = [rotor1, rotor2, rotor3]
	enigma = Enigma(rotors, reflector, plugboard)
	enigma.setWindowCharacters('ZRC')
	print enigma.encodeString('WETTERVORHERSAGEBISKAYA')

class Enigma:
	def __init__(self, rotors, reflector, plugboard):
		self.rotors = rotors
		self.reflector = reflector
		self.plugboard = plugboard

	def setWindowCharacters(self, windowCharacters):
		for i in range(len(self.rotors)):
			self.rotors[i].setWindowCharacter(windowCharacters[i])

	def step(self):
		turnover = True
		index = len(self.rotors) - 1
		while turnover and index >= 0:
			turnover = self.rotors[index].step()
			index = index - 1

	def encodeString(self, input):
		result = ""
		for c in input:
			result = result + self.encodeCharacter(c)
		return result

	def encodeCharacter(self, input):
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

class Rotor:
	def __init__(self, wiring, ring, notch):
		self.wiring = wiring
		self.ring = ord(ring) - ord('A')
		self.notch = ord(notch) - ord('A')
		self.window = 0

	def setWindowCharacter(self, windowCharacter):
		self.window = ord(windowCharacter) - ord('A')

	def step(self):
		turnover = (self.window == self.notch)
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
		pass

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

	def process(self, input):
		if input in self.matrix:
			return self.matrix[input]
		return input

def shift(input, value):
	return (input + value) % 26

if __name__ == "__main__":
	main()
