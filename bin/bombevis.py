#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, Queue, pyenigma, time, argparse
from PyQt4 import QtGui, QtCore

def main():

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-g', '--ground', required=True, help='ground settings ex. "FUQ"')
	parser.add_argument('-v', '--verbose', action='store_true', help='set if you want to display verbose logs')
	args = parser.parse_args()

	# Example from "From Bombe ‘stops’ to Enigma keys" by Frank Carter
	# The correct answer is not given
	# menu = Menu([
	# 	('A', 'J', 1),
	# 	('T', 'B', 2),
	# 	('S', 'X', 3),
	# 	('J', 'T', 4),
	# 	('B', 'I', 5),
	# 	('M', 'Z', 6),
	# 	('Y', 'M', 7),
	# 	('A', 'S', 8),
	# 	('J', 'P', 9),
	# 	('Z', 'R', 10),
	# 	('Y', 'Q', 12),
	# 	('Y', 'F', 13),
	# 	('Y', 'T', 14),
	# 	('R', 'M', 15),
	# ])

	# Example from 
	# https://cryptocellar.web.cern.ch/cryptocellar/Shaylor/bombe.html
	# https://cryptocellar.web.cern.ch/cryptocellar/Shaylor/bombeapp.html
	# The correct answer is 123-CBA (AH) (LY) (NS) (OR)
	menu = Menu([
		('B', 'F', 1),
		('L', 'Y', 2),
		('E', 'O', 3),
		('T', 'K', 4),
		('C', 'V', 5),
		('H', 'N', 6),
		('L', 'J', 7),
		('E', 'D', 8),
		('Y', 'E', 9),
		('P', 'V', 10),
		('A', 'C', 11),
		('R', 'N', 12),
		('K', 'N', 13),
		('E', 'P', 14),
		('N', 'W', 15),
		('G', 'N', 16),
		('L', 'Z', 17),
		('A', 'R', 18),
		('N', 'G', 19),
		('D', 'N', 20),
	])

	# right answer
	# rotorSettings = RotorSettings('CBA')
	rotorSettings = RotorSettings(args.ground)

	bombe = Bombe(menu)
	app = QtGui.QApplication(sys.argv)
	gui = Gui(bombe)
	gui.setRotorSettings(rotorSettings)
	gui.show()

	sys.exit(app.exec_())

class Bombe:
	def __init__(self, menu):
		self.menu = menu
		plugboard = pyenigma.Plugboard('')
		rotors = [pyenigma.ROTOR1, pyenigma.ROTOR2, pyenigma.ROTOR3]
		self.enigma = pyenigma.Enigma(rotors, pyenigma.REFLECTOR_B, plugboard, turnover=False)

	def run(self):
		while not self.q.empty():
			st = self.q.get()
			result = []
			print '================'
			# d: d[0] is stickered with d[1] and d[1] to be input for unstickered enigma.
			for d in [(st[0], st[1]), (st[1], st[0])]:
				if d in self.visited:
					continue
				self.visited.add(d)

				targets = self.menu.get(d[0])
				# t: t[0] is an output character after the plugboard and t[1] is an index number in the crib.
				for t in targets:
					rs = self.rotorSettings.getSettingsAt(t[1]-1)
					self.enigma.setWindowCharacters(rs)
					raw_output = self.enigma.encode(d[1])
					# now raw_output is supposed to be stickered with t[0]
					deduction = (raw_output, t[0])
					if deduction in self.visited:
						continue

					self.q.put(deduction)
					self.checked[ord(raw_output)-65][ord(t[0])-65] = 1
					self.checked[ord(t[0])-65][ord(raw_output)-65] = 1

					print '%s => %s => %s => %s at %s' % (d[0], d[1], raw_output, t[0], rs)

					result.append((raw_output, t[0]))
			yield result

	def setRotorSettings(self, rotorSettings):
		self.rotorSettings = rotorSettings
		self.q = Queue.Queue()
		self.visited = set()
		self.checked = [[0 for i in range(26)] for j in range(26)]

	def setInitialAssumption(self, initial_assumption):
		self.centralLetter = initial_assumption[0]
		self.q.put(initial_assumption)
		self.checked[ord(initial_assumption[0])-65][ord(initial_assumption[1])-65] = 1
		self.checked[ord(initial_assumption[1])-65][ord(initial_assumption[0])-65] = 1

	def isStop(self):
		count = 0
		for i in range(26):
			if self.checked[ord(self.centralLetter)-65][i] > 0:
				count = count + 1
		return count != 26

