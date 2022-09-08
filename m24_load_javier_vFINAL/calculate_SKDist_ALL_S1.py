# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:27:52 2021

@author: sound
"""
# -*- coding: utf-8 -*-

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
##################################################
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
actual="C:/Users/sound/Downloads/m24_load_javier"
directory=actual+f"/Data/S1_NoConditions_Dist/SK"
try:
    os.makedirs(directory)
except:
    None

for exp in range(nexp):
    # loading the data of one exp 
    exp_id=m24.getSessionID(files[exp])
    data, electrodes, trials, info = m24.loadSaskia(files[exp]) # data of a exp
    ###################################
    # loading every electrode data in a dictionary
    lfp=fn.elc_dict(data,electrodes,trials)
    # loading every area data in a dictionary joining electrodes in an unique array
    lfp_areas=fn.extract_trials_areas(lfp, electrodes,s_areas=['S1'])
    area=list(lfp_areas.keys())[0]
    x=lfp_areas[area][:,wait]
    x2=lfp_areas[area][:,delay1]
    x3=lfp_areas[area][:,delay2]
    sk=skew(x,axis=1)
    sk2=skew(x2,axis=1)
    sk3=skew(x3,axis=1)
    samples=np.array([sk,sk2,sk3])
    fsave=f'Data/S1_NoConditions_Dist/SK/SK_exp_{exp:03}_samples'
    np.save(fsave,samples,allow_pickle=False)
    print(fsave)
    
    

        