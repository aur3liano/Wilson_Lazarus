#This program completes targeted definitive validation
#of all possible unique decisions for 5 cards of 52 different values

def All_Card_Count():
    All_Card_lists = []
    
    one_dec_list = []
    for c1 in range(1,53):
        decision = [c1]
        one_dec_list.append(decision)
    All_Card_lists.append(one_dec_list)

    two_dec_list = []
    for c1 in range(1,52):
        for c2 in range((c1+1),53):
            decision = [c1,c2]
            two_dec_list.append(decision)
    All_Card_lists.append(two_dec_list)
    
    thr_dec_list = []
    for c1 in range(1,51):
        for c2 in range((c1+1),52):
            for c3 in range((c2+1),53):
                decision = [c1,c2,c3]
                thr_dec_list.append(decision)
    All_Card_lists.append(thr_dec_list)
    
    fou_dec_list = []
    for c1 in range(1,50):
        for c2 in range((c1+1),51):
            for c3 in range((c2+1),52):
                for c4 in range((c3+1),53):
                    decision = [c1,c2,c3,c4]
                    fou_dec_list.append(decision)
    All_Card_lists.append(fou_dec_list)
    '''
    fiv_hand_list = []
    for c1 in range(1,49):
        for c2 in range((c1+1),50):
            for c3 in range((c2+1),51):
                for c4 in range((c3+1),52):
                    for c5 in range((c4+1),53):
                        decision = [c1,c2,c3,c4,c5]
                        fiv_hand_list.append(decision)
    All_Card_lists.append(fiv_hand_list)
    '''
    return(All_Card_lists)

def Card_Valid_Func(Card_list):
    #Import libraries
    import time
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    
    #Establish reward vector for all decisions
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    
    #Initialize decision count
    decision_count = 0
    time_start = time.time()
    time_inc = 10
    time_print = time_inc
    Valid_Vals = []
    
    for cc in range(len(Card_list)):
        decision = Card_list[cc]
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
        hand_count = 0
        for mc in range(1,53):
            if (mc not in decision):
                hand = decision + [mc]
                #Evaluate the decision
                hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,reward_vector)
                #Tally Rewards
                if (hand_reward[0] == reward_vector[0]):
                    Pair = Pair + 1
                elif (hand_reward[0] == reward_vector[1]):
                    DoubP = DoubP + 1
                elif (hand_reward[0] == reward_vector[2]):
                    Trip = Trip + 1
                elif (hand_reward[0] == reward_vector[3]):
                    Str8 = Str8 + 1
                elif (hand_reward[0] == reward_vector[4]):
                    Floosh = Floosh + 1
                elif (hand_reward[0] == reward_vector[5]):
                    FullH = FullH + 1
                elif (hand_reward[0] == reward_vector[6]):
                    Quad = Quad + 1
                elif (hand_reward[0] == reward_vector[7]):
                    Str8Fl = Str8Fl + 1
                elif (hand_reward[0] == reward_vector[8]):
                    RoyFl = RoyFl + 1
                hand_count += 1
        if ((time.time()-time_start) > time_print):
            #Write to the log file
            prog_calc = round((decision_count/len(Card_list))*100,3)
            print('Progress: ',str(prog_calc),' %')
            print()
            time_print += time_inc
        num_zeros = 5-len(decision)
        dec_print = list(decision)
        for nz in range(num_zeros):
            dec_print.append(0)
        #Record Probabilities
        probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
        #Calculate BNGs
        bng = 0
        for prb in range(len(probabilities)):
            bng += ((probabilities[prb]/100)*reward_vector[prb])
        bng = ((bng-1)*100)
        temp_list = dec_print + [bng] + probabilities
        Valid_Vals.append(temp_list)
    return(Valid_Vals)

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
    BNG_file = open("Zero_Card_Decision_BNGs.txt","a+")
    BNG_file.write(str(Baseline_BNG))
    BNG_file.write(" ")
    BNG_file.write('\n')
    BNG_file.close()
    #Open the Probabilities file for writing
    PRB_file = open("Zero_Card_Decision_Reward_Probabilities.txt","a+")
    for i in range(len(Baseline_Probabilities)):
        PRB_file.write(str(Baseline_Probabilities[i])),
        PRB_file.write(" ")
    PRB_file.write('\n')
    PRB_file.close()
    #Open the Times file for writing
    delta_time = (time.time() - start_time)
    TIM_file = open("Zero_Card_Decision_Times.txt","a+")
    TIM_file.write(str(delta_time))
    TIM_file.write(" ")
    TIM_file.write('\n')
    TIM_file.close()
    return(Baseline_BNG,Baseline_Probabilities,Baseline_Probability_Errors)

