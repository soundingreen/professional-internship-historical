##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
##Library for working with folders
import os
## Custom functions
import m24_functions as fn
##################################################
#the experiment i want to visualize
exp=0
##################################################
#WTF
### Array for of times
times=np.arange(-2.001, 8, 0.001)
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
for ch in electrodes[1]:
    directory=actual+f"/Raw_plots/exp{exp_id}/{ch}"
    print(directory)
    try:
        os.makedirs(directory)
    except OSError:
        print("The directory creation %s fail" % directory)
    else:
        print("The directory has been created: %s " % directory)
    
    for trial in range(lfp[ch].shape[0]):
        if info[trial][2]:
            outcome_color="#688eac" # hits are blue
        else:
            outcome_color="#B54518" # misses are orange
                
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        ax.plot(times,lfp[ch][trial],color=outcome_color,alpha=0.7)
        ax.set_xlim(times[0],times[-1])
        fn.events(ax)
        ax.set_xlabel("Time[s]",fontsize=14)
        ax.set_ylabel("Voltage [uV]",fontsize=14)
        ax.set_title(f'Exp id {exp_id} \n Ensayo {trial+1:03} \n Electrodo {ch}')
        ax.legend(fontsize="medium",shadow=True,fancybox=True)
        fsave=(f"Raw_plots/exp{exp_id}/{ch}/SingleTrialLFP_exp-{exp_id}_trial-{trial+1:03}_{ch}.svg")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')

