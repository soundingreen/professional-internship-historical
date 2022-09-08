import numpy as np
import m24
###  Skewness and kurtosis
from scipy.stats import skew
from scipy.stats import kurtosis
##
import glob
####THE JOY OF FUNCTIONS


###########################Distributions

def getSampleDistribution(sample,nbins=100):
    mi=np.min(sample)
    mx=np.max(sample)
    # linspace between mi and mx, it has the number of bins especified on the parameters, default nbins=100
    bins=np.linspace(mi,mx,nbins) 
    d=np.histogram(sample.flatten(),bins=bins)[0]
    d1=d/d.sum()
    print(d1.sum())
    return d1,bins

def getSamplesDistributions(samples,nbins=100):
    """
    This function creates a probability distributions for a list of samples or condition 
    Input parameters:
    samples= It must be a list of ndarrays with shape NxT, every array corresponding to a condition
    nbins=number of bins that will have the distributions
    """
    # minimum of distributions minimums
    mi=min([s.min() for s in samples])
   
    print(mi)
    # maximum of distributions maximums
    mx=max([s.max() for s in samples])
    print(mx)
    # linspace between mi and mx, it has the number of bins especified on the parameters, default nbins=100
    bins=np.linspace(mi,mx,nbins) 
    cdist=[]
    for sample in samples:
        d=np.histogram(sample.flatten(),bins=bins)[0]
        d=d/d.sum()
        cdist.append(d)
    return cdist,bins
###############################Moments
def getMomentsSamples(samples,moment='std'):
    """
    This function creates probability distributions for every trial std using the respective numerical sample.
    Input parameters:
    samples= It must be a list of ndarrays with shape NxT
    nbins=number of bins that will have the distributions
    """
    if moment=='std':
        samplesback=[]
        for s in samples:
            st=np.apply_along_axis(np.std,1,s).flatten()
            samplesback.append(st)
        return samplesback
    
    elif moment=='sk':
        samplesback=[]
        for s in samples:
            skw=np.apply_along_axis(skew,1,s).flatten()
            samplesback.append(skw)
        return samplesback
    elif moment=='kr':
        samplesback=[]
        for s in samples:
            kur=np.apply_along_axis(kurtosis,1,s).flatten()
            samplesback.append(kur)
        return samplesback
    


############################Data management
def elc_dict(data,electrodes,trials):
    """
    Parameters
    ----------
    data :
    trials : 
    electrodes : 
        
    Returns
    -------
    lfp : dictionary of electrodes (key) 
    with all the trials of the electrode (items)
    """
    # loading every electrode data in a dictionary
    lfp=dict() # empty dictionary 
    for ch in electrodes[1]: # loop for every chanel/electrode in this file
        idx = electrodes[1].index(ch) #index of the electrode in the list of names of the electrodes in this exp
        x = m24.getElectrode(idx,data,trials)# data of the particular electrode
        lfp[ch]=(x)#assign every electrode to his trials
    return lfp

def i_conditions(info):
    """
    Given the info of an experiment this function calculates the indexes
    of 4 conditions
    Parameters
    ----------
    info : TYPE
        DESCRIPTION.

    Returns
    -------
    c1 : condition 1 f1 higher than f2 and hit
    c2 : condition 2 f1 higher than f2 and miss
    c3 : condition 3 f2 higher than f1 and hit
    c4 : condition 4 f2 higher than f1 and miss
    """
    mf1=np.nonzero(info[:,0]>info[:,1])
    mf2=np.nonzero(info[:,0]<info[:,1])
    hits=np.nonzero(info[:,2]==1)
    misses=np.nonzero(info[:,2]==0)
    #####################################
    c1=np.intersect1d(mf1,hits)
    c2=np.intersect1d(mf1,misses)
    c3=np.intersect1d(mf2,hits)
    c4=np.intersect1d(mf2,misses)
    return c1,c2,c3,c4

