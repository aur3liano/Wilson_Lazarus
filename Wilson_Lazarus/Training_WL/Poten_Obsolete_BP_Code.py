'''
POTENTIALLY OBSOLETE BP CODE FOR WILSON LAZARUS
'''

#Back Propagation
def Back_Prop(PC_Value_History,PC_Error_History,gain,iteration,iters_crit,bet_net_gain):
    #Import math library
    import math
    #Calculate the average PC Value
    PC_avg = math.mean(PC_Value_History)
    #Decide which adjustment calculation should be made
    if (bet_net_gain < 100):
        adj = -gain*(PC_avg)
    elif (bet_net_gain > 100):
        adj = gain*(1-PC_avg)
    #Calculate new value
    PC_new = PC_avg + adj
    #Calculate the value error
    error_diff = abs(PC_new-PC_avg)
    #Choose the right appending protocol
    if (iteration < iters_crit):
        #Append new PC
        PC_Value_History.append(PC_new)
        #Calculate error_stat
        error_a = math.mean(PC_Error_History)
        err_var_sum = 0
        for pce in range(len(PC_Error_History)):
            err_var_sum = err_var_sum + ((PC_Error_History[pce]-error_a)^2)
        err_var = err_var_sum/(iteration)
        err_stdev = math.sqrt(err_var)
        error_stat = (3.5*err_stdev)/math.sqrt(iteration)
        #Append new PC error
        PC_Error_History.append(error_diff)
    else:
        #Remove the first PC value list element
        del PC_Value_History[0]
        #Append new PC
        PC_Value_History.append(PC_new)
        #Calculate error_stat
        error_a = math.mean(PC_Error_History)
        err_var_sum = 0
        for pce in range(len(PC_Error_History)):
            err_var_sum = err_var_sum + ((PC_Error_History[pce]-error_a)^2)
        err_var = err_var_sum/(iters_crit)
        err_stdev = math.sqrt(err_var)
        error_stat = (3.5*err_stdev)/math.sqrt(iters_crit)
        #Remove the first PC error list element
        del PC_Error_History[0]
        #Append new PC error
        PC_Error_History.append(error_diff)
    return(PC_Value_History,PC_Error_History,gain,error_diff,error_stat)

#Writing Configuration File
def Config_File_Write(Current_Master_PC_values,Current_Master_PC_gains,
                      Current_Master_PC_errors,Current_Master_PC_sub_iter,
                      Convergence_Vector,mand_iters,gain_adapt):
    #Open the configuration file for writing
    WL_prev_config_file = open("WL_prev_config.txt",'a')
    '''
    Write the Priority coefficients, gains, errors, sub iterations,
    convergence conditions, mandatory iterations and the gain adaptation value
    to the configuration file
    '''
    for MPCv in range(len(Current_Master_PC_values)):
        WL_prev_config_file.write((str(Current_Master_PC_values[MPCv])+"\t"),)
        WL_prev_config_file.write((str(Current_Master_PC_gains[MPCv])+"\t"),)
        WL_prev_config_file.write((str(Current_Master_PC_errors[MPCv])+"\t"),)
        WL_prev_config_file.write((str(Current_Master_PC_sub_iter[MPCv])+"\t"),)
        WL_prev_config_file.write((str(Convergence_Vector[MPCv])+"\t"),)
    WL_prev_config_file.write((str(mand_iters)+"\t"),)
    WL_prev_config_file.write((str(gain_adapt)+"\t"))
    #Write the next line
    WL_prev_config_file.write("\n")
    #Close the configuration file
    WL_prev_config_file.close()
    return(Current_Master_PC_values)
    
