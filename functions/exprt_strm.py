# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 02:47:57 2021

@author: M ElGhorab
"""

def export_storm(DS,typ):
    import numpy as np
    np.savetxt('Outputs\{} Storm Hyetograph.txt'.format(typ), DS, delimiter=',')  
    