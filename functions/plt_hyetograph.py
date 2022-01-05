# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 01:50:42 2021

@author: M ElGhorab
"""

def hyt_plt(hyt,typ):
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(figsize=[25,12.5]) 
    if typ == 'Frequency':
        plt.bar(hyt[:,0],hyt[:,1],width = 7.5,edgecolor = 'k')
    else:
        plt.bar(hyt[:,0],hyt[:,1],width = 0.15,edgecolor = 'k')
    title_font = {'family':'serif', 'color':'darkblue', 'weight':'normal', 'size':35} # dictionary for title font
    plt.title('{} Storm Hyetograph'.format(typ),fontdict=title_font ,pad=(25))
    plt.grid()
    plt.xlabel('Time (mins)', size = 20)
    plt.xlim([0,np.amax(hyt[:,0])])
    plt.ylabel('Depth (mm)', size = 20)
    plt.tick_params(axis='both', which='major', labelsize=17.5)                # axis label size
    import os
    os.makedirs('Outputs', exist_ok = True)
    plt.savefig('Outputs\{} Storm Hyetograph.png'.format(typ))
    return fig