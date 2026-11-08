#This program runs every conceivable hand combination for the 30 possible unknown decisions that a user could make
#The final (31st) combination simply needs to be evaluated by the reward subroutine
#Once the averages and errors have been collected the combinations are 

def hand_index_conv(test_combination,hand):
    #Cycle through each test combination value to collect hand cards
    second_hand = []
    for i in range(len(test_combination)):
        second_hand.append(hand[test_combination[i]-1])
    return(second_hand)

def Data_Collection(hand,Baseline_Probabilities,reward_vector):
    #Import the time library
    import time
    #Access the Jacks or Better experimental case study function list
    import Jacks_or_Better_Exp_CS
    #Establish the pallidromic master list
    master_list = [[[]], [[1], [2], [3], [4], [5]], [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]], [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]], [[1, 2, 3, 4, 5]]]
    #Calculate Baseline BNG
    Baseline_BNG = 0
    for bng in range(len(reward_vector)):
        Baseline_BNG = Baseline_BNG + (Baseline_Probabilities[bng]*reward_vector[bng])
    Baseline_BNG = ((Baseline_BNG-1)*100)
    #Cycle through each list collecting the the data for each test combination while skiping the empty list and the 5 card list
    averages = [Baseline_BNG]
    errors = [0]
    times = [0]
    for m in range(1,(len(master_list)-1)):
        internal_list = master_list[m]
        for i in range(len(internal_list)):
            test_combination = master_list[m][i]
            #Convert test_combination to card values
            second_hand = hand_index_conv(test_combination,hand)
            #Obtain average and error for the test combination
            start_time = time.time()
            [rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors] = Jacks_or_Better_Exp_CS.Case_Study(hand,second_hand,reward_vector)
            delta_time = (time.time() - start_time)
            #Concatenate values
            averages.append(rel_BNG_avg)
            errors.append(rel_BNG_error)
            times.append(delta_time)
    #Evaluate the full hand decision
    FiC_reward = Jacks_or_Better_Exp_CS.Reward(hand,reward_vector)
    #Bet net gain calculation
    FiC_bng = ((FiC_reward[0] - 1)*100)
    #Concatenate final values
    averages.append(FiC_bng)
    errors.append(0)
    times.append(0)
    return(averages,errors,times)

def Definitive_Validation():
    #Access the Jacks or Better experimental case study function list
    import Jacks_or_Better_Exp_CS
    #Import Sort Vect
    import Sort_Vect
    #Establish reward vector
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    #Establish baseline probabilities
    All_Hands_Count = 2598960
    Baseline_Reward_Count = [(1098240*(4/13)),123552,54912,10200,5108,3744,624,36,4]
    Baseline_Probabilities = [0] * len(Baseline_Reward_Count)
    for bp in range(len(Baseline_Reward_Count)):
        Baseline_Probabilities[bp] = Baseline_Reward_Count[bp]/All_Hands_Count
    #Specify the number of random hands to be tested
    Hands_to_Test = 1
    #Initialize hand counting variable
    hand_iters = 0
    while (hand_iters < Hands_to_Test):
        #hand iteration counter
        hand_iters = hand_iters + 1
        #Establish hand to test
        '''
        first_hand = Jacks_or_Better_Exp_CS.Random_Cards(5)
        '''
        #Fix hand to test for reward vector analysis
        first_hand = [3,16,25,47,46]
        
        #Open the hand data file for writing
        Hnd_file = open("Def_Val_Hnd.txt","a+")
        for i in range(len(first_hand)):
            Hnd_file.write(str(first_hand[i]))
            Hnd_file.write(" ")
        Hnd_file.write('\n')
        Hnd_file.close()
        #Collect validation data for the hand
        [averages,errors,times] = Data_Collection(first_hand,Baseline_Probabilities,reward_vector)
        #Initialize the three data vectors
        Lows = []
        Meds = []
        Hiis = []
        for i in range(len(averages)):
            #Calculate data vectors
            low = (averages[i]-errors[i])
            med = (averages[i])
            hii = (averages[i]+errors[i])
            #Append the data vectors
            Lows.append(low)
            Meds.append(med)
            Hiis.append(hii)
        #Initialize data vectors with new reference values
        New_ref_Lows = []
        New_ref_Meds = []
        New_ref_Hiis = []
        for i in range(len(Lows)):
            #Calculate data vectors with new reference values
            new_low = Lows[i] - min(Lows)
            new_med = Meds[i] - min(Meds)
            new_hii = Hiis[i] - min(Hiis)
            #Append the data vectors
            New_ref_Lows.append(new_low)
            New_ref_Meds.append(new_med)
            New_ref_Hiis.append(new_hii)
        #Normalize the data vectors to calculate the value score
        Value_Scores = []
        for i in range(len(Lows)):
            #Calculate component value scores
            low_scor = New_ref_Lows[i]/max(New_ref_Lows[i])
            med_scor = New_ref_Meds[i]/max(New_ref_Meds[i])
            hii_scor = New_ref_Hiis[i]/max(New_ref_Hiis[i])
            #Calculate the total value score
            score = (low_scor + med_scor + hii_scor)/3
            #Append the total value score
            Value_Scores.append(score)
        #Sort the value scores
        [sort_valscor_vect,sort_valscor_ide_vect] = Sort_Vect.Sort_1D_List(Value_Scores)
        #Open the averages data file for writing
        Avg_file = open("Def_Val_Avg.txt","a+")
        #Print data averages
        for j in range(len(averages)):
            Avg_file.write(str(averages[j])),
            Avg_file.write(" ")
        Avg_file.write('\n')
        Avg_file.close()
        #Open the errors data file for writing
        Err_file = open("Def_Val_Err.txt","a+")
        #Print data errors
        for k in range(len(errors)):
            Err_file.write(str(errors[k])),
            Err_file.write(" ")
        Err_file.write('\n')
        Err_file.close()
        #Open the times data file for writing
        Tim_file = open("Def_Val_Tim.txt","a+")
        #Print data times
        for m in range(len(times)):
            Tim_file.write(str(times[m])),
            Tim_file.write(" ")
        Tim_file.write('\n')
        Tim_file.close()
    return(1)

Definitive_Validation()
