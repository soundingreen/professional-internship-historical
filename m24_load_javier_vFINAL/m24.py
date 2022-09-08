#####################################################################
# Author: Jeronimo Zizumbo Colunga 
# Date: October 25, 2021
#####################################################################
import glob
import numpy as np
import m24_aux as aux
from scipy.io import loadmat
#####################################################################
# this module contains the following functions: 
#####################################################################
# MUCH NEEDED VARIABLES
BAD_ELECTRODES = aux.get_badElectrodes()
AREAS = ['THA','S1','S2','VPC','DPC','MPC','M1']
TASKS = ('activa','luces')
FREQUENCY_RANGE = [10,14,16,18,20,22,24,26,28,30,34]
#####################################################################
# THE JOY OF FUNCTIONS

def getSessionID(f,task='activa'):
    """
    Get the integer identification number from the path of one of Saskia's MATLAB data file. 
    """
    x = f.split('/')[-1].split('_')[-1][3:-4]
    if '-' in x and task=='luces':
        x = x.split('-')[0]
    return int(x)

def getFilelist(path,task='activa'):
    """
    Get a sorted list of full paths to Saskia-style named MAT files in a directory. 
    """
    x = glob.glob(path+'/data_m24_exp*.mat')
    x = sorted(x,key=lambda f: getSessionID(f,task))
    return x

def loadSaskia(path):
    with open(path,'rb') as of:
        data = loadmat(of)
    assert all(data['data']['label'][0][0][-2:][:,0]==('trig','events'))
    electrodes = [None,None,None]
    electrodes[1] = tuple(x[0][0] for x in data['data']['label'][0][0] if '-E' in x[0][0])
    electrodes[2] = tuple(int(x.split('-')[-1][1:]) for x in electrodes[1])
    electrodes[0] = len(electrodes[1])
    ntrials = data['data']['trial'][0][0][0].shape[0]
    # list to skip trials with weird lengths
    skips = []
    for i in range(ntrials):
        if data['data']['time'][0][0][0][i][0].shape[0]<10001:
            skips.append(i)
    time = data['data']['time'][0][0][0][0][0]
    tt = [x for x in range(ntrials) if x not in skips]
    if 'trialinfo' in data['data'].dtype.fields:
        info = data['data']['trialinfo'][0][0][tt][:,[0,1,2,5]]
    else:
        info = data['data']['cfg'][0][0][0]['trl'][0][tt][:,[3,4,5,8]] 
    return data['data']['trial'][0][0][0], electrodes, tt, info

def getElectrode(electrode,data,trials):
    ntrials = len(trials)
    lfp = np.empty( (ntrials,10001) )
    for t,i in zip(trials,range(ntrials)):
        lfp[i] = data[t][electrode]
    return lfp