def Config_File_Read(Centi_Nodes,Deci_Nodes):
    #Open the configuration file for reading
    WL_prev_config_file = open("WL_config.txt",'r+')
    #Read the contents
    prev_config = WL_prev_config_file.readlines()
    #Convert list to string
    prev_config = prev_config[0]
    #Convert the string back to a list
    prev_config = prev_config.split("\t")
    #Remove the previous contents
    WL_prev_config_file.truncate(0)
    #Close the file
    WL_prev_config_file.close()
    #Initialize lists to build
    Current_Master_PC_values = [Centi_Nodes*[0],Deci_Nodes*[0]]
    Current_Master_PC_gains = [Centi_Nodes*[0],Deci_Nodes*[0]]
    Current_Master_PC_errors = [Centi_Nodes*[0],Deci_Nodes*[0]]
    Current_Master_PC_sub_iter = [Centi_Nodes*[0],Deci_Nodes*[0]]
    Convergence_Vector = [Centi_Nodes*[0],Deci_Nodes*[0]]
    #Cycle through all of the different expected lists
    for li in range(12):
        gains_index_start = (Centi_Nodes+Deci_Nodes)*1
        errors_index_start = (Centi_Nodes+Deci_Nodes)*2
        sub_iter_index_start = (Centi_Nodes+Deci_Nodes)*3
        conv_vect_index_start = (Centi_Nodes+Deci_Nodes)*4
        Current_Master_PC_values[li] = prev_config[li]
        Current_Master_PC_gains[li] = prev_config[li+gains_index_start]
        Current_Master_PC_errors[li] = prev_config[li+errors_index_start]
        Current_Master_PC_sub_iter[li] = prev_config[li+sub_iter_index_start]
        Convergence_Vector[li] = prev_config[li+conv_vect_index_start]
    MI_index_start = ((Centi_Nodes+Deci_Nodes)*4)+1
    GA_index_start = ((Centi_Nodes+Deci_Nodes)*4)+2
    mand_iters = prev_config[MI_index_start]
    gain_adapt = prev_config[GA_index_start]
    return(Current_Master_PC_values,Current_Master_PC_gains,
           Current_Master_PC_errors,Current_Master_PC_sub_iter,
           Convergence_Vector,mand_iters,gain_adapt)

