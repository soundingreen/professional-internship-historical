##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
######
import os
##################################################
exp=0
#elc='S1-E2'
##################################################
#WTF
### Array for of times
wait,delay1,delay2,times=fn.times(epochs='yes')
epochs=(wait,delay1,delay2)
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
directory=actual+f"/Raw_Mean_plots/exp{exp_id}/"
print(directory)
try:
    os.makedirs(directory)
except OSError:
    print("The directory creation %s fail" % directory)
else:
    print("The directory has been created: %s " % directory)

All_means=[]
for ch in electrodes[1]:
    m=np.mean(lfp[ch],axis=0)
    All_means.append(m)
    s=np.std(lfp[ch],axis=0)    
    fig = plt.figure(figsize=(11,6))
    ax=fig.add_subplot(1,1,1)
    ax.plot(times,m,color='red',alpha=0.7)
    ax.set_xlim(times[0],times[-1])
    fn.events(ax)
    ax.fill_between(times,m-s,m+s,color='blue',label='f1',alpha=0.09)
    ax.set_xlabel("Time[s]",fontsize=14)
    ax.set_ylabel("Voltage [uV]",fontsize=14)
    ax.set_title(f'Promedio del  electrodo {ch}\n Exp {exp+1} ')
    fsave=(f"Raw_Mean_plots/exp{exp_id}/Raw_mean_LFP_exp-{exp_id}_{ch}.svg")
    fig.savefig(fsave)
    print(fsave)
    plt.close('all')
    #####################
All_m=np.vstack(All_means)
print(All_m.shape)
m=np.mean(All_m,axis=0)
print(m.shape)
s=np.std(All_m,axis=0)    
fig = plt.figure(figsize=(11,6))
ax=fig.add_subplot(1,1,1)
ax.plot(times,m,color='red',alpha=0.7)
ax.set_xlim(times[0],times[-1])
fn.events(ax)
ax.fill_between(times,m-s,m+s,color='blue',label='f1',alpha=0.09)
ax.set_xlabel("Time[s]",fontsize=14)
ax.set_ylabel("Voltage [uV]",fontsize=14)
ax.set_title(f'Promedio de todos los electrodos \n Exp {exp+1} ')
fsave=(f"Raw_Mean_plots/exp{exp_id}/All_ch_Raw_mean_LFP_exp-{exp_id}.svg")
fig.savefig(fsave)
print(fsave)
plt.close('all')

    
