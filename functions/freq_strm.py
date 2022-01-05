# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:17:38 2021

@author: M ElGhorab
"""
def fr_strm(IDF,quart):
    #    '''
    #    This functions opens the IDF curve in a text/CSV file and reads it
    #    and uses the alternating blocks method to generate the design storm based 
    #    on the IDF values and total duration of the IDF
     #   '''
    # =============================================================================
    #     Reading the IDF file
    # =============================================================================
    import numpy as np
    with open(IDF,'r') as idf:
        file = idf.readlines()
        templist = []
        for i in range(len(file)):
            templist.append(file[i].split())
        idf = np.array(templist)                # storing the idf in an array
        (du,intn) = idf[:,0],idf[:,1]           # splitting the duration and intensity to separate arrays
        ### numpy string to float
        du = du.astype(float)
        intn = intn.astype(float)
    # =============================================================================
    #       Detecting the interval and rearranging if the interval is not regular
    # =============================================================================
        z = np.zeros((len(du)-2,1))
        for i in range(1,len(du)-2):
            z[i] = du[i] - du[i-1]
        for i in range(1,len(z)-1):
            if z[i]-z[i-1] != 0:
                du2 = np.arange(np.amin(du),np.amax(du)-du[1],du[1])
                from scipy.interpolate import CubicSpline as Cs
                intn2 = Cs(du,intn)(du2)
                intn2 = np.interp(du2,du,intn)
        if len(intn2) < len(intn):         # if the arrangement fails return to original
            du2 = du
            intn2 = intn        
    # =============================================================================
    #    Cumulative & incremental depth calculation
    # =============================================================================
        # the calculation is based on the assumption of the intensity being 
        # in mm/hr and the duration in minutes
        cd = du2*intn2/60                        # Cumulative Depth
        inc = np.zeros((len(cd),1))              # Incremental Depth
        inc[0]=cd[0]
        for i in range(1,len(cd)):
            inc[i] = cd[i]-cd[i-1] 
    # =============================================================================
    #       Alternating Blocks Calculator    
    # =============================================================================
    lox = {'25':4, '33':3, '50':2, '67':1.5, '75':1.333}   # location of the peak
    loc = int(len(du2)/lox[quart])
    hyt_AltBLX = np.zeros((len(cd),2))
    j = 0      
    while np.sum(hyt_AltBLX) < np.amax(cd) and j < len(inc):
        if j%2 == 0:
            ## checking if the array reached the beginning
            if(loc - int(j/2)-1) < 0:
                hyt_AltBLX[j:] = inc[j:]
                break
            ##############################################
            hyt_AltBLX[loc-int(j/2)-1,1] = inc[j]         # normal block arrangement towards begininng
        else:
            ## checking if the array reached the end
            if(loc+int(j/2)) > len(hyt_AltBLX)-1:
                incf = np.flip(inc)
                hyt_AltBLX[:len(hyt_AltBLX)-j] = incf[:len(hyt_AltBLX)-j]
                break
            ##############################################
            hyt_AltBLX[loc+int(j/2),1] = inc[j]           # normal block arrangement towards end
        j = j+1
    hyt_AltBLX[:,0]= du2
    return hyt_AltBLX