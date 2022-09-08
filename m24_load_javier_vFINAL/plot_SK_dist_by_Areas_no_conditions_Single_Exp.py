# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:47:30 2021

@author: sound
"""
##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
##########
import os
###########################
from scipy.stats import kurtosis
from scipy.stats import skew
##################################################
exp=0
#ch='S1-E2'
##################################################
#WTF
### Array for of times
wait,delay1,delay2,times=fn.times(epochs='yes')
epochs=(wait,delay1,delay2)
ne=['Waiting','Delay1','Delay2']
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
# loading every area data in a dictionary joining electrodes in an unique array
lfp_areas=fn.extract_trials_areas(lfp, electrodes)
#########################################################
areas=list(lfp_areas.keys())
#########################################################
actual="C:/Users/sound/Downloads/m24_load_javier"

for area in areas:
    directory=actual+f"/SK_No_conditions_Join_e_plots/exp{exp_id}/All_epochs"
    print(directory)
    try:
        os.makedirs(directory)
    except OSError:
        print("The directory creation %s fail" % directory)
    else:
        print("The directory has been created: %s " % directory)
    
    fig = plt.figure(figsize=(11,6))
    ax=fig.add_subplot(1,1,1)
    x=lfp_areas[area][:,wait]
    x2=lfp_areas[area][:,delay1]
    x3=lfp_areas[area][:,delay2]
    sk=skew(x,axis=1)
    sk2=skew(x2,axis=1)
    sk3=skew(x3,axis=1)
    samples=(sk,sk2,sk3)
    dists,bins=fn.getSamplesDistributions(samples,nbins=30)
    dist1,dist2,dist3=dists
    ax.plot(bins[1:],dist1, label='Wait',color='blue',alpha=0.7)
    ax.plot(bins[1:],dist2,label='Delay 1',color='red',alpha=0.7)
    ax.plot(bins[1:],dist3,label='Delay 2',color='green',alpha=0.7)
    ax.set_title(f'Probability distribution of Skewness in the area {area}\n during All epochs\n Exp id_{exp_id} \n without conditions')
    ax.legend()
    ax.set_xlabel('units')
    ax.set_ylabel('Probability')
    fsave=(f"SK_No_conditions_Join_e_plots/exp{exp_id}/All_epochs/SingleCh_SK_No_conditions_Area{area}.svg")
    fig.savefig(fsave)
    print(fsave)
    plt.close('all')
    

