# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:27:28 2021

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
#

#####################################
#creating plots
actual="D:/m24_load_javier/alternatives"
s_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']
for a in s_areas:
    moments=['MEAN','STD','KUR','SK']
    mom={'KUR':'Excess Kurtosis','STD':'Standard Deviation','MEAN':'Mean','SK':'Skewness'}
    
    ################3 epochs of conditions by moment 
    for m in moments:
        #######################################################
        ##c1
        directory1=actual+f"/Data/{a}_Conditions_Dist/c1/{m}"
        x_c1=fn.getFilelist(directory1,prefixo=f'{m}_exp*.npy')
        nx=len(x_c1)
        #########c1
        data_wait_c1=[]
        data_delay1_c1=[]
        data_delay2_c1=[]
        for i in range(nx):
            exp=np.load(x_c1[i])
            data_wait_c1.append(exp[0])
            data_delay1_c1.append(exp[1])
            data_delay2_c1.append(exp[2])  
        data_wait_c1=np.concatenate(data_wait_c1)
        data_delay1_c1=np.concatenate(data_delay1_c1)
        data_delay2_c1=np.concatenate(data_delay2_c1)
        #####################################################
        ##c2
        directory2=actual+f"/Data/{a}_Conditions_Dist/c2/{m}"
        x_c2=fn.getFilelist(directory2,prefixo=f'{m}_exp*.npy')
        nx=len(x_c2)
        #########c2
        data_wait_c2=[]
        data_delay1_c2=[]
        data_delay2_c2=[]
        for i in range(nx):
            exp=np.load(x_c2[i])
            data_wait_c2.append(exp[0])
            data_delay1_c2.append(exp[1])
            data_delay2_c2.append(exp[2])  
        data_wait_c2=np.concatenate(data_wait_c2)
        data_delay1_c2=np.concatenate(data_delay1_c2)
        data_delay2_c2=np.concatenate(data_delay2_c2)
        #######################################################
        ##c3
        directory3=actual+f"/Data/{a}_Conditions_Dist/c3/{m}"
        x_c3=fn.getFilelist(directory3,prefixo=f'{m}_exp*.npy')
        nx=len(x_c3)
        #########c3
        data_wait_c3=[]
        data_delay1_c3=[]
        data_delay2_c3=[]
        for i in range(nx):
            exp=np.load(x_c3[i])
            data_wait_c3.append(exp[0])
            data_delay1_c3.append(exp[1])
            data_delay2_c3.append(exp[2])  
        data_wait_c3=np.concatenate(data_wait_c3)
        data_delay1_c3=np.concatenate(data_delay1_c3)
        data_delay2_c3=np.concatenate(data_delay2_c3)
        ########################################################
        ##c4
        directory4=actual+f"/Data/{a}_Conditions_Dist/c4/{m}"
        x_c4=fn.getFilelist(directory4,prefixo=f'{m}_exp*.npy')
        nx=len(x_c4)
        #########c4
        data_wait_c4=[]
        data_delay1_c4=[]
        data_delay2_c4=[]
        for i in range(nx):
            exp=np.load(x_c4[i])
            data_wait_c4.append(exp[0])
            data_delay1_c4.append(exp[1])
            data_delay2_c4.append(exp[2])  
        data_wait_c4=np.concatenate(data_wait_c4)
        data_delay1_c4=np.concatenate(data_delay1_c4)
        data_delay2_c4=np.concatenate(data_delay2_c4)
        #########################################################
        
        #Plotting
        
        ###############Wait
        directory=actual+f"/plots/ByEpoch/{a}_conditions_Allexp/{m}"
        print(directory)
        try:
            os.makedirs(directory)
        except OSError:
            print("The directory creation %s fail" % directory)
        else:
            print("The directory has been created: %s " % directory)
            
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        samples=(data_wait_c1,data_wait_c2,data_wait_c3,data_wait_c4)
        dists,bins=fn.getSamplesDistributions(samples)
        dist1,dist2,dist3,dist4=dists
        #ax.set_yscale('log')
        ax.plot(bins[1:],dist1, label='c1',color='blue',alpha=0.7)
        ax.plot(bins[1:],dist2,label='c2',color='red',alpha=0.7)
        ax.plot(bins[1:],dist3,label='c3',color='green',alpha=0.7)
        ax.plot(bins[1:],dist4,label='c4',color='orange',alpha=0.7)
        ax.set_title(f'Probability distribution of {mom[m]} in {a}\n during Wait \n All exp \n All_conditions')
        ax.legend()
        ax.set_xlabel('units')
        ax.set_ylabel('Probability')
        fsave=(f"D:/m24_load_javier/alternatives/plots/ByEpoch/{a}_conditions_Allexp/{m}/Wait_{m}_{a}_conditions_byEpoch_ALlconditions.png")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')
        
        ##############Delay1
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        samples=(data_delay1_c1,data_delay1_c2,data_delay1_c3,data_delay1_c4)
        dists,bins=fn.getSamplesDistributions(samples)
        dist1,dist2,dist3,dist4=dists
        #ax.set_yscale('log')
        ax.plot(bins[1:],dist1, label='c1',color='blue',alpha=0.7)
        ax.plot(bins[1:],dist2,label='c2',color='red',alpha=0.7)
        ax.plot(bins[1:],dist3,label='c3',color='green',alpha=0.7)
        ax.plot(bins[1:],dist4,label='c4',color='orange',alpha=0.7)
        ax.set_title(f'Probability distribution of {mom[m]} in {a}\n during Delay 2 sec 1 \n All exp \n All_conditions')
        ax.legend()
        ax.set_xlabel('units')
        ax.set_ylabel('Probability')
        fsave=(f"D:/m24_load_javier/alternatives/plots/ByEpoch/{a}_conditions_Allexp/{m}/Delay1_{m}_{a}_conditions_byEpoch_ALlconditions.png")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')
       
        #########Delay2
        fig = plt.figure(figsize=(11,6))
        ax=fig.add_subplot(1,1,1)
        samples=(data_delay2_c1,data_delay2_c2,data_delay2_c3,data_delay2_c4)
        dists,bins=fn.getSamplesDistributions(samples)
        dist1,dist2,dist3,dist4=dists
        #ax.set_yscale('log')
        ax.plot(bins[1:],dist1, label='c1',color='blue',alpha=0.7)
        ax.plot(bins[1:],dist2,label='c2',color='red',alpha=0.7)
        ax.plot(bins[1:],dist3,label='c3',color='green',alpha=0.7)
        ax.plot(bins[1:],dist4,label='c4',color='orange',alpha=0.7)
        ax.set_title(f'Probability distribution of {mom[m]} in {a}\n during Delay 2 sec 3 \n All exp \n All_conditions')
        ax.legend()
        ax.set_xlabel('units')
        ax.set_ylabel('Probability')
        fsave=(f"D:/m24_load_javier/alternatives/plots/ByEpoch/{a}_conditions_Allexp/{m}/Delay2_{m}_{a}_conditions_byEpoch_ALlconditions.png")
        fig.savefig(fsave)
        print(fsave)
        plt.close('all')
       