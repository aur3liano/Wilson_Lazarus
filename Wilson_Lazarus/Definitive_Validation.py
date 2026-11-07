d#This program runs every conceivable hand combination for the 30 possible unknown decisions that a user could make
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
    Baseline_BNG = (1*Baseline_BNG)-1
    #Cycle through each list collecting the the data for each test combination and skip the empty list
    averages = [Baseline_BNG]
    errors = [0]
    times = [0]
    for m in range(1,6):
        internal_list = master_list[m]
        for i in range(len(internal_list)):
            test_combination = master_list[m][i]
            #Convert test_combination to card values
            second_hand = hand_index_conv(test_combination,hand)
            #Obtain average and error for the test combination
            start_time = time.time()
            [rel_BNG_avg,rel_BNG_error] = Jacks_or_Better_Exp_CS.Case_Study(hand,second_hand,reward_vector)
            delta_time = (time.time() - start_time)
            #Concatenate values
            averages.append(rel_BNG_avg)
            errors.append(rel_BNG_error)
            times.append(delta_time)
    return(averages,errors,times)

def Definitive_Validation():
    #Access the Jacks or Better experimental case study function list
    import Jacks_or_Better_Exp_CS
    #Access the Jacks or Better 4WL
    import Jacks_or_Better_4WL
    #Establish reward vector
    Reward_Vect_Baseline = [3.25,8.89,20,107.67,215,293.33,1760,30506.67,274560]
    Reward_Vect_Gain = 0.065735472679572 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    #Establish baseline probabilities
    All_Hands_Count = 2598960
    Baseline_Reward_Count = [1098240 123552 54912 10200 5108 3744 624 36 4]
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
#        first_hand = Jacks_or_Better_4WL.Random_Cards(5)
        #Fix hand to test for reward vector analysis
        first_hand = [5,29,50,16,7]
        #Open the hand data file for writing
        Hnd_file = open("Def_Val_Hnd.txt","a+")
        for i in range(len(first_hand)):
            Hnd_file.write(str(first_hand[i]))
            Hnd_file.write(" ")
        Hnd_file.write('\n')
        Hnd_file.close()
        #Collect validation data for the hand
        [averages,errors,times] = Data_Collection(first_hand,Baseline_Probabilities,reward_vector)
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

Definitive_Validation()
