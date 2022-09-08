##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
##########
import os
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
#########################################################
actual="C:/Users/sound/Downloads/m24_load_javier"
for e in range(len(epochs)):
    for ch in electrodes[1]:
        directory=actual+f"/No_conditions_plots/exp{exp_id}/epoch{ne[e]}"
        print(directory)
        try:
            os.makedirs(directory)
        except OSError:
            print("The directory creation %s fail" % directory)
        else:
            print("The directory has been created: %s " % directory)
    
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        dist,bins=fn.getSampleDistribution(lfp[ch][:,epochs[e]].flatten())
        ax.plot(bins[1:],dist)
        ax.set_title(f'Probability distribution of the electrode{ch}\n during_{ne[e]}_epoch\n Exp id_{exp_id} \n without conditions')
        ax.set_xlabel('uV')
        ax.set_ylabel('Probability')
        fsave=(f"No_conditions_plots/exp{exp_id}/epoch{ne[e]}/SingleCh_No_conditions_epoch{ne[e]}_{ch}.svg")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')
        
