##Library for loading data
import m24
##Basic library for working with arrays
import numpy as np
##Library for working with folders
import os
##Custom functions
import m24_functions as fn
###  Standard deviation, skewness and kurtosis
from numpy import std
from scipy.stats import skew
from scipy.stats import kurtosis
###for calculating non parametric PDF
from sklearn.neighbors import KernelDensity

##################################################
exp=0
elc='S1-E1'
###################################################
wait,delay1,delay2,times=fn.times(epochs='yes')
epochs=(wait,delay1,delay2)
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
######################################################
epochs_list=[]
for epoch in epochs:
    lfp_dict=dict()
    for ch in electrodes[1]:
        c1=np.vstack(lfp[ch][0])[:,epoch]
        c2=np.vstack(lfp[ch][1])[:,epoch]
        c3=np.vstack(lfp[ch][2])[:,epoch]
        c4=np.vstack(lfp[ch][3])[:,epoch]
        dist,bins=fn.getTrialDistributions([c1,c2,c3,c4])
        lfp_dict[ch]=[dist,bins]
    epochs_list.append(lfp_dict)
wait_dist=epochs_list[0]
delay1_dist=epochs_list[1]
delay2_dist=epochs_list[2]


print(wait_dist)
distc1,distc2,distc3,distc4=wait_dist[elc][0]
bins=wait_dist[elc][1]

import matplotlib.pyplot as plt
plt.hist(bins[:-1],bins,weights=distc4)
    




def getTrialDistributions(samples,nbins=100):
    """
    This function creates probability distributions for every trial using the respective numerical sample.
    Input parameters:
    samples= It must be a list of ndarrays with shape NxT
    nbins=number of bins that will have the distributions
    """
    # minimum of distributions minimums
    mi=min([s.min() for s in samples])
    # maximum of distributions maximums
    mx=max([s.min() for s in samples])
    # linspace between mi and mx, it has the number of bins especified on the parameters, default nbins=100
    bins=np.linspace(mi,mx,nbins) 
    dist=[]
    for s in samples:
        n=len(s[0])# number of time points in a trial
        d=np.apply_along_axis(np.histogram,1,s,bins=bins)[:,0]/n
        #x=s.shape[0]
        #y=s.shape[1]
        #n=x*y
        #d=np.histogram(s.flatten(),bins=bins)[0]/n
        dist.append(d)
    return dist,bins





def getDistributions(sample1,sample2,nbins=100):
    """
    This function creates 2 probability distributions using the respective numerical sample.
    Input parameters:
    sample1=
    nbins=number of bins that will have the distributions
    """
    mi=np.min((sample1.min(),sample2.min()))# el mínimo de mínimos de las dos distribuciones redondeado hacia abajo # [0] el mínimo de la distribución 1 y [1] el mínimo de las distribución 2
    mx=np.max((sample1.max(),sample2.max()))# el máximo de máximos de las dos distribuciones redondeado hacia arriba # [0] el Máximo de la distribución 1 y [1] el Máximo de la distribución 2
    bins=np.linspace(mi,mx,nbins) # genero un linspace entre el minimo de minimos y el maximo de maximos, y este linspace va a tener el número de bines que yo indique en nbins 
    n1=len(sample1)# n de elementos sample 1
    n2=len(sample2)# n de elementos sample 2
    dist1=np.histogram(sample1,bins=bins)[0]/n1 #probabilidades de los bines de la muestra 1
    dist2=np.histogram(sample2,bins=bins)[0]/n2#probabilidades de los bines de la muestra 2
    return dist1,dist2,bins



def getTrialPDF(samples,values=1000):
    # minimum of distributions minimums
    mi=min([s.min() for s in samples])
    # maximum of distributions maximums
    mx=max([s.min() for s in samples])
    pdf=[]
    for s in samples:
        #fit density
        model=KernelDensity(bandwidth=3,kernel='gaussian')
        s=s.flatten()
        model.fit(s)
        values=np.asarray([value for value in range(mi,mx)])
        values=values.reshape((len(values),1))
        probabilities=model.score_samples(values)
        probabilities=np.exp(probabilities)
        pdf.append(probabilities)
    return pdf,values




def cDist_dict(lfp,epochs,electrodes):
    epochs_list=[]
    for epoch in epochs:
        lfp_dict=dict()
        for ch in electrodes[1]:
            c1=np.vstack(lfp[ch][0])[:,epoch]
            c2=np.vstack(lfp[ch][1])[:,epoch]
            c3=np.vstack(lfp[ch][2])[:,epoch]
            c4=np.vstack(lfp[ch][3])[:,epoch]
            dist,bins=fn.getTrialDistributions([c1,c2,c3,c4])
            lfp_dict[ch]=[dist,bins]
        epochs_list.append(lfp_dict)
    wait_dist=epochs_list[0]
    delay1_dist=epochs_list[1]
    delay2_dist=epochs_list[2]
    return wait_dist,delay1_dist,delay2_dist

##########################calculate conditions 

lfp=fn.elc_dict(data,electrodes,trials)
c1,c2,c3,c4=fn.i_conditions(info)
print(type(c1))
print(c1.shape)
print(c1)

ep=delay1
idx = electrodes[1].index(elc)
x = m24.getElectrode(idx,data,trials)
print(x[c1,:].shape)
print(x[c2,:].shape)
print(x[c3,:].shape)
print(x[c4,:].shape)
####################################
print(x[c1,:][:,ep].shape)
print(x[c2,:][:,ep].shape)
print(x[c3,:][:,ep].shape)
print(x[c4,:][:,ep].shape)

s1=x[c1,:][:,ep]
s2=x[c2,:][:,ep]
s3=x[c3,:][:,ep]
s4=x[c4,:][:,ep]
samples=(s1,s2,s3,s4)
dist,bins=fn.getConditionsDistributions(samples)
dc1,dc2,dc3,dc4=dist
#mi=np.min(sample)
#mx=np.max(sample)
#print(mi,mx)
#bins=np.linspace(mi,mx,100)
#d=np.histogram(sample.flatten(),bins=bins)[0]
#d=d/d.sum()


fig = plt.figure(figsize=(11,6))
ax=fig.add_subplot(1,1,1)
ax.plot(bins[1:],dc1,label='c1')


########################
def extract_areas(electrodes):    
    e=list(electrodes[1])
    ne=len(e)
    Ael=[]
    for i in range(ne): 
        Ael.append(e[i][0:3])
    areas=np.unique(Ael)
    ar=dict()
    for sub in areas:
        el = [i for i in e if sub  in i]
        ar.update({sub:el})
    return ar