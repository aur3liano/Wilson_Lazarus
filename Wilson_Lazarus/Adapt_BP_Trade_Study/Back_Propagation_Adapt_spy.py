# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:23:46 2019

@author: justin
"""

def Back_Prop_Adapt():
    #Import the random library
    import random
    #Import math library
    import math
    #Import time library
    import time
    #Import the MATLAB plotting library
    import matplotlib.pyplot as plt
    #Import the Python console library
    from IPython import get_ipython
    #Bring plots into their own window
    get_ipython().run_line_magic('matplotlib','qt')
    #Set Back Propagation convergence parameters
    A = 0.01
    B = 5
    #Configure iterations for convergence
    iters_crit = int(1/(2*A))
    mand_iters = B*iters_crit
    #Set the bias vector
    biases = [0.75]
    #Set the gain and gain adaptation
    gain = A*B
    gain_adapt = 1 - gain
    Gains = []
    #Set simulation tolerances and error initialization
    error_tol = A/B
    error_diff = 1
    for b in range(len(biases)):
        #Initialize time counter
        start_time = time.time()
        #Initialize the simulation
        y_a = 0.5
        y_sim = [y_a]
        iteration = 0
        Error_Diff = [error_diff]
        Gains = [Gains,gain]
        #Simulation calculations
        while (error_diff > error_tol):
            error_stat = 1
            sub_iter = 0
            while ((error_stat > error_tol) or (sub_iter < mand_iters)):
                #Obtain simulation result
                rand_flag = random.random()
                #Decide on adjustment
                if (rand_flag > biases[b]):
                    #Calculate loss adjustment
                    adj = -gain*(y_a)
                else:
                    #Calculate gain adjustment
                    adj = gain*(1-y_a)
                #Calculate new value
                y_1 = y_a + adj
                #Record the new value
                y_sim.append(y_1)
                #Increment simulation iteration
                iteration = iteration + 1
                #Increment simulation sub iterations
                sub_iter = sub_iter + 1
                #Calculate error difference
                error_diff = abs(y_1-y_a)
                #Record the simulation convergence metrics
                Error_Diff.append(error_diff)
                Gains.append(gain)
                #Decide on new average
                if (iteration < iters_crit):
                    #Calculate a global average
                    y_a = sum(y_sim)/(iteration+1)
                    #Calculate error average
                    err_a = sum(Error_Diff)/(iteration+1)
                    #Calculate error variance
                    err_var_sum = 0
                    for err in range(len(Error_Diff)):
                        err_var_sum = err_var_sum + ((Error_Diff[err] - err_a)**2)
                    #Calculate error standard deviation
                    err_stdev = math.sqrt(err_var_sum/iteration)
                    #Calculate statistical error in error difference
                    error_stat = (3.5*err_stdev)/iteration
                else:
                    #Calculate a moving average
                    y_a_sum = 0
                    for im in range((iteration-iters_crit),iteration):
                        y_a_sum = y_a_sum + y_sim[im]
                    y_a = (y_a_sum/iters_crit)
                    #Calculate error average
                    err_a_sum = 0
                    for em in range((iteration-iters_crit),iteration):
                        err_a_sum = err_a_sum + Error_Diff[em]
                    err_a = (err_a_sum/iters_crit)
                    #Calculate error variance
                    err_var_sum = 0
                    for err in range(len(Error_Diff)):
                        err_var_sum = err_var_sum + ((Error_Diff[err] - err_a)**2)
                    #Calculate error standard deviation
                    err_stdev = math.sqrt(err_var_sum/iteration)
                    #Calculate statistical error in error difference
                    error_stat = (2*err_stdev)/iteration
            #Attenuate the gain once error difference has converged
            gain = gain * gain_adapt
            print(error_diff)
        #End time
        end_time = time.time() - start_time
        #Build the iters vector
        iters = [0]*(iteration+1)
        for its in range(iteration+1):
            iters[its] = its
        #Open the simulation results file
        file = open("bias_"+str(biases[b])+".txt","w+")
        #Print the simulation results
        for ir in range(len(y_sim)):
            file.write(str(iters[ir]))
            file.write(" ")
            file.write(str(y_sim[ir]))
            file.write(" ")
            file.write(str(Error_Diff[ir]))
            file.write('\n')
        file.close()
        plt.scatter(iters,y_sim)
    return(y_sim)
    
Back_Prop_Adapt()