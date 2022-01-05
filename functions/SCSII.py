# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 03:40:46 2021

@author: M ElGhorab
"""
def SCSII(depth,durn):
    '''
    this function requires the storm depth and the duration and returns
    the storm hydrograph according to SCS type II distributions
    '''
# =============================================================================
#         Reading the Distributions File
# =============================================================================
    import pandas as pd
    import numpy as np
    SCS = pd.read_csv(r'functions\SCSII_dist.csv')
    cum = depth * SCS[durn]             # calculating cumulative depths
    cum = cum.dropna()                  # remove nan from pandas dataframe
    # creating incremental hyetograph
    hyt = np.zeros((len(cum),2))
    temp = cum.to_numpy()
    hyt[0,1] = temp[0]
    hyt[0,0] = 0.1
    for i in range(1,len(temp),1):
        hyt[i][0] = hyt[i-1][0]+0.1
        hyt[i][1] = temp[i] - temp[i-1]
   
    return hyt
    