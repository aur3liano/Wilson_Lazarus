def Back_Prop_Adapt():
    #Import the random library
    import random
    #Import math library
    import math
    #Import time library
    import time
    '''
    #Import the MATLAB plotting library
    import matplotlib.pyplot as plt
    #Import the Python console library
    from IPython import get_ipython
    #Bring plots into their own window
    get_ipython().run_line_magic('matplotlib', 'qt')
    '''
    #Set the bias vector
    biases = [0,0.1,0.3,0.7,0.9,1]
    #Establish the Back Propagation convergence parameter vectors
    A_vect = [0.05,0.025,0.01]
    B_vect = [3,5,7]
    C_ic_vect = [(1/3),0.5,1]
    C_et_vect = [1,0.5,(1/3)]
    Times = []
    for bi in range(len(biases)):
        for a in range(len(A_vect)):
            for b in range(len(B_vect)):
                for cic in range(len(C_ic_vect)):
                    for cet in range(len(C_et_vect)):
                        #Iterate through each convergence parameter vector
                        A = A_vect[a]
                        B = B_vect[b]
                        C_ic = C_ic_vect[cic]
                        C_et = C_et_vect[cet]
                        #Configure iterations for convergence
                        iters_crit = int(round((C_ic*(1/A)),0))
                        mand_iters = B*iters_crit
                        #Configure the gain and gain adaptation 
                        gain = A*B
                        gain_adapt = 1-gain
                        Gains = []
                        #Set simulation tolerances and error initialization
                        error_tol = C_et*(A/B)
                        #Start timer
                        start_time = time.time()
                        #Initialize the simulation
                        y_a = 0.5
                        y_sim = [y_a]
                        iteration = 0
                        error_diff = 1
                        error_diff_min = 1
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
                                if (rand_flag > biases[bi]):
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
                                #Compare error difference values to test minimum error difference
                                if (error_diff < error_diff_min):
                                    error_diff_min = error_diff
                                    #Print each successive error_diff_min
                                    print(error_diff_min)
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
                            #Attenuate the gain once error difference has converged for the current adaption level
                            gain = gain * gain_adapt
                            Gains.append(gain)
                        #Print final report
                        print()
                        print('Value Achieved:')
                        print(round(y_a,3))
                        print('Absolute Error:')
                        abs_err = round((y_a - biases[bi]),5) 
                        print(abs_err)
                        '''
                        print('Error Percentage:')
                        err_per = round(((y_a - biases[bi])/biases[bi])*100,3)
                        err_per = str(err_per)+'%'
                        print(err_per)
                        '''
                        print('Time Elapsed:')
                        time_elpsd = round((time.time() - start_time)/60,3)
                        Times.append(time_elpsd)
                        time_elpsd = str(time_elpsd) + ' ' + 'mins'
                        print(time_elpsd)
                        print('Total Iterations:')
                        print(iteration)
                        print('Total adaptations:')
                        print(len(Gains))
                        print('Final Gain:')
                        fin_gain = round(Gains[len(Gains)-1],6)
                        print(fin_gain)
                        print()
                        #Concatenate report vector
                        report_vect = [round(y_a,3),abs_err,iteration,len(Gains),fin_gain,Times[len(Times)-1]]
                        '''
                        #Build the iters vector
                        iters = [0]*(iteration+1)
                        for its in range(iteration+1):
                            iters[its] = its
                        #Open the simulation results file
                        file = open("bias_"+str(biases[bi])+".txt","w+")
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
                        '''
                        #Open the trade study results file
                        file = open("bias_"+str(biases[bi])+".txt","a+")
                        #Print the trade study results
                        for ts in range(len(report_vect)):
                            file.write(str(report_vect[ts])),
                            file.write(" ")
                        file.write('\n')
                        file.close()
    return(y_a)
    
Back_Prop_Adapt()
