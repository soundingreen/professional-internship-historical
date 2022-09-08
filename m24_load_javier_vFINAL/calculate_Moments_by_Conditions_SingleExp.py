# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:36:21 2021

@author: sound
"""

##Library for loading data
import m24
##Basic library for working with arrays
import numpy as np
##Library for working with folders
import os
##Custom functions
import m24_functions as fn
#
import matplotlib.pyplot as plt
##################################################
exp=0
elc='S1-E2'
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
######################################################
#loading every electrode conditions in a dictionary
lfp=fn.conditions_dict(data, electrodes, trials, info)
#######################################################
#Moments
ch=elc
e=0
c1=lfp[ch][0][:,epochs[e]]
c2=lfp[ch][1][:,epochs[e]]
c3=lfp[ch][2][:,epochs[e]]
c4=lfp[ch][3][:,epochs[e]]
samples=[c1,c2,c3,c4]

resample=fn.getMomentsSamples(samples,moment='sk')
print(len(resample))
print(len(resample[0]))
print(len(resample[1]))
print(len(resample[2]))
print(len(resample[3]))

        