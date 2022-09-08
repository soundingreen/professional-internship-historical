# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:23:11 2021

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
##################################################
#all_Enames=[]
#for e in range(nexp):
    # loading the data of one exp 
    #data, electrodes, trials, info = m24.loadSaskia(files[e]) # data of a 
    #for i in electrodes[1]:
        #if i not in all_Enames:
            #all_Enames.append(i)

#print(all_Enames)


allN=['S1-E1', 'S1-E2', 'S1-E3', 'S1-E4', 'S1-E6', 'S2-E8', 'S2-E9', 'S2-E10', 'S2-E11', 'MPC-left-E17', 'MPC-left-E19', 'MPC-left-E20', 'MPC-left-E21', 'VPC-E22', 'VPC-E24', 'VPC-E28', 'S1-E5', 'S2-E13', 'S2-E14', 'MPC-left-E15', 'MPC-left-E16', 'MPC-left-E18', 'VPC-E23', 'VPC-E27', 'S2-E12', 'S1-E7', 'VPC-E25', 'VPC-E26', 'M1-E29', 'M1-E30', 'M1-E32', 'M1-E34', 'DPC-E25', 'DPC-E26', 'DPC-E28', 'M1-E31', 'DPC-E22', 'DPC-E23', 'DPC-E24', 'DPC-E27', 'M1-E33', 'MPC-right-E15', 'MPC-right-E16', 'MPC-right-E17', 'MPC-right-E18', 'MPC-right-E19', 'MPC-right-E20', 'MPC-right-E21']
print(allN)


all_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']