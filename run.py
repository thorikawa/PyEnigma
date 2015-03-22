#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import pyenigma

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-g', '--ground', required=True, help='ground settings ex. "FUQ"')
	parser.add_argument('-r', '--ring', required=False, default='AAA', help='ring settings ex. "ZZZ"')
	parser.add_argument('-o', '--order', required=False, default='123', help='robor order ex. "132"')
	parser.add_argument('-p', '--plug', required=False, default='', help='plug settings ex. "AH LY NS OR"')
	parser.add_argument('-t', '--turnover', action='store_true', help='set if you want to enable turnover')
	parser.add_argument('-u', '--reflector', required=False, default='A', help='reflector to set ex. "B"')
	parser.add_argument('-v', '--verbose', action='store_true', help='set if you want to display verbose logs')
	args = parser.parse_args()

	rotor_indices = [int(x) for x in args.order]
	rotors = [pyenigma.ROTORS[x-1] for x in rotor_indices]
	plugboard = pyenigma.Plugboard(args.plug)
	reflector = eval('pyenigma.REFLECTOR_' + args.reflector.upper())
	enigma = pyenigma.Enigma(rotors, reflector, plugboard, turnover=args.turnover)

	enigma.setWindowCharacters(args.ground)
	enigma.setRingSettings(args.ring)

	if args.verbose:
		print str(enigma)

	while True:
		input = raw_input()
		print '%s => %s' % (input, enigma.encode(input))

if __name__ == "__main__":
	main()
