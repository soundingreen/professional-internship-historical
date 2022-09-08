# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 23:12:57 2021

@author: sound
"""
##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
######Library for managing files
import os
########################### Excess Kurtosis and Skewness
from scipy.stats import kurtosis
from scipy.stats import skew
##
import glob

################
actual="C:/Users/sound/Downloads/m24_load_javier"
directory=actual+f"/Data/S1_NoConditions_Dist/SK"

x=fn.getFilelist(directory,prefixo='SK_exp*.npy')
nx=len(x)

data_wait=[]
data_delay1=[]
data_delay2=[]

for i in range(nx):
    exp=np.load(x[i])
    data_wait.append(exp[0])
    data_delay1.append(exp[1])
    data_delay2.append(exp[2])
    
data_wait=np.concatenate(data_wait)
data_delay1=np.concatenate(data_delay1)
data_delay2=np.concatenate(data_delay2)
############################################
actual="C:/Users/sound/Downloads/m24_load_javier"
directory=actual+f"/plots/S1_Dist_No_conditions_Allexp"
print(directory)
try:
    os.makedirs(directory)
except OSError:
    print("The directory creation %s fail" % directory)
else:
    print("The directory has been created: %s " % directory)
    
fig = plt.figure(figsize=(11,6))
ax=fig.add_subplot(1,1,1)
samples=(data_wait,data_delay1,data_delay2)
dists,bins=fn.getSamplesDistributions(samples)
dist1,dist2,dist3=dists
ax.set_yscale('log')
ax.plot(bins[1:],dist1, label='Wait',color='blue',alpha=0.7)
ax.plot(bins[1:],dist2,label='Delay 1',color='red',alpha=0.7)
ax.plot(bins[1:],dist3,label='Delay 2',color='green',alpha=0.7)
ax.set_title('Probability distribution of Skewness in S1\n during All epochs\n All exp \n without conditions')
ax.legend()
ax.set_xlabel('units')
ax.set_ylabel('Probability')
fsave=("plots/S1_Dist_No_conditions_Allexp/SK_S1_No_conditions_ALlepochs_log.svg")
fig.savefig(fsave)
print(fsave)
plt.close('all')

    
    