def conditions_dict(data,electrodes,trials,info):
    """
    This function calculates a dictionary of  
    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    electrodes : TYPE
        DESCRIPTION.
    trials : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    ##calculing index of the conditions
    c1,c2,c3,c4=i_conditions(info)
    #conditions by electrode
    lfp=dict()
    for ch in electrodes[1]:
        idx = electrodes[1].index(ch)
        x = m24.getElectrode(idx,data,trials)
        lfp[ch]=(x[c1,:],x[c2,:],x[c3,:],x[c4,:])
    return lfp


def extract_areas(electrodes,s_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']): 
    e=list(electrodes[1])
    a_in_electrode=dict()
    for sub in s_areas:
        el = [i for i in e if sub  in i]
        if len(el)>0:
            a_in_electrode.update({sub:el})
    return a_in_electrode
            

def extract_trials_areas(lfp,electrodes,s_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']):
    elc_areas=extract_areas(electrodes,s_areas)
    areas=list(elc_areas.keys())
    lfp_areas=dict()
    for area in areas:
        a=[]
        for ch in elc_areas[area]:
            a.append(lfp[ch])
        a=np.vstack(a)
        lfp_areas.update({area:a})
    return lfp_areas

def extract_tr_ar_conditions(lfp,electrodes,condition,s_areas=['S1','S2','MPC-left','MPC-right','VPC','M1','DPC']):
    elc_areas=extract_areas(electrodes,s_areas)
    areas=list(elc_areas.keys())
    lfp_areas_cond=dict()
    for area in areas:
        ac=[]
        for ch in elc_areas[area]:
            ac.append(lfp[ch][condition,:])
        ac=np.vstack(ac)
        lfp_areas_cond.update({area:ac})
    return lfp_areas_cond

#############################Plotting
def events(axis):
    """
    Inspired by Jeronimo's code.
    This function plots task events on the given axis.
    The x-axis is the time in seconds
    Because of the set ylim it must be use after plotting everything else
    Parameters
    ----------
    axis :
        
    Returns
    -------
    None.

    """
    #define limits
    ylim=axis.get_ylim()
    #fix limits
    axis.set_ylim(*ylim)
    #stimulation periods
    axis.fill_between([0.000,0.520],*ylim,color='#d6d6d6',label='f1')
    axis.fill_between([3.500,4.020],*ylim,color='#d6d6d6',label='f1')
    #probe up
    axis.vlines([7.0],*ylim,color='grey',ls='--',label='PU')
    return None

def times(epochs='no'):
    """

    Parameters
    ----------
    epochs : TYPE, optional
        DESCRIPTION. The default is 'yes'.

    Returns
    -------
    None.

    """
    ### Array for of times
    times=np.arange(-2.001, 8, 0.001)
    
    if epochs=='no':
        return times
    else:
    #Index for every epoch of interest
    
    #indexes of pre-stimulus wait
        infp=np.nonzero(times<0)
        supp=np.nonzero(times>=-2)
        prestimulus=np.intersect1d(infp,supp)
        #index of interstimulus delay
        infd=np.nonzero(times>=0.5)
        supd=np.nonzero(times<=3.5)
        first_delay=np.intersect1d(infd,supd)
        #index of second delay
        inf2=np.nonzero(times>=4.5)
        sup2=np.nonzero(times<=6.5)
        second_delay=np.intersect1d(inf2,sup2)
        return prestimulus,first_delay,second_delay,times
    
    
#####Working with dictionaries
def merge_dicts(combiner, dicts):
    new_dict = {}
    for d in dicts:
       for k, v in d.items():
           if k in new_dict:
               new_dict[k] = combiner(new_dict[k], v)
           else:
               new_dict[k] = v
    return new_dict

#example
#x = {'a': 1, 'b': 2}
#y = {'b': 2, 'c': 3}
#new=merge_dicts(combiner= lambda x, y:np.vstack((x,y)) , dicts=(x,y))

### loading my data

def getFilelist(path,prefixo='SK_exp*.npy'):
    """
    Get a sorted list of full paths. 
    """
    x = glob.glob(path+'/'+prefixo)
    x=sorted(x)
    return x


