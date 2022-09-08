# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:33:51 2021

@author: Javier Castilla
"""

##Library for loading data
import m24
##Basic library for working with arrays
import numpy as np
##Library for working with folders
import os
##Custom functions
import m24_functions as fn
#Library for plotting data
import matplotlib.pyplot as plt
##################################################
exp=0
###################################################
wait,delay1,delay2,times=fn.times(epochs='yes')
epochs=(wait,delay1,delay2)
ne=['Waiting','Delay1','Delay2']
######################################
# Loading the files
path_to_file_directory = "C:/Users/sound/Documents/DatosLFP_Saskia/preprocessed_vfdt"
files = m24.getFilelist(path_to_file_directory)
nexp=len(files)# number of experiments
#####################################################
# loading the data 
exp_id=m24.getSessionID(files[exp])
data, electrodes, trials, info = m24.loadSaskia(files[exp]) # data of a particular exp
####################################
#loading every electrode conditions in a dictionary
lfp=fn.conditions_dict(data, electrodes, trials, info)
####################################
#plotting
actual="C:/Users/sound/Downloads/m24_load_javier"
for e in range(len(epochs)):
    for ch in electrodes[1]:
        directory=actual+f"/Hiper/Excess_Kurtosis/Conditions_plots/exp{exp_id}/epoch{ne[e]}"
        print(directory)
        try:
            os.makedirs(directory)
        except OSError:
            print("The directory creation %s fail" % directory)
        else:
            print("The directory has been created: %s " % directory)
        
        c1=lfp[ch][0][:,epochs[e]]
        c2=lfp[ch][1][:,epochs[e]]
        c3=lfp[ch][2][:,epochs[e]]
        c4=lfp[ch][3][:,epochs[e]]
        samples=[c1,c2,c3,c4]
        resample=fn.getMomentsSamples(samples,moment='kr')
        cdist,bins=fn.getSamplesDistributions(resample)
        
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        ax.plot(bins[1:],cdist[0],label='c1')
        ax.plot(bins[1:],cdist[1],label='c2')
        ax.plot(bins[1:],cdist[2],label='c3')
        ax.plot(bins[1:],cdist[3],label='c4')
        ax.set_title(f'Probability distributions of Excess Kurtosis by conditions\n electrode{ch}\n During_{ne[e]}_epoch\n Exp id_{exp_id}')
        ax.set_xlabel('uV')
        ax.set_ylabel('Probability')
        ax.legend()
        fsave=(f"Hiper/Excess_Kurtosis/Conditions_plots/exp{exp_id}/epoch{ne[e]}/SingleCh_Excess_Kurtosis_Conditions_epoch{ne[e]}_{ch}.svg")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')
        