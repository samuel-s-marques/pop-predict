#coding: utf-8
#!/usr/bin/python3

'''
Predicts world population based on
past years' population, using 
linear regression.
'''

import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np
import scipy.interpolate
import scipy.misc

from utils import *
import sys

class Countries:
	def predict(year):
		years = [
		 2000,
		 2001,
		 2002,
		 2003,
		 2004,
		 2005,
		 2006,
		 2007,
		 2008, 
		 2009,
		 2010,
		 2011,
		 2012,
		 2013,
		 2014,
		 2015,
		 2016,
		 2017,
		 2018,
		 2019,
		 2020,
		]

		population = [
		 6143493823,
		 6222626606,
		 6301773188,
		 6381185114,
		 6461159389,
		 6541907027,
		 6623847913,
		 6705946610,
		 6789088686,
		 6872767093,
		 6956823603,
		 7041194301,
		 7125828059,
		 7210581976,
		 7295290765,
		 7379797139,
		 7464022049,
		 7547858925,
		 7631091040,
		 7713468100,
		 7794798739,
		]

		x = np.asarray(years)
		y = np.asarray(population)

		f = scipy.interpolate.interp1d(x, y)

		dx = 0.01
		x0 = x[-1] - 2 * dx
		first = scipy.misc.derivative(f, x0, dx=dx, n=1)
		second = scipy.misc.derivative(f, x0, dx=dx, n=2)

		forecast = lambda x_new: np.poly1d([second/2, first, f(x[-1])])(x_new - x[-1])

		print('Year: ' + str(year))
		print('Population: \n\t' + str(Utils.round(forecast(year))) + '\n\t{:,}'.format(forecast(year)))

def main():
	if(len(sys.argv) > 2 or len(sys.argv) < 2):
		print("\n\predict.py YEAR")
	else:
		Countries.predict(int(sys.argv[1]))

if __name__ == '__main__':
	main()
