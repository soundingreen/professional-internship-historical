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
####################################
#loading every electrode conditions in a dictionary
lfp=fn.conditions_dict(data, electrodes, trials, info)

