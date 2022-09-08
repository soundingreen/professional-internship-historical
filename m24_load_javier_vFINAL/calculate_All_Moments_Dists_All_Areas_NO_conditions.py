# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 01:39:49 2021

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
actual="D:/m24_load_javier"
s_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']
for  a in s_areas:
    ##############
    directory=actual+f"/Data/{a}_NoConditions_Dist/RAW"
    try:
        os.makedirs(directory)
    except:
        None
    ##############
    directory=actual+f"/Data/{a}_NoConditions_Dist/MEAN"
    try:
        os.makedirs(directory)
    except:
        None
    ##############
    directory=actual+f"/Data/{a}_NoConditions_Dist/STD"
    try:
        os.makedirs(directory)
    except:
        None
    ###############
    directory=actual+f"/Data/{a}_NoConditions_Dist/KUR"
    try:
        os.makedirs(directory)
    except:
        None
    ################
    directory=actual+f"/Data/{a}_NoConditions_Dist/SK"
    try:
        os.makedirs(directory)
    except:
        None
    
    #######################################################################
    sareas=[a]
    for exp in range(nexp):
        # loading the data of one exp 
        exp_id=m24.getSessionID(files[exp])
        data, electrodes, trials, info = m24.loadSaskia(files[exp]) # data of a exp
        ###################################
        # loading every electrode data in a dictionary
        lfp=fn.elc_dict(data,electrodes,trials)
        # loading every area data in a dictionary joining electrodes in an unique array
        lfp_areas=fn.extract_trials_areas(lfp, electrodes,s_areas=sareas)
        if list(lfp_areas.keys())!=[]:
            area=list(lfp_areas.keys())[0]
            x=lfp_areas[area][:,wait]
            x2=lfp_areas[area][:,delay1]
            x3=lfp_areas[area][:,delay2]
            ##################RAW
            raw_samples=np.array(lfp_areas[area])
            rfsave=f'D:/m24_load_javier/Data/{a}_NoConditions_Dist/RAW/RAW_exp_{exp:03}_samples'
            np.save(rfsave,raw_samples,allow_pickle=False)
            print(rfsave)
            ##################MEAN
            m=kurtosis(x,axis=1)
            m2=kurtosis(x2,axis=1)
            m3=kurtosis(x3,axis=1)
            mean_samples=np.array([m,m2,m3])
            mfsave=f'D:/m24_load_javier/Data/{a}_NoConditions_Dist/MEAN/MEAN_exp_{exp:03}_samples'
            np.save(mfsave,mean_samples,allow_pickle=False)
            print(mfsave)
            ###################STD
            std=np.std(x,axis=1)
            std2=np.std(x2,axis=1)
            std3=np.std(x3,axis=1)
            std_samples=np.array([std,std2,std3])
            sfsave=f'D:/m24_load_javier/Data/{a}_NoConditions_Dist/STD/STD_exp_{exp:03}_samples'
            np.save(sfsave,std_samples,allow_pickle=False)
            print(sfsave)
            ##################KUR
            k=kurtosis(x,axis=1)
            k2=kurtosis(x2,axis=1)
            k3=kurtosis(x3,axis=1)
            kur_samples=np.array([k,k2,k3])
            kfsave=f'D:/m24_load_javier/Data/{a}_NoConditions_Dist/KUR/KUR_exp_{exp:03}_samples'
            np.save(kfsave,kur_samples,allow_pickle=False)
            print(kfsave)   
            ##################SK
            sk=kurtosis(x,axis=1)
            sk2=kurtosis(x2,axis=1)
            sk3=kurtosis(x3,axis=1)
            sk_samples=np.array([sk,sk2,sk3])
            skfsave=f'D:/m24_load_javier/Data/{a}_NoConditions_Dist/SK/SK_exp_{exp:03}_samples'
            np.save(skfsave,sk_samples,allow_pickle=False)
            print(skfsave) 
        