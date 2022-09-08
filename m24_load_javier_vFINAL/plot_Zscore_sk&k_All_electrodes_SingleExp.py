# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:26:16 2021

@author: sound
"""
##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
######
import os
###########################
from scipy.stats import kurtosis
from scipy.stats import skew
##################################################
exp=0
#elc='S1-E2'
##################################################
#WTF
### Array for of times
wait,delay1,delay2,times=fn.times(epochs='yes')
epochs=(wait,delay1,delay2)
#####################################################
# Loading the files
path_to_file_directory = "C:/Users/sound/Documents/DatosLFP_Saskia/preprocessed_vfdt"
files = m24.getFilelist(path_to_file_directory)
nexp=len(files)# number of experiments
#######################################################
# loading the data 
exp_id=m24.getSessionID(files[exp])
data, electrodes, trials, info = m24.loadSaskia(files[exp]) # data of a exp
###################################
# loading every electrode data in a dictionary
lfp=fn.elc_dict(data,electrodes,trials)
#########################################################
actual="C:/Users/sound/Downloads/m24_load_javier"
directory=actual+f"/Raw_Sk&k_Zscore_plots/exp{exp_id}"
print(directory)
try:
    os.makedirs(directory)
except OSError:
    print("The directory creation %s fail" % directory)
else:
    print("The directory has been created: %s " % directory)


for ch in electrodes[1]:
    mg=np.mean(lfp[ch])
    stdg=np.std(lfp[ch])
    z=(lfp[ch]-mg)/stdg
    #mz=np.mean((lfp[ch]-mg)/stdg,axis=0)
    #sz=np.std(z,axis=0)
    #m=np.mean(lfp[ch],axis=0)
    #s=np.std(lfp[ch],axis=0)
    k=kurtosis(z,axis=0)
    sk=skew(z,axis=0)
    fig = plt.figure(figsize=(11,6))
    ax=fig.add_subplot(1,1,1)
    #ax.plot(times,mz,color='blue',alpha=0.7,label='Mean Z-score')
    #ax.plot(times,sz,color='green',alpha=0.7,label='stdz')
    ax.plot(times,k,color='blue',alpha=0.7,label='excess kurtosis')
    ax.plot(times,sk,color='red',alpha=0.7,label='skewness')
    ax.set_xlim(times[0],times[-1])
    fn.events(ax)
    ax.legend()
    ax.set_xlabel("Time[s]",fontsize=14)
    ax.set_ylabel("Units ",fontsize=14)
    ax.set_title(f'Skewness and kurtosis of z-scores of the electrode {ch}\n Exp {exp+1} ')
    fsave=(f"Raw_Sk&k_Zscore_plots/exp{exp_id}/Raw_Sk&k_Zscore_LFP_exp-{exp_id}_{ch}.svg")
    fig.savefig(fsave)
    print(fsave)
    plt.close('all')
    #####################
