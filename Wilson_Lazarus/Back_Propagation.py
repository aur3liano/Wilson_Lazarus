#This program explores the concept of "back propagation"

def Back_Prop():
    #Import the random library
    import random
    #Set Back Propagation convergence parameters
    A = 0.005
    B = 3
    C = 10
    #Configure iterations for convergence
    final_iteration = 1001
    iters = [0]*final_iteration
    for i in range(final_iteration):
        iters[i] = i
    iters_crit = int(A*final_iteration)
    #Set the bias vector
    biases = [0.75]
    #Set the gain vector
    gains = [0.01,0.02,0.03]
    for b in range(len(biases)):
        for g in range(len(gains)):
            #Initialize the simulation
            y_a = 0.5
            y_sim = [0]*final_iteration
            y_sim[0] = y_a
            #Simulation calculations
            for s in range(1,final_iteration):
                #Obtain simulation result
                rand_flag = random.random()
                #Decide on adjustment
                if (rand_flag < biases[b]):
                    #Calculate loss adjustment
                    adj = -gains[g]*(y_a)
                else:
                    #Calculate gain adjustment
                    adj = gains[g]*(1-y_a)
                #Calculate new value
                y_1 = y_a + adj
                #Record the new value
                y_sim[s] = y_1
                #Decide on new average
                if (s < iters_crit):
                    #Calculate a global average
                    y_a = sum(y_sim)/(s+1)
                else:
                    #Calculate a moving average
                    y_a_sum = 0
                    for sm in range((s-iters_crit),s):
                        y_a_sum = y_a_sum + y_sim[sm]
                    y_a = (y_a_sum/iters_crit)
            #Open the simulation results file
            file = open("bias_"+str(biases[b])+"_gain_"+str(gains[g])+".txt","w+")
            #Print the simulation results
            for sr in range(len(y_sim)):
                file.write(str(iters[sr]))
                file.write(" ")
                file.write(str(y_sim[sr]))
                file.write('\n')
            file.close()
    return(y_sim)

Back_Prop()