class RotorSettings:
	def __init__(self, initialSettings):
		self.settings = initialSettings

	def __str__(self):
		return self.get()

	def set(self, settings):
		self.settings = settings

	def get(self):
		return self.settings

	def next(self):
		self.settings = self.getSettingsAt(1, True)

	def getSettingsAt(self, step, carry=False):
		result = self.settings
		size = len(self.settings)
		index = size-1
		while True:
			ch = self.settings[index]
			new_character = (ord(ch) - 65 + step)
			do_next = False
			if carry and new_character >= 26 and index > 0:
				do_next = True

			new_character = chr(new_character % 26 + 65)
			result = result[:index] + new_character + result[index+1:]
			if do_next:
				index = index - 1
			else:
				break
		return result

class Menu:
	def __init__(self, data_array):
		self.dict = {}
		for c in [chr(x) for x in range(65, 65+26)]:
			self.dict[c] = []
		for data in data_array:
			self.add(data)

	def add(self, data):
		self.dict[data[0]].append((data[1], data[2]))
		self.dict[data[1]].append((data[0], data[2]))

	def get(self, ch):
		return self.dict[ch]

class Gui(QtGui.QWidget):
	def __init__(self, bombe):
		super(Gui, self).__init__()
		self.checkboxes = []
		self.initUi()
		self.bombe = bombe

	def initUi(self):
		boxLayout = QtGui.QVBoxLayout()

		self.header = QtGui.QLabel('setting')

		gridWidget = QtGui.QWidget()
		gridLayout = QtGui.QGridLayout()
		
		for position in [(i,j) for i in range(27) for j in range(27)]:

			if position[0] == 0 and position[1] == 0:
				name = ' '
			elif position[0] == 0:
				name = chr(65 + position[1] - 1)
			elif position[1] == 0:
				name = chr(65 + position[0] - 1)
			else:
				name = ''

			if name == '':
				cb = QtGui.QCheckBox()
				gridLayout.addWidget(cb, *position)
				self.checkboxes.append(cb)
			else:
				button = QtGui.QLabel(name)
				gridLayout.addWidget(button, *position)

		gridWidget.setLayout(gridLayout)

		stepButton = QtGui.QPushButton('Step')
		stepButton.clicked.connect(self.step)

		runButton = QtGui.QPushButton('Run')
		runButton.clicked.connect(self.run)

		boxLayout.addWidget(self.header)
		boxLayout.addWidget(stepButton)
		boxLayout.addWidget(runButton)
		boxLayout.addWidget(gridWidget)

		self.resize(250, 150)
		self.move(300, 300)
		self.setLayout(boxLayout)
		self.setWindowTitle('Simple')

	def setRotorSettings(self, rotorSettings):
		self.bombe.setRotorSettings(rotorSettings)
		self.setHeaderText('Rotor: %s' % (rotorSettings))

		initialAssumption = ('N', 'S')
		self.bombe.setInitialAssumption(initialAssumption)
		self.check(*initialAssumption)

		self.generator = self.bombe.run()

	def step(self):
		try:
			newPairs = self.generator.next()
			for pair in newPairs:
				self.check(pair[0], pair[1])
			QtCore.QCoreApplication.processEvents()
			return True
		except StopIteration:
			return False

	def run(self):
		while True:
			if not self.step():
				break
			time.sleep(0.01)

	def check(self, ch1, ch2):
		ch1 = ord(ch1) - 65
		ch2 = ord(ch2) - 65
		index1 = ch1 * 26 + ch2
		index2 = ch2 * 26 + ch1
		# print "check %d %d of %d" % (index1, index2, len(self.checkboxes))
		self.checkboxes[index1].setChecked(True)
		self.checkboxes[index2].setChecked(True)

	def setHeaderText(self, text):
		self.header.setText(text)

if __name__ == '__main__':
	main()
