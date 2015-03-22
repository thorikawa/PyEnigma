#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import Permutation

# From 
# A = (as)(br)(cw)(di)(ev)(fh)(gn)(jo)(kl)(my)(pt)(qx)(uz)
# B = (ay)(bj)(ct)(dk)(ei)(fn)(gx)(hl)(mp)(ow)(qr)(su)(vz)
# C = (ax)(bl)(cm)(dg)(ei)(fo)(hv)(ju)(kr)(np)(qs)(tz)(wy)
# D = (as)(bw)(cr)(dj)(ep)(ft)(gq)(hk)(iv)(lx)(mo)(nz)(uy)
# E = (ac)(bp)(dk)(ez)(fh)(gt)(io)(jl)(ms)(nq)(rv)(uw)(xy)
# F = (aw)(bx)(co)(df)(ek)(gu)(hi)(jz)(lv)(mq)(ns)(py)(rt)
a = Permutation('SRWIVHNFDOLKYGJTXBAPZECQMU')
b = Permutation('YJTKINXLEBDHPFWMRQUCSZOGAV')
c = Permutation('XLMGIODVEURBCPFNSKQZJHYAWT')
d = Permutation('SWRJPTQKVDHXOZMEGCAFYIBLUN')
e = Permutation('CPAKZHTFOLDJSQIBNVMGWRUYXE')
f = Permutation('WXOFKDUIHZEVQSCYMTNRGLABPJ')

# From Tony Sale's example
# a = Permutation('SNGIPRCXDUOVWBKETFAQJLMHZY')
# b = Permutation('YNUOIZTMEKJWHBDRVPXGCQLSAF')
# c = Permutation('XQHVIULCEMNGJKYSBWPZFDRAOT')
# d = Permutation('SCBNLZOJUHQEWDGXKYAVITMPRF')
# e = Permutation('JMIKRQUTCADZBONWFEVHGSPYXL')
# f = Permutation('BASZKNLWRYEGQFVUMICXPOHTJD')

print 'A=%s' % a.cycles()
print 'B=%s' % b.cycles()
print 'C=%s' % c.cycles()
print 'D=%s' % d.cycles()
print 'E=%s' % e.cycles()
print 'F=%s' % f.cycles()
print 'AD = %s' % (a*d).cycles()
print 'BE = %s' % (b*e).cycles()
print 'CF = %s' % (c*f).cycles()

# (ap)(bl)(cz)(fh)(jk)(qu).
s = Permutation('PLZDEHGFIKJBMNOAURSTQVWXYC')
# IZ ES CY XV AM KR
# s = Permutation('MBYDSFGHZJRLANOPQKETUXWVCI')

p1 = Permutation.rotation(1)
p2 = Permutation.rotation(2)
p3 = Permutation.rotation(3)
p4 = Permutation.rotation(4)
p5 = Permutation.rotation(5)
p6 = Permutation.rotation(6)

u = (~p1) * (~s) * a * s * p1
v = (~p2) * (~s) * b * s * p2
w = (~p3) * (~s) * c * s * p3
x = (~p4) * (~s) * d * s * p4
y = (~p5) * (~s) * e * s * p5
z = (~p6) * (~s) * f * s * p6

uv = u * v
vw = v * w
wx = w * x

print 'uv=%s %s' % (uv, uv.cycles())
print 'vw=%s %s' % (vw, vw.cycles())
print 'wx=%s %s' % (wx, wx.cycles())

# enigma1
# n = Permutation('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
# n = Permutation('AJDKSIRUXBLHWTMCQGZNPYFVOE')
n = Permutation('BDFHJLCPRTXVZNYEIWGAKMUSQO')
# n = Permutation('ESOVPZJAYQUIRHXLNFTGKDCMWB')
# n = Permutation('VZBRGITYUPSDNHLXAWMJQOFECK')
# n = Permutation('JPGVOUMFYQBENHZRDKASXLICTW')
# n = Permutation('NZJHGRCXMYSWBOUFAIVLPEKQDT')
# n = Permutation('FKQHTLXOCBJSPDZRAMEWNIUYGV')

# German Railway (Rocket)
# n = Permutation('JGDQOXUSCAMIFRVTPNEWKBLZYH')
# n = Permutation('NTZPSFBOKMWRCJDIVLAEYUXHGQ')
# n = Permutation('JVIUBHTCDYAKEQZPOSGXNRMWFL')

# commercial enigma
# n = Permutation('DMTWSILRUYQNKFEJCAZBPGXOHV')
# n = Permutation('HQZGPJTMOBLNCIFDYAWVEUSRKX')
# n = Permutation('UQNTLSZFMREHDPXKIBVYGJCWOA')

for i in range(26):
	p = Permutation.rotation(i)
	nn = p * n * (~p)
	res = []
	for j in range(26):
		q = Permutation.rotation(j)
		res.append(str(~q * nn))
	print '%d %s %s' % (i, nn, ' '.join(res))
