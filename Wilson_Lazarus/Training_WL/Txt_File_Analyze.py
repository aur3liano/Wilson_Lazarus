# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:38:56 2019

This script loads a text file with numpy and plots the contents

@author: justin
"""

def Analyze():
    #Import numpy as np
    import numpy as np
    #Import the MATLAB plotting library
    import matplotlib.pyplot as plt
    #Import the Python console library
    from IPython import get_ipython
    #Bring plots into their own window
    get_ipython().run_line_magic('matplotlib','qt')
    #Create player file name and figure names
    ply_file_nm = 'WL_config.txt'
    img_nm = 'Fixed_Training.png'
    #Load text file for analysis
    data = np.loadtxt(ply_file_nm,dtype = float)
    #Create an iters vector to plot against and normalize the priority coefficients
    iters = []
    pcs_norm = []
    for i in range(len(data[:,0])):
        iters.append(i+1)
        #Sum the pcs
        pc_sum = 0
        for pcs in range(12):
            pc_sum = pc_sum + data[i,pcs]
        #Calculate new pcs
        new_pcs = []
        for pcs in range(12):
            new_pcs.append(data[i,pcs]/pc_sum)
        #Append new pcs
        pcs_norm.append(new_pcs)
    #Plot the rock priority coefficient
    plt.figure(num=None, figsize=(16, 7.9), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(iters,R_PC_norm,linewidth = 1.5)
    plt.plot(iters,P_PC_norm,linewidth = 1.5)
    plt.plot(iters,S_PC_norm,linewidth = 1.5)
    plt.axis([0,100000,0,1.0])
    plt.xlabel('Games')
    plt.ylabel('PC')
    plt.title('NEL_Apathetic_Ties')
    plt.savefig(img_nm)
    return(1)

Analyze()