'''
def One_Cards(reward_vector):
    #Import libraries
    import time
    import csv
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize all of the validation values
    Valid_Vals = []
    #Start the one card time metric
    start_time = time.time()
    #Card 1 ranges from 1 to 52
    for c1 in range(1,53):
        #Set the first hand as an input necessity
        first_hand = [1,2,3,4,5]
        #Set the list of decision values
        Decision = [c1]
        #Simulate the Decision to calculate the BNG, BNG error, Reward Probabilities, Reward Probability Errors
        [rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors] = Jacks_or_Better_Exp_CS.Case_Study(first_hand,Decision,reward_vector)
        #Record all of the validation values
        temp_list = [c1,0,0,0,0,rel_BNG_avg,rel_BNG_error] + Reward_Probs + Reward_Prob_Errors
        Valid_Vals.append(temp_list)
    #Calculate the delta time
    delta_time = (time.time() - start_time)
    print()
    print('Total_Time: ',str(round(delta_time,4)),' seconds')
    #Write the csv file
    Card_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5']
    BNG_header_section = ['BNG_Avg','BNG_Err']
    Prob_Avg_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
    Prob_Err_header_section = ['Pair_Err','Two_Pair_Err','Triple_Err','Straight_Err','Flush_Err','Full_House_Err','Quad_Err','Straight_Flush_Err','Royal_Flush_Err']
    #Build the full header list
    header = Card_header_section + BNG_header_section + Prob_Avg_header_section + Prob_Err_header_section
    with open('Single_Card_Dec_Valid.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = header)
        writer.writeheader()
        for vv in range(len(Valid_Vals)):
            temp_list = Valid_Vals[vv]
            temp_dict = {}
            for h in range(len(header)):
                temp_dict[header[h]] = temp_list[h]
            writer.writerow(temp_dict)
    csvfile.close()
    return(Valid_Vals)

def Two_Cards(reward_vector):
    #Import the time library
    import time
    import csv
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize all of the validation values
    Valid_Vals = []
    #Initialize decision count
    decision_count = 0
    #Initialize the writing flag
    write_flg = 0
    time_start = time.time()
    time_inc = 120
    time_print = time_inc
    #Card 1 ranges from 1 to 51
    for c1 in range(1,52):
        for c2 in range((c1+1),53):
            #Set the first hand as an input necessity
            first_hand = [1,2,3,4,5]
            #Set the list of decision values
            Decision = [c1,c2]
            #Simulate the Decision to calculate the BNG, BNG error, Reward Probabilities, Reward Probability Errors
            [rel_BNG_avg,rel_BNG_error,Reward_Probs,Reward_Prob_Errors] = Jacks_or_Better_Exp_CS.Case_Study(first_hand,Decision,reward_vector)
            #Record all of the validation values
            temp_list = [c1,c2,0,0,0,rel_BNG_avg,rel_BNG_error] + Reward_Probs + Reward_Prob_Errors
            Valid_Vals.append(temp_list)
            decision_count += 1
            if ((time.time()-time_start) > time_print):
                print('Decision: ',str(c1),' ',str(c2),' ',str(0),' ',str(0),' ',str(0))
                print()
                print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
                print()
                prog_calc = round((decision_count/2601)*100,3)
                print('Progress: ',str(prog_calc),' %')
                print()
                time_print += time_inc
            
    #Calculate the delta time
    delta_time = (time.time() - time_start)
    print()
    print('Total_Time: ',str(round(delta_time,4)),' seconds')
    #Write the csv file
    Card_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5']
    BNG_header_section = ['BNG_Avg','BNG_Err']
    Prob_Avg_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
    Prob_Err_header_section = ['Pair_Err','Two_Pair_Err','Triple_Err','Straight_Err','Flush_Err','Full_House_Err','Quad_Err','Straight_Flush_Err','Royal_Flush_Err']
    #Build the full header list
    header = Card_header_section + BNG_header_section + Prob_Avg_header_section + Prob_Err_header_section
    with open('Two_Card_Dec_Valid.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = header)
        writer.writeheader()
        for vv in range(len(Valid_Vals)):
            temp_list = Valid_Vals[vv]
            temp_dict = {}
            for h in range(len(header)):
                temp_dict[header[h]] = temp_list[h]
            writer.writerow(temp_dict)
    csvfile.close()
    return(Valid_Vals)
'''

