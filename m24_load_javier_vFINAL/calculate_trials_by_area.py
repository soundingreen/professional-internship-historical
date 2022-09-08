# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:03:40 2021

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
print(areas)


