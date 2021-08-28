from math import *
from matplotlib import *
from numpy import *
from pylab import *
def gauss_formula(n):
	return (n/log(n))
x=arange(1.01,100000,1)
plot(x,gauss_formula(x),color='blue',marker=".")
title("Gauss prime formula (the primes less than x)",color="red",size="10")
show()