def Two_Cards(reward_vector):
    #Import libraries
    import time
    import csv
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Initialize the writing flag
    write_flg = 0
    time_start = time.time()
    time_inc = 10
    time_print = time_inc
    Valid_Vals = []
    #Card 2 ranges from 2 to 49
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        for c2 in range((c1+1),50):
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
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    #Card 5 ranges from 5 to 52
                    for c5 in range((c4+1),53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Evaluate the decision
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,reward_vector)
                        #Tally Rewards
                        if (hand_reward[0] == reward_vector[0]):
                            Pair = Pair + 1
                        elif (hand_reward[0] == reward_vector[1]):
                            DoubP = DoubP + 1
                        elif (hand_reward[0] == reward_vector[2]):
                            Trip = Trip + 1
                        elif (hand_reward[0] == reward_vector[3]):
                            Str8 = Str8 + 1
                        elif (hand_reward[0] == reward_vector[4]):
                            Floosh = Floosh + 1
                        elif (hand_reward[0] == reward_vector[5]):
                            FullH = FullH + 1
                        elif (hand_reward[0] == reward_vector[6]):
                            Quad = Quad + 1
                        elif (hand_reward[0] == reward_vector[7]):
                            Str8Fl = Str8Fl + 1
                        elif (hand_reward[0] == reward_vector[8]):
                            RoyFl = RoyFl + 1
                        #Increment hand count
                        hand_count = hand_count + 1
                if ((time.time()-time_start) > time_print):
                    print('Decision: ',str(c1),' ',str(c2),' ',str(0),' ',str(0),' ',str(0))
                    print()
                    print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
                    print()
                    prog_calc = round((hand_count/2598960)*100,3)
                    print('Progress: ',str(prog_calc),' %')
                    time_print += time_inc
            decision = [c1,c2,0,0,0]
            #Record Probabilities
            probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
            #Calculate BNGs
            two_bng = 0
            for prb in range(len(probabilities)):
                two_bng += ((probabilities[prb]/100)*reward_vector[prb])
            two_bng = ((two_bng-1)*100)
            temp_list = decision + [two_bng,0] + probabilities + [0,0,0,0,0,0,0,0,0]
            Valid_Vals.append(temp_list)
    #Write the csv file
    Card_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5']
    BNG_header_section = ['BNG_Avg','BNG_Err']
    Prob_Avg_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
    Prob_Err_header_section = ['Pair_Err','Two_Pair_Err','Triple_Err','Straight_Err','Flush_Err','Full_House_Err','Quad_Err','Straight_Flush_Err','Royal_Flush_Err']
    #Build the full header list
    header = Card_header_section + BNG_header_section + Prob_Avg_header_section + Prob_Err_header_section
    with open('Two_Card_Dec_Valid.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = header)
        
        if (write_flg == 0):
            writer.writeheader()
            write_flg = 1
        for vv in range(len(Valid_Vals)):
            temp_list = Valid_Vals[vv]
            temp_dict = {}
            for h in range(len(header)):
                temp_dict[header[h]] = temp_list[h]
            writer.writerow(temp_dict)
    csvfile.close()
    return(Valid_Vals)

def Three_Cards(reward_vector):
    #Import libraries
    import time
    import csv
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Initialize the writing flag
    write_flg = 0
    time_start = time.time()
    time_inc = 10
    time_print = time_inc
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        Valid_Vals = []
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
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,reward_vector)
                        #Tally Rewards
                        if (hand_reward[0] == reward_vector[0]):
                            Pair = Pair + 1
                        elif (hand_reward[0] == reward_vector[1]):
                            DoubP = DoubP + 1
                        elif (hand_reward[0] == reward_vector[2]):
                            Trip = Trip + 1
                        elif (hand_reward[0] == reward_vector[3]):
                            Str8 = Str8 + 1
                        elif (hand_reward[0] == reward_vector[4]):
                            Floosh = Floosh + 1
                        elif (hand_reward[0] == reward_vector[5]):
                            FullH = FullH + 1
                        elif (hand_reward[0] == reward_vector[6]):
                            Quad = Quad + 1
                        elif (hand_reward[0] == reward_vector[7]):
                            Str8Fl = Str8Fl + 1
                        elif (hand_reward[0] == reward_vector[8]):
                            RoyFl = RoyFl + 1
                        #Increment hand count
                        hand_count = hand_count + 1
                decision = [c1,c2,c3,0,0]
                #Record Probabilities
                probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
                #Calculate BNGs
                thc_bng = 0
                for prb in range(len(probabilities)):
                    thc_bng += ((probabilities[prb]/100)*reward_vector[prb])
                thc_bng = ((thc_bng-1)*100)
                temp_list = decision + [thc_bng,0] + probabilities + [0,0,0,0,0,0,0,0,0]
                Valid_Vals.append(temp_list)
                if ((time.time()-time_start) > time_print):
                    print('Decision: ',str(c1),' ',str(c2),' ',str(c3),' ',str(0),' ',str(0))
                    print()
                    print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
                    print()
                    prog_calc = round((hand_count/2598960)*100,3)
                    print('Progress: ',str(prog_calc),' %')
                    time_print += time_inc
        #Write the csv file
        Card_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5']
        BNG_header_section = ['BNG_Avg','BNG_Err']
        Prob_Avg_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
        Prob_Err_header_section = ['Pair_Err','Two_Pair_Err','Triple_Err','Straight_Err','Flush_Err','Full_House_Err','Quad_Err','Straight_Flush_Err','Royal_Flush_Err']
        #Build the full header list
        header = Card_header_section + BNG_header_section + Prob_Avg_header_section + Prob_Err_header_section
        with open('Three_Card_Dec_Valid.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames = header)
            
            if (write_flg == 0):
                writer.writeheader()
                write_flg = 1
            for vv in range(len(Valid_Vals)):
                temp_list = Valid_Vals[vv]
                temp_dict = {}
                for h in range(len(header)):
                    temp_dict[header[h]] = temp_list[h]
                writer.writerow(temp_dict)
        csvfile.close()
    return(Valid_Vals)

def Four_Cards(reward_vector):
    #Import libraries
    import time
    import csv
    #Import Jacks_or_Better_Exp_CS
    import Jacks_or_Better_Exp_CS
    #Initialize decision count
    decision_count = 0
    #Initialize the writing flag
    write_flg = 0
    time_start = time.time()
    time_inc = 10
    time_print = time_inc
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        Valid_Vals = []
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
                    for c5 in range(1,53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Evaluate the decision
                        hand_reward = Jacks_or_Better_Exp_CS.Reward(hand,reward_vector)
                        #Tally Rewards
                        if (hand_reward[0] == reward_vector[0]):
                            Pair = Pair + 1
                        elif (hand_reward[0] == reward_vector[1]):
                            DoubP = DoubP + 1
                        elif (hand_reward[0] == reward_vector[2]):
                            Trip = Trip + 1
                        elif (hand_reward[0] == reward_vector[3]):
                            Str8 = Str8 + 1
                        elif (hand_reward[0] == reward_vector[4]):
                            Floosh = Floosh + 1
                        elif (hand_reward[0] == reward_vector[5]):
                            FullH = FullH + 1
                        elif (hand_reward[0] == reward_vector[6]):
                            Quad = Quad + 1
                        elif (hand_reward[0] == reward_vector[7]):
                            Str8Fl = Str8Fl + 1
                        elif (hand_reward[0] == reward_vector[8]):
                            RoyFl = RoyFl + 1
                        #Increment hand count
                        hand_count = hand_count + 1
                    decision = [c1,c2,c3,c4,0]
                    #Record Probabilities
                    probabilities = [((Pair/hand_count)*100),((DoubP/hand_count)*100),((Trip/hand_count)*100),((Str8/hand_count)*100),((Floosh/hand_count)*100),((FullH/hand_count)*100),((Quad/hand_count)*100),((Str8Fl/hand_count)*100),((RoyFl/hand_count)*100)]
                    #Calculate BNGs
                    foc_bng = 0
                    for prb in range(len(probabilities)):
                        foc_bng += ((probabilities[prb]/100)*reward_vector[prb])
                    foc_bng = ((foc_bng-1)*100)
                    temp_list = decision + [foc_bng,0] + probabilities + [0,0,0,0,0,0,0,0,0]
                    Valid_Vals.append(temp_list)
                    if ((time.time()-time_start) > time_print):
                        print('Decision: ',str(c1),' ',str(c2),' ',str(c3),' ',str(c4),' ',str(0))
                        print()
                        print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
                        print()
                        prog_calc = round((hand_count/2598960)*100,3)
                        print('Progress: ',str(prog_calc),' %')
                        time_print += time_inc
        #Write the csv file
        Card_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5']
        BNG_header_section = ['BNG_Avg','BNG_Err']
        Prob_Avg_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
        Prob_Err_header_section = ['Pair_Err','Two_Pair_Err','Triple_Err','Straight_Err','Flush_Err','Full_House_Err','Quad_Err','Straight_Flush_Err','Royal_Flush_Err']
        #Build the full header list
        header = Card_header_section + BNG_header_section + Prob_Avg_header_section + Prob_Err_header_section
        with open('Four_Card_Dec_Valid.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames = header)
            
            if (write_flg == 0):
                writer.writeheader()
                write_flg = 1
            for vv in range(len(Valid_Vals)):
                temp_list = Valid_Vals[vv]
                temp_dict = {}
                for h in range(len(header)):
                    temp_dict[header[h]] = temp_list[h]
                writer.writerow(temp_dict)
        csvfile.close()
    return(Valid_Vals)

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

def One_Card_Dec_Writing(process,One_Card_list):
    file_name = 'One_Card_Decs_' + str(process) + '.txt'
    One_File = open(file_name,'a')
    for fc in range(len(One_Card_list)):
        internal_list = One_Card_list[fc]
        for il in range(len(internal_list)):
            One_File.write(str(internal_list[il]))
            One_File.write(" ")
        One_File.write('\n')
    One_File.close()
    return(1)

def Two_Card_Dec_Writing(process,Two_Card_list):
    file_name = 'Two_Card_Decs_' + str(process) + '.txt'
    Two_File = open(file_name,'a')
    for fc in range(len(Two_Card_list)):
        internal_list = Two_Card_list[fc]
        for il in range(len(internal_list)):
            Two_File.write(str(internal_list[il]))
            Two_File.write(" ")
        Two_File.write('\n')
    Two_File.close()
    return(1)

def Three_Card_Dec_Writing(process,Thr_Card_list):
    file_name = 'Thr_Card_Decs_' + str(process) + '.txt'
    Thr_File = open(file_name,'a')
    for fc in range(len(Thr_Card_list)):
        internal_list = Thr_Card_list[fc]
        for il in range(len(internal_list)):
            Thr_File.write(str(internal_list[il]))
            Thr_File.write(" ")
        Thr_File.write('\n')
    Thr_File.close()
    return(1)

def Four_Card_Dec_Writing(process,Fou_Card_list):
    file_name = 'Fou_Card_Decs_' + str(process) + '.txt'
    Fou_File = open(file_name,'a')
    for fc in range(len(Fou_Card_list)):
        internal_list = Fou_Card_list[fc]
        for il in range(len(internal_list)):
            Fou_File.write(str(internal_list[il]))
            Fou_File.write(" ")
        Fou_File.write('\n')
    Fou_File.close()
    return(1)

def Three_Card_Fillout(Card_list):
    #Import libraries
    import time
    import csv
    #Initialize decision count
    decision_count = 0
    hand_count = 0
    write_flg = 0
    time_start = time.time()
    time_inc = 15
    time_print = time_inc
    master_decision_list = []
    for cc in range(len(Card_list)):
        decision_start = Card_list[cc]
        decision = list(decision_start)
        #Increment decision count
        decision_count = decision_count + 1
        for mc1 in range(1,53):
            if (mc1 not in decision):
                decision = decision + [mc1]
            for mc2 in range(1,53):
                if (mc2 not in decision):
                    decision = decision + [mc2]
                    hand_count +=1
                    master_decision_list.append(decision)
                    decision = list(decision_start + [mc1])
            decision = list(decision_start)
            if ((time.time()-time_start) > time_print):
                print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
                print()
                prog_calc = round((hand_count/2598960)*100,3)
                print('Progress: ',str(prog_calc),' %')
                time_print += time_inc
        #Write the csv file
        header = ['Card_1','Card_2','Card_3','Card_4','Card_5']
        with open('Three_Card_Fillout.csv', 'a', newline='') as csvfile:
            
            writer = csv.DictWriter(csvfile,fieldnames = header)
            
            if (write_flg == 0):
                writer.writeheader()
                write_flg = 1
            for mdl in range(len(master_decision_list)):
                temp_list = master_decision_list[mdl]
                temp_dict = {}
                for h in range(len(header)):
                    temp_dict[header[h]] = temp_list[h]
                writer.writerow(temp_dict)
        csvfile.close()
    return(1)

def Validate():
    #Generate all card lists
    All_Card_lists = All_Card_Count()
    
    #Decompose all card lists    
    One_Card_list_1 = All_Card_lists[0][0:6]
    One_Card_list_2 = All_Card_lists[0][6:11]
    One_Card_list_3 = All_Card_lists[0][11:16]
    One_Card_list_4 = All_Card_lists[0][16:21]
    One_Card_list_5 = All_Card_lists[0][21:26]
    One_Card_list_6 = All_Card_lists[0][26:31]
    One_Card_list_7 = All_Card_lists[0][31:36]
    One_Card_list_8 = All_Card_lists[0][36:41]
    One_Card_list_9 = All_Card_lists[0][41:46]
    One_Card_list_10 = All_Card_lists[0][46:52]
    
    Two_Card_list_1 = All_Card_lists[1][0:133]
    Two_Card_list_2 = All_Card_lists[1][133:265]
    Two_Card_list_3 = All_Card_lists[1][265:398]
    Two_Card_list_4 = All_Card_lists[1][398:530]
    Two_Card_list_5 = All_Card_lists[1][530:663]
    Two_Card_list_6 = All_Card_lists[1][663:796]
    Two_Card_list_7 = All_Card_lists[1][796:928]
    Two_Card_list_8 = All_Card_lists[1][928:1061]
    Two_Card_list_9 = All_Card_lists[1][1061:1193]
    Two_Card_list_10 = All_Card_lists[1][1193:1326]
    
    Thr_Card_list_1 = All_Card_lists[2][0:2210]
    Thr_Card_list_2 = All_Card_lists[2][2210:4420]
    Thr_Card_list_3 = All_Card_lists[2][4420:6630]
    Thr_Card_list_4 = All_Card_lists[2][6630:8840]
    Thr_Card_list_5 = All_Card_lists[2][8840:11050]
    Thr_Card_list_6 = All_Card_lists[2][11050:13260]
    Thr_Card_list_7 = All_Card_lists[2][13260:15470]
    Thr_Card_list_8 = All_Card_lists[2][15470:17680]
    Thr_Card_list_9 = All_Card_lists[2][17680:19890]
    Thr_Card_list_10 = All_Card_lists[2][19890:22100]
    
    Fou_Card_list_1 = All_Card_lists[3][0:27073]
    Fou_Card_list_2 = All_Card_lists[3][27073:54145]
    Fou_Card_list_3 = All_Card_lists[3][54145:81218]
    Fou_Card_list_4 = All_Card_lists[3][81218:108290]
    Fou_Card_list_5 = All_Card_lists[3][108290:135363]
    Fou_Card_list_6 = All_Card_lists[3][135363:162435]
    Fou_Card_list_7 = All_Card_lists[3][162435:189508]
    Fou_Card_list_8 = All_Card_lists[3][189508:216580]
    Fou_Card_list_9 = All_Card_lists[3][216580:243653]
    Fou_Card_list_10 = All_Card_lists[3][243653:270725]
    
    print(All_Card_lists[2][0])
    Three_Card_Fillout([[All_Card_lists[2][0]]])
    
    '''
    Potentially obsolete code
    
    One_Card_Dec_Writing(1,One_Card_list_1)
    One_Card_Dec_Writing(2,One_Card_list_2)
    One_Card_Dec_Writing(3,One_Card_list_3)
    One_Card_Dec_Writing(4,One_Card_list_4)
    One_Card_Dec_Writing(5,One_Card_list_5)
    One_Card_Dec_Writing(6,One_Card_list_6)
    One_Card_Dec_Writing(7,One_Card_list_7)
    One_Card_Dec_Writing(8,One_Card_list_8)
    One_Card_Dec_Writing(9,One_Card_list_9)
    One_Card_Dec_Writing(10,One_Card_list_10)

    Two_Card_Dec_Writing(1,Two_Card_list_1)
    Two_Card_Dec_Writing(2,Two_Card_list_2)
    Two_Card_Dec_Writing(3,Two_Card_list_3)
    Two_Card_Dec_Writing(4,Two_Card_list_4)
    Two_Card_Dec_Writing(5,Two_Card_list_5)
    Two_Card_Dec_Writing(6,Two_Card_list_6)
    Two_Card_Dec_Writing(7,Two_Card_list_7)
    Two_Card_Dec_Writing(8,Two_Card_list_8)
    Two_Card_Dec_Writing(9,Two_Card_list_9)
    Two_Card_Dec_Writing(10,Two_Card_list_10)
    
    Three_Card_Dec_Writing(1,Thr_Card_list_1)
    Three_Card_Dec_Writing(2,Thr_Card_list_2)
    Three_Card_Dec_Writing(3,Thr_Card_list_3)
    Three_Card_Dec_Writing(4,Thr_Card_list_4)
    Three_Card_Dec_Writing(5,Thr_Card_list_5)
    Three_Card_Dec_Writing(6,Thr_Card_list_6)
    Three_Card_Dec_Writing(7,Thr_Card_list_7)
    Three_Card_Dec_Writing(8,Thr_Card_list_8)
    Three_Card_Dec_Writing(9,Thr_Card_list_9)
    Three_Card_Dec_Writing(10,Thr_Card_list_10)
    
    Four_Card_Dec_Writing(1,Fou_Card_list_1)
    Four_Card_Dec_Writing(2,Fou_Card_list_2)
    Four_Card_Dec_Writing(3,Fou_Card_list_3)
    Four_Card_Dec_Writing(4,Fou_Card_list_4)
    Four_Card_Dec_Writing(5,Fou_Card_list_5)
    Four_Card_Dec_Writing(6,Fou_Card_list_6)
    Four_Card_Dec_Writing(7,Fou_Card_list_7)
    Four_Card_Dec_Writing(8,Fou_Card_list_8)
    Four_Card_Dec_Writing(9,Fou_Card_list_9)
    Four_Card_Dec_Writing(10,Fou_Card_list_10)
    
    Valid_Vals = Card_Valid_Func(Fou_Card_list_1[0:1])
    print(Valid_Vals)
    
    #Write the csv file
    Begin_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5','BNG_Avg']
    Final_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
    #Build the full header list
    header = Begin_header_section + Final_header_section
    file_name = '4_Card_Dec_Valid.csv'
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = header)
        writer.writeheader()
        for vv in range(len(Valid_Vals)):
            temp_list = Valid_Vals[vv]
            temp_dict = {}
            for h in range(len(header)):
                temp_dict[header[h]] = temp_list[h]
            writer.writerow(temp_dict)
    csvfile.close()
    
    #Write the data for the ZERO CARDS decision
    [Baseline_BNG,Baseline_Probabilities,Baseline_Probability_Errors] = Zero_Cards(reward_vector)
    #Write the data for the ONE CARDS decision
    Valid_Vals = Card_Valid_Func(reward_vector,One_Card_list,Fiv_Card_list)
    #Write the data for the TWO CARDS decision
    Valid_Vals = Card_Valid_Func(reward_vector,Two_Card_list,Fiv_Card_list)
    #Write the data for the THREE CARDS decision
    Valid_Vals = Card_Valid_Func(reward_vector,Thr_Card_list,Fiv_Card_list)
    #Write the data for the FOUR CARDS decision
    Valid_Vals = Card_Valid_Func(reward_vector,Fou_Card_list,Fiv_Card_list)
    
    #Write the data for the FIVE CARDS decision
    [FiC_BNGs,FiC_Probabilities,FiC_Errors] = Five_Cards(reward_vector)
    '''
    return(1)

Validate()