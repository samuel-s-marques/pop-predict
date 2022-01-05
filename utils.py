#coding: utf-8
#!/usr/bin/python3

'''
To round and format large numbers

Got from: https://stackoverflow.com/questions/3154460/python-human-readable-large-numbers
'''

import math

class Utils:
	def round(n):
		suffixes = ['', ' thousand', ' million', ' billion', ' trillion']

		n = float(n)
		millidx = max(0, min(len(suffixes) - 1, int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

		return '{:.0f}{}'.format(n / 10 ** (3 * millidx), suffixes[millidx])
