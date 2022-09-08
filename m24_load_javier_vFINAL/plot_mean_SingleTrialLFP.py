##Library for loading data
import m24
##Basic libraries for plotting and working with arrays
import matplotlib.pyplot as plt
import numpy as np
######Custom functions
import m24_functions as fn
##################################################
exp=0
elc='S1-E1'
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
m=np.mean(lfp[elc],axis=0)
s=np.std(lfp[elc],axis=0)

fig = plt.figure(figsize=(11,6))
ax=fig.add_subplot(1,1,1)
ax.plot(times,m,color='black',alpha=0.7,label='Mean all trials')
ax.plot(times,lfp[elc][0],color='orange',alpha=0.5,label='trial1')
ax.plot(times,lfp[elc][10],color='blue',alpha=0.5,label='trial 11')
ax.plot(times,lfp[elc][15],color='red',alpha=0.5,label='trial 16')
fn.events(ax)
ax.fill_between(times,m-s,m+s,color='blue',label='f1',alpha=0.09)
ax.set_xlabel("Time[s]",fontsize=14)
ax.set_ylabel("Voltage [uV]",fontsize=14)
ax.set_title(f'Promedio del  electrodo {elc}\n Exp {exp+1} ')