#Convergence Training
def Convergence_Training(A,B,reward_vector):
    #Access Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Access Wilson Lazarus
    import Wilson_Lazarus_N1_D2_BP
    '''
    Calculate convergence parameters
    '''
    iters_crit = round((1/(2*A)),0)
    mand_iters = round((B*iters_crit),0)
    gain = A*B
    gain_adapt = 1-gain
    error_diff = 1
    error_tol = A/(3*B)
    starting_PC = 0.5
    #Strategy Node count
    Centi_Nodes = 7
    Deci_Nodes = 5
    #Macro_Nodes = 1
    '''
    #Initialize back propagation lists and lists of lists
    PC_Value_Master_History = [Centi_Nodes*[starting_PC],Deci_Nodes*[starting_PC]]
    PC_Gain_Master_History = [Centi_Nodes*[gain],Deci_Nodes*[gain]]
    PC_Error_Master_History = [Centi_Nodes*[error_diff],Deci_Nodes*[error_diff]]
    '''
    #Initialize back propagation lists and lists of lists
    Current_Master_PC_values = [Centi_Nodes*[starting_PC],Deci_Nodes*[starting_PC]]
    Current_Master_PC_gains = [Centi_Nodes*[gain],Deci_Nodes*[gain]]
    Current_Master_PC_errors = [Centi_Nodes*[error_diff],Deci_Nodes*[error_diff]]
    sub_iter = 0
    Current_Master_PC_sub_iter = [Centi_Nodes*[sub_iter],Deci_Nodes*[sub_iter]]
    #Initialize convergence condition
    Convergence_Vector = [Centi_Nodes*[0],Deci_Nodes*[0]]
    conv_cond = 0
    #Write the first line to a configuration file
    Current_Master_PC_values = Config_File_Write(Current_Master_PC_values,
                                                 Current_Master_PC_gains,
                                                 Current_Master_PC_errors,
                                                 Current_Master_PC_sub_iter,
                                                 Convergence_Vector,mand_iters,
                                                 gain_adapt)
    '''
    Initiate back propagation on Macro Node 1
    '''
    iteration = 0
    while(conv_cond < 12):
        #Initialize sub iterations
        sub_iter = 0
        PC_SubIter_Master_History = [Centi_Nodes*[sub_iter],Deci_Nodes*[sub_iter]]
        #Initialize error convergence condition
        Error_Convergence = [Centi_Nodes*[0],Deci_Nodes*[0]]
        error_conv_cond = 0
        while ((error_conv_cond < 12) or (sub_iter < mand_iters)):
            #Increment iterations
            iteration = iteration + 1
            sub_iter = sub_iter + 1
            '''
            Call the Macro Node 1 decision
            '''
            #Summon a random hand
            first_hand = Jacks_or_Better_4WL.Random_Cards(5)
            #Send the first hand to the neural network
            [Drop_Card,activation_list] = Wilson_Lazarus_N1_D2_BP.Drop_Card_Neural_Network(first_hand,Current_PC_Master_list)
            #Build the second hand
            second_hand = []
            #Test if no cards were recommended for drop
            if (Drop_Card == 0):
                second_hand = first_hand
            else:
                for i in range(len(first_hand)):
                    #Drop the cards in the Drop Card list
                    if (first_hand[i] not in Drop_Card):
                        second_hand.append(first_hand[i])
            #Calculate cards to recover
            card_recover_quantity = len(first_hand)-len(second_hand)
            '''
            Obtain Decision Results
            '''
            #Establish the strength of training parameters
            bet_per_hand = 1
            total_hands = 50
            #Initialize Reward Tallies
            RoyFl = 0
            Str8Fl = 0
            Quad = 0
            FullH = 0
            Floosh = 0
            Str8 = 0
            Trip = 0
            DoubP = 0
            Pair = 0
            #Generate new hands and reward user
            WL_reward = 0
            for j in range(total_hands):
                #Initialize individual hand reward
                temp_reward = 0
                #Collect other cards
                temp_cards = Jacks_or_Better_4WL.Random_Cards(card_recover_quantity)
                #Append new cards
                temp_hand = second_hand + temp_cards
                #Assign hand reward
                temp_reward = Jacks_or_Better_4WL.Reward(temp_hand,reward_vector)
                #Add hand reward to user account
                WL_reward = WL_reward + (temp_reward[0] * bet_per_hand)
                #Tally Rewards
                if (temp_reward[0] == reward_vector[0]):
                    Pair = Pair + 1
                elif (temp_reward[0] == reward_vector[1]):
                    DoubP = DoubP + 1
                elif (temp_reward[0] == reward_vector[2]):
                    Trip = Trip + 1
                elif (temp_reward[0] == reward_vector[3]):
                    Str8 = Str8 + 1
                elif (temp_reward[0] == reward_vector[4]):
                    Floosh = Floosh + 1
                elif (temp_reward[0] == reward_vector[5]):
                    FullH = FullH + 1
                elif (temp_reward[0] == reward_vector[6]):
                    Quad = Quad + 1
                elif (temp_reward[0] == reward_vector[7]):
                    Str8Fl = Str8Fl + 1
                elif (temp_reward[0] == reward_vector[8]):
                    RoyFl = RoyFl + 1      
            '''
            Calculate Decision Results
            '''
            total_bet = bet_per_hand * total_hands
            bet_net_gain = ((round((WL_reward - total_bet),2))/total_hands)*100
            '''
            Modify Priority Coefficients for each Node based on decision results
            '''
            
            '''
            Recalculate error convergence condition
            '''
            for L2 in range(len(Error_Convergence)):
                conv_internal_list = Error_Convergence[L2]
                #Calculate sum of strategy level list of lists
                error_conv_cond = error_conv_cond + sum(conv_internal_list)
        '''
        Attenuate the gain
        '''
        
        '''
        Recalculate convergence condition
        '''
        for L2 in range(len(Convergence_Vector)):
            conv_internal_list = Convergence_Vector[L2]
            #Calculate sum of strategy level list of lists
            conv_cond = conv_cond + sum(conv_internal_list)    
    return(Convergence_Vector)

def Wilson_Lazarus_Training():
    #Import time library
    import time
    #Establish reward vector
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    #Choose between convergence and fixed training sets
    training_method = "convergence"
    #Initiate training
    if (training_method == "convergence"):
        #Set convergence parameters
        A = 0.025
        B = 7
        [Convergence_Vector] = Convergence_Training(A,B,reward_vector)
    elif (training_method == "fixed"):
        '''
        #Set fixed training parameters
        Fixed_Iterations = 1000000
        Discretization = 0.001
        Amplification = 7
        '''
        A = 0.025
        B = 7
        [Node_PC_vect] = Initiate_Training(A,B,reward_vector)
        [Node_PC_vect] = Fixed_Iteration_Training(A,B,reward_vector)
    else:
        print('Training Method Not Selected Properly')
        time.sleep(60)
    return(training_method)

Wilson_Lazarus_Training()
