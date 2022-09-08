##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
##Library for working with folders
import os
## Custom funtions
import m24_functions as fn
###  Standard deviation, skewness and kurtosis
import numpy.std as std
from scipy.stats import skew
from scipy.stats import kurtosis
##################################################

### Array for of times
times=np.arange(-2.001, 8, 0.001)

#Index for every epoch of interest

#indexes of pre-stimulus wait
prestimulus=times[np.nonzero(times<0)]
#index of interstimulus delay
infd=np.nonzero(times>=0.5)
supd=np.nonzero(times<=3.5)
first_delay=np.intersect1d(infd,supd)
#index of second delay
inf2=np.nonzero(times>=4.5)
sup2=np.nonzero(times<=6.5)
second_delay=np.intersect1d(inf2,sup2)

#####################################################


#plt.hist(bins[:-1],bins,weights=distc4)
plt.plot(bins[1:],distc1)

