#This program completes targeted definitive validation
#of all possible unique decisions for 5 cards of 52 different values

def Zero_Cards(reward_vector):
    #Import the time library
    import time
    #Start the zero card time metric
    start_time = time.time()
    #Establish baseline probabilities
    All_Hands_Count = 2598960
    Baseline_Reward_Count = [(1098240*(4/13)),123552,54912,10200,5108,3744,624,36,4]
    Baseline_Probabilities = [0] * len(Baseline_Reward_Count)
    for bp in range(len(Baseline_Reward_Count)):
        Baseline_Probabilities[bp] = (Baseline_Reward_Count[bp]/All_Hands_Count)*100
    #Calculate Baseline BNG
    Baseline_BNG = 0
    for bng in range(len(reward_vector)):
        Baseline_BNG = Baseline_BNG + ((Baseline_Probabilities[bng]/100)*reward_vector[bng])
    Baseline_BNG = ((Baseline_BNG-1)*100)
    #Set Baseline Probability Errors
    Baseline_Probability_Errors = [0] * len(Baseline_Reward_Count)
    #Open the Bet Net Gain file for writing
    BNG_file = open("All_Card_Decision_BNGs.txt","a+")
    BNG_file.write(str(Baseline_BNG))
    BNG_file.write(" ")
    BNG_file.write('\n')
    BNG_file.close()
    #Open the Probabilities file for writing
    PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(Baseline_Probabilities)):
        PRB_file.write(str(Baseline_Probabilities[i])),
        PRB_file.write(" ")
    PRB_file.write('\n')
    PRB_file.close()
    #Open the Times file for writing
    delta_time = (time.time() - start_time)
    TIM_file = open("All_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    return(Baseline_BNG,Baseline_Probabilities,Baseline_Probability_Errors)

def One_Cards(Reward_Vect):
    #Import the time library
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize the bet net gain list
    OnC_BNGs = [0] * 52
    #Initialize the bet net gain error list
    OnC_BNG_Errors = [0] * 52
    #Initialize the reward probabilities list
    OnC_Probabilities = []
    #Initialize the reward probability error list
    OnC_Probability_Errors = []
    #Start the one card time metric
    start_time = time.time()
    #Card 1 ranges from 1 to 52
    for c1 in range(1,53):
        #Set the first hand as an input necessity
        first_hand = [1,2,3,4,5]
        #Set the list of decision values
        Decision = [c1]
        #Simulate the Decision to calculate the BNG, BNG error, Reward Probabilities, Reward Probability Errors
        [rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors] = Jacks_or_Better_Exp_CS.Case_Study(first_hand,Decision,Reward_Vect)
        #Record BNG values
        OnC_BNGs[(c1-1)] = rel_BNG_avg
        #Record BNG errors
        OnC_BNG_Errors[(c1-1)] = rel_BNG_error
        #Record reward probabilities
        OnC_Probabilities.append(Reward_Probs)
        #Record reward probability errors
        OnC_Probability_Errors.append(Reward_Prob_Errors)
    #Calculate the delta time
    delta_time = (time.time() - start_time)
    #Open the Times file for writing
    TIM_file = open("All_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    #Open the Bet Net Gain file for writing
    ALL_BNG_file = open("All_Card_Decision_BNGs.txt","a+")
    for bng in range(len(OnC_BNGs)):
        ALL_BNG_file.write(str(OnC_BNGs[bng]))
        ALL_BNG_file.write(" ")
        ALL_BNG_file.write('\n')
    ALL_BNG_file.close()
    #Open the Bet Net Gain Error file for writing
    ALL_BNG_e_file = open("All_Card_Decision_BNG_Errors.txt","a+")
    for bng_e in range(len(OnC_BNG_Errors)):
        ALL_BNG_e_file.write(str(OnC_BNG_Errors[bng_e]))
        ALL_BNG_e_file.write(" ")
        ALL_BNG_e_file.write('\n')
    ALL_BNG_e_file.close()
    #Open the Probabilities file for writing
    ALL_PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(OnC_Probabilities)):
        internal_list = OnC_Probabilities[i]
        for j in range(len(internal_list)):
            ALL_PRB_file.write(str(OnC_Probabilities[i][j])),
            ALL_PRB_file.write(" ")
        ALL_PRB_file.write('\n')
    ALL_PRB_file.close()
    #Open the Errors file for writing
    ALL_ERR_file = open("All_Decision_Reward_Probability_Errors.txt","a+")
    for k in range(len(OnC_Probability_Errors)):
        internal_list = OnC_Probability_Errors[k]
        for m in range(len(internal_list)):
            ALL_ERR_file.write(str(OnC_Probability_Errors[k][m])),
            ALL_ERR_file.write(" ")
        ALL_ERR_file.write('\n')
    ALL_ERR_file.close()
    #Open the Bet Net Gain file for writing
    ONE_BNG_file = open("All_One_Card_Decision_BNGs.txt","a+")
    for bng in range(len(OnC_BNGs)):
        ONE_BNG_file.write(str(OnC_BNGs[bng]))
        ONE_BNG_file.write(" ")
        ONE_BNG_file.write('\n')
    ONE_BNG_file.close()
    #Open the Bet Net Gain Error file for writing
    ONE_BNG_e_file = open("All_One_Card_Decision_BNG_Errors.txt","a+")
    for bng_e in range(len(OnC_BNG_Errors)):
        ONE_BNG_e_file.write(str(OnC_BNG_Errors[bng_e]))
        ONE_BNG_e_file.write(" ")
        ONE_BNG_e_file.write('\n')
    ONE_BNG_e_file.close()
    #Open the Probabilities file for writing
    ONE_PRB_file = open("One_Card_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(OnC_Probabilities)):
        internal_list = OnC_Probabilities[i]
        for j in range(len(internal_list)):
            ONE_PRB_file.write(str(OnC_Probabilities[i][j])),
            ONE_PRB_file.write(" ")
        ONE_PRB_file.write('\n')
    ONE_PRB_file.close()
    #Open the Errors file for writing
    ONE_ERR_file = open("One_Card_Decision_Reward_Probability_Errors.txt","a+")
    for k in range(len(OnC_Probability_Errors)):
        internal_list = OnC_Probability_Errors[k]
        for m in range(len(internal_list)):
            ONE_ERR_file.write(str(OnC_Probability_Errors[k][m])),
            ONE_ERR_file.write(" ")
        ONE_ERR_file.write('\n')
    ONE_ERR_file.close()
    return(rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors)

def Two_Cards(Reward_Vect):
    #Import the time library
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize the bet net gain list
    TwC_BNGs = []
    #Initialize the bet net gain error list
    TwC_BNG_Errors = []
    #Initialize the reward probabilities list
    TwC_Probabilities = []
    #Initialize the reward probability error list
    TwC_Probability_Errors = []
    #Start the one card time metric
    start_time = time.time()
    #Card 1 ranges from 1 to 51
    for c1 in range(1,52):
        for c2 in range(2,53):
            #Set the first hand as an input necessity
            first_hand = [1,2,3,4,5]
            #Set the list of decision values
            Decision = [c1,c2]
            #Simulate the Decision to calculate the BNG, BNG error, Reward Probabilities, Reward Probability Errors
            [rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors] = Jacks_or_Better_Exp_CS.Case_Study(first_hand,Decision,Reward_Vect)
            #Record BNG values
            TwC_BNGs.append(rel_BNG_avg)
            #Record BNG errors
            TwC_BNG_Errors.append(rel_BNG_error)
            #Record reward probabilities
            TwC_Probabilities.append(Reward_Probs)
            #Record reward probability errors
            TwC_Probability_Errors.append(Reward_Prob_Errors)
    #Calculate the delta time
    delta_time = (time.time() - start_time)
    #Open the Times file for writing
    TIM_file = open("All_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    #Open the Bet Net Gain file for writing
    ALL_BNG_file = open("All_Card_Decision_BNGs.txt","a+")
    for bng in range(len(TwC_BNGs)):
        ALL_BNG_file.write(str(TwC_BNGs[bng]))
        ALL_BNG_file.write(" ")
        ALL_BNG_file.write('\n')
    ALL_BNG_file.close()
    #Open the Bet Net Gain Error file for writing
    ALL_BNG_e_file = open("All_Card_Decision_BNG_Errors.txt","a+")
    for bng_e in range(len(TwC_BNG_Errors)):
        ALL_BNG_e_file.write(str(TwC_BNG_Errors[bng_e]))
        ALL_BNG_e_file.write(" ")
        ALL_BNG_e_file.write('\n')
    ALL_BNG_e_file.close()
    #Open the Probabilities file for writing
    ALL_PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(TwC_Probabilities)):
        internal_list = TwC_Probabilities[i]
        for j in range(len(internal_list)):
            ALL_PRB_file.write(str(TwC_Probabilities[i][j])),
            ALL_PRB_file.write(" ")
        ALL_PRB_file.write('\n')
    ALL_PRB_file.close()
    #Open the Errors file for writing
    ALL_ERR_file = open("All_Decision_Reward_Probability_Errors.txt","a+")
    for k in range(len(TwC_Probability_Errors)):
        internal_list = TwC_Probability_Errors[k]
        for m in range(len(internal_list)):
            ALL_ERR_file.write(str(TwC_Probability_Errors[k][m])),
            ALL_ERR_file.write(" ")
        ALL_ERR_file.write('\n')
    ALL_ERR_file.close()
    #Open the Bet Net Gain file for writing
    TWO_BNG_file = open("All_Two_Card_Decision_BNGs.txt","a+")
    for bng in range(len(TwC_BNGs)):
        TWO_BNG_file.write(str(TwC_BNGs[bng]))
        TWO_BNG_file.write(" ")
        TWO_BNG_file.write('\n')
    TWO_BNG_file.close()
    #Open the Bet Net Gain Error file for writing
    TWO_BNG_e_file = open("All_Two_Card_Decision_BNG_Errors.txt","a+")
    for bng_e in range(len(TwC_BNG_Errors)):
        TWO_BNG_e_file.write(str(TwC_BNG_Errors[bng_e]))
        TWO_BNG_e_file.write(" ")
        TWO_BNG_e_file.write('\n')
    TWO_BNG_e_file.close()
    #Open the Probabilities file for writing
    TWO_PRB_file = open("Two_Card_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(TwC_Probabilities)):
        internal_list = TwC_Probabilities[i]
        for j in range(len(internal_list)):
            TWO_PRB_file.write(str(TwC_Probabilities[i][j])),
            TWO_PRB_file.write(" ")
        TWO_PRB_file.write('\n')
    TWO_PRB_file.close()
    #Open the Errors file for writing
    TWO_ERR_file = open("Two_Card_Decision_Reward_Probability_Errors.txt","a+")
    for k in range(len(TwC_Probability_Errors)):
        internal_list = TwC_Probability_Errors[k]
        for m in range(len(internal_list)):
            TWO_ERR_file.write(str(TwC_Probability_Errors[k][m])),
            TWO_ERR_file.write(" ")
        TWO_ERR_file.write('\n')
    TWO_ERR_file.close()
    return(rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors)

def Three_Cards(Reward_Vect):
    #Import time library
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Start the three card time metric
    start_time = time.time()
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        #Initialize the master decision list
        master_decision_list = []
        #Initialize BNG list
        ThC_BNGs = []
        #Initialize Probabilities nested list
        ThC_Probabilities = []
        #Card 2 ranges from 2 to 49
        for c2 in range((c1+1),50):
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Increment decision count
                decision_count = decision_count + 1
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
                #Initialize hand count
                hand_count = 0
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    #Card 5 ranges from 5 to 52
                    for c5 in range((c4+1),53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Evaluate the decision
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,Reward_Vect)
                        #Tally Rewards
                        if (hand_reward[0] == Reward_Vect[0]):
                            Pair = Pair + 1
                        elif (hand_reward[0] == Reward_Vect[1]):
                            DoubP = DoubP + 1
                        elif (hand_reward[0] == Reward_Vect[2]):
                            Trip = Trip + 1
                        elif (hand_reward[0] == Reward_Vect[3]):
                            Str8 = Str8 + 1
                        elif (hand_reward[0] == Reward_Vect[4]):
                            Floosh = Floosh + 1
                        elif (hand_reward[0] == Reward_Vect[5]):
                            FullH = FullH + 1
                        elif (hand_reward[0] == Reward_Vect[6]):
                            Quad = Quad + 1
                        elif (hand_reward[0] == Reward_Vect[7]):
                            Str8Fl = Str8Fl + 1
                        elif (hand_reward[0] == Reward_Vect[8]):
                            RoyFl = RoyFl + 1
                        #Increment hand count
                        hand_count = hand_count + 1
                #Record Probabilities
                probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
                ThC_Probabilities.append(probabilities)
                #Calculate BNGs
                thc_bng = 0
                for prb in range(len(ThC_Probabilities)):
                    internal_list = ThC_Probabilities[prb]
                    for bng in range(len(internal_list)):
                        thc_bng = thc_bng + ((ThC_Probabilities[prb][bng]/100) * Reward_Vect[bng])
                thc_bng = ((thc_bng-1)*100)
                #Record BNGs
                ThC_BNGs.append(thc_bng)
        #Open the Bet Net Gain file for writing
        ALL_BNG_file = open("All_Card_Decision_BNGs.txt","a+")
        for i in range(len(ThC_BNGs)):
            ALL_BNG_file.write(str(ThC_BNGs[i]))
            ALL_BNG_file.write(" ")
        ALL_BNG_file.write('\n')
        ALL_BNG_file.close()
        #Open the Probabilities file for writing
        ALL_PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
        for j1 in range(len(ThC_Probabilities)):
            internal_list = ThC_Probabilities[j1]
            for j2 in range(len(internal_list)):
                ALL_PRB_file.write(str(ThC_Probabilities[j1][j2])),
                ALL_PRB_file.write(" ")
            ALL_PRB_file.write('\n')
        ALL_PRB_file.close()
        #Open the Bet Net Gain file for writing
        THR_BNG_file = open("All_Three_Card_Decision_BNGs.txt","a+")
        for i in range(len(ThC_BNGs)):
            THR_BNG_file.write(str(ThC_BNGs[i]))
            THR_BNG_file.write(" ")
        THR_BNG_file.write('\n')
        THR_BNG_file.close()
        #Open the Probabilities file for writing
        THR_PRB_file = open("Three_Card_Decision_Reward_Probabilities.txt","a+")
        for j1 in range(len(ThC_Probabilities)):
            internal_list = ThC_Probabilities[j1]
            for j2 in range(len(internal_list)):
                THR_PRB_file.write(str(ThC_Probabilities[j1][j2])),
                THR_PRB_file.write(" ")
            THR_PRB_file.write('\n')
        THR_PRB_file.close()
        print(hand)
    #Calculate the delta time
    delta_time = (time.time() - start_time)
    #Open the Times file for writing
    TIM_file = open("All_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    return(ThC_BNGs,ThC_Probabilities)

def Four_Cards(Reward_Vect):
    #Import time library
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Start the four card time metric
    start_time = time.time()
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        #Initialize the master decision list
        master_decision_list = []
        #Initialize BNG list
        FoC_BNGs = []
        #Initialize Probabilities nested list
        FoC_Probabilities = []
        #Card 2 ranges from 2 to 49
        for c2 in range((c1+1),50):
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    #Increment decision count
                    decision_count = decision_count + 1
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
                    #Initialize hand count
                    hand_count = 0
                    #Card 5 ranges from 5 to 52
                    for c5 in range((c4+1),53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Evaluate the decision
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,Reward_Vect)
                        #Tally Rewards
                        if (hand_reward[0] == Reward_Vect[0]):
                            Pair = Pair + 1
                        elif (hand_reward[0] == Reward_Vect[1]):
                            DoubP = DoubP + 1
                        elif (hand_reward[0] == Reward_Vect[2]):
                            Trip = Trip + 1
                        elif (hand_reward[0] == Reward_Vect[3]):
                            Str8 = Str8 + 1
                        elif (hand_reward[0] == Reward_Vect[4]):
                            Floosh = Floosh + 1
                        elif (hand_reward[0] == Reward_Vect[5]):
                            FullH = FullH + 1
                        elif (hand_reward[0] == Reward_Vect[6]):
                            Quad = Quad + 1
                        elif (hand_reward[0] == Reward_Vect[7]):
                            Str8Fl = Str8Fl + 1
                        elif (hand_reward[0] == Reward_Vect[8]):
                            RoyFl = RoyFl + 1
                        #Increment hand count
                        hand_count = hand_count + 1
                    #Record Probabilities
                    probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
                    FoC_Probabilities.append(probabilities)
                    #Calculate BNGs
                    foc_bng = 0
                    for prb in range(len(FoC_Probabilities)):
                        internal_list = FoC_Probabilities[prb]
                        for bng in range(len(internal_list)):
                            foc_bng = foc_bng + ((FoC_Probabilities[prb][bng]/100)*Reward_Vect[bng])
                    foc_bng = ((foc_bng-1)*100)
                    #Record BNGs
                    FoC_BNGs.append(foc_bng)
        #Open the Bet Net Gain file for writing
        ALL_BNG_file = open("All_Card_Decision_BNGs.txt","a+")
        for i in range(len(FoC_BNGs)):
            ALL_BNG_file.write(str(FoC_BNGs[i]))
            ALL_BNG_file.write(" ")
        ALL_BNG_file.write('\n')
        ALL_BNG_file.close()
        #Open the Probabilities file for writing
        ALL_PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
        for j1 in range(len(FoC_Probabilities)):
            internal_list = FoC_Probabilities[j1]
            for j2 in range(len(internal_list)):
                ALL_PRB_file.write(str(FoC_Probabilities[j1][j2])),
                ALL_PRB_file.write(" ")
            ALL_PRB_file.write('\n')
        ALL_PRB_file.close()
        #Open the Bet Net Gain file for writing
        FOR_BNG_file = open("All_Four_Card_Decision_BNGs.txt","a+")
        for i in range(len(FoC_BNGs)):
            FOR_BNG_file.write(str(FoC_BNGs[i]))
            FOR_BNG_file.write(" ")
        FOR_BNG_file.write('\n')
        FOR_BNG_file.close()
        #Open the Probabilities file for writing
        FOR_PRB_file = open("Four_Card_Decision_Reward_Probabilities.txt","a+")
        for j1 in range(len(FoC_Probabilities)):
            internal_list = FoC_Probabilities[j1]
            for j2 in range(len(internal_list)):
                FOR_PRB_file.write(str(FoC_Probabilities[j1][j2])),
                FOR_PRB_file.write(" ")
            FOR_PRB_file.write('\n')
        FOR_PRB_file.close()
        print(hand)
    #Calculate the delta time
    delta_time = (time.time() - start_time)
    #Open the Times file for writing
    TIM_file = open("All_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    return(FoC_BNGs,FoC_Probabilities)

'''
def Five_Cards(Reward_Vect):
    #Import time library
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        #Start the five card card 1 iteration time metric
        start_time = time.time()
        #Initialize the master decision list
        master_decision_list = []
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
        #Initialize BNG list
        FiC_BNGs = []
        #Initialize Probabilities nested list
        FiC_Probabilities = []
        #Initialize Probabilities Errors nested list
        FiC_Errors = []
        #Card 2 ranges from 2 to 49
        for c2 in range((c1+1),50):
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    #Card 5 ranges from 5 to 52
                    for c5 in range((c4+1),53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Evaluate the decision
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,Reward_Vect)
                        #Bet net gain calculation
                        FiC_BNGs.append((hand_reward[0] - 1)*100)
                        #Tally Rewards
                        if (hand_reward[0] == Reward_Vect[0]):
                            Pair = 1
                        elif (hand_reward[0] == Reward_Vect[1]):
                            DoubP = 1
                        elif (hand_reward[0] == Reward_Vect[2]):
                            Trip = 1
                        elif (hand_reward[0] == Reward_Vect[3]):
                            Str8 = 1
                        elif (hand_reward[0] == Reward_Vect[4]):
                            Floosh = 1
                        elif (hand_reward[0] == Reward_Vect[5]):
                            FullH = 1
                        elif (hand_reward[0] == Reward_Vect[6]):
                            Quad = 1
                        elif (hand_reward[0] == Reward_Vect[7]):
                            Str8Fl = 1
                        elif (hand_reward[0] == Reward_Vect[8]):
                            RoyFl = 1
                        #Record Probabilities
                        probabilities = [(Pair*100),(DoubP*100),(Trip*100),(Str8*100),(Floosh*100),(FullH*100),(Quad*100),(Str8Fl*100),(RoyFl*100)]
                        FiC_Probabilities.append(probabilities)
                        #Record Errors
                        errors = [0] * 9
                        FiC_Errors.append(errors)
        #Open the Bet Net Gain file for writing
        BNG_file = open("All_Five_Card_Decision_BNGs.txt","a+")
        for i in range(len(FiC_BNGs)):
            BNG_file.write(str(FiC_BNGs[i]))
            BNG_file.write(" ")
        BNG_file.write('\n')
        BNG_file.close()
        #Open the Probabilities file for writing
        PRB_file = open("All_Decision_Reward_Probabilities.txt","a+")
        for j1 in range(len(FiC_Probabilities)):
            internal_list = FiC_Probabilities[j1]
            for j2 in range(len(internal_list)):
                PRB_file.write(str(FiC_Probabilities[j1][j2])),
                PRB_file.write(" ")
            PRB_file.write('\n')
        PRB_file.close()
        #Open the Errors file for writing
        ERR_file = open("All_Decision_Reward_Probability_Errors.txt","a+")
        for k1 in range(len(FiC_Errors)):
            internal_list = FiC_Errors[k1]
            for k2 in range(len(internal_list)):
                ERR_file.write(str(FiC_Errors[k1][k2])),
                ERR_file.write(" ")
            ERR_file.write('\n')
        ERR_file.close()
        print(hand)
        delta_time = (time.time() - start_time)
        print(delta_time)
        #Open the Times file for writing
        TIM_file = open("All_Five_Card_Decision_Times.txt","a+")
        TIM_file.write(str(delta_time))
        TIM_file.write(" ")
        TIM_file.write('\n')
        TIM_file.close()
    return(FiC_BNGs,FiC_Probabilities,FiC_Errors)
'''

def Validate():
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Establish reward vector for all decisions
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    #Write the data for the ZERO CARDS decision
    [Baseline_BNG,Baseline_Probabilities,Baseline_Probability_Errors] = Zero_Cards(reward_vector)
    #Write the data for the ONE CARDS decision
    [OnC_BNGs,OnC_BNG_Errors,OnC_Probabilities,OnC_Prob_Errors] = One_Cards(reward_vector)
    #Write the data for the TWO CARDS decision
    [TwC_BNGs,TwC_BNG_Errors,TwC_Probabilities,TwC_Prob_Errors] = Two_Cards(reward_vector)
    #Write the data for the THREE CARDS decision
    [ThC_BNGs,ThC_Probabilities,ThC_Errors] = Three_Cards(reward_vector)
    #Write the data for the FOUR CARDS decision
    [FoC_BNGs,FoC_Probabilities,FoC_Errors] = Four_Cards(reward_vector)
    '''
    #Write the data for the FIVE CARDS decision
    [FiC_BNGs,FiC_Probabilities,FiC_Errors] = Five_Cards(reward_vector)
    '''

Validate()
