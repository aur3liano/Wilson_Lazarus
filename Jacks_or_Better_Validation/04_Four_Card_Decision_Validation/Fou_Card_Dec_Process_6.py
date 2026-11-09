# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:28:11 2021

@author: Justin Paul
"""

'''
def test_func(i):
    if (i%2==0):
        oper = (i-1)*(i+1)
    else:
        oper = i*i
    print(oper)
    return(oper)

def validate():
    import multiprocessing as mlpr
    import time
    
    par_time_start = time.time()
    for i in range(mlpr.cpu_count()):
        p_test = mlpr.Process(target=test_func, args=(i,))
        p_test.start()
        p_test.join()
    par_time_end = time.time() - par_time_start
    print('Parallel time: ',str(round(par_time_end,3)))
    print()

    ser_time_start = time.time()
    for i in range(mlpr.cpu_count()):
        oper = test_func(i)
    ser_time_end = time.time() - ser_time_start
    print('Serial time: ',str(round(ser_time_end,3)))
    return(1)

validate()
'''

def Card_Valid_Func(i):
    #Import libraries
    import time
    import csv
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
    
    #Read in the card list file
    card_list_file_nm = 'Fou_Card_Decs_' + str(i) + '.txt'
    card_list_file_obj = open(card_list_file_nm,'r')
    Card_list_raw = card_list_file_obj.readlines()
    #Process the raw card list
    Card_list = []
    for crd_lst in range(len(Card_list_raw)):
        cards = Card_list_raw[crd_lst]
        cards = cards.strip()
        cards_str = cards.split(" ")
        cards_num = []
        for cs in range(len(cards_str)):
            crd_num = int(cards_str[cs])
            cards_num.append(crd_num)
        Card_list.append(cards_num)
    card_list_file_obj.close()
    
    #Open the log file
    log_file_nm = 'Fou_Card_Decs_' + str(i) + '_logfile' + '.txt'
    log_file_obj = open(log_file_nm,'a')
    
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
            time_elsd = round(time_print/60,3)
            progress_string = 'Progress: ' + str(prog_calc) + ' % at time: ' + str(time_elsd) + ' minutes\n'
            log_file_obj.write(progress_string)
            print('Time Elapsed:',str(round(time_print/60,3)),' minutes')
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
    log_file_obj.close()
        
    #Write the csv file
    Begin_header_section = ['Card_1','Card_2','Card_3','Card_4','Card_5','BNG_Avg']
    Final_header_section = ['Pair_Avg','Two_Pair_Avg','Triple_Avg','Straight_Avg','Flush_Avg','Full_House_Avg','Quad_Avg','Straight_Flush_Avg','Royal_Flush_Avg']
    #Build the full header list
    header = Begin_header_section + Final_header_section
    file_name = '4_Card_Dec_Valid_' + str(i) + '.csv'
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
    return(Valid_Vals)

Card_Valid_Func(6)

'''
if __name__ == "__main__":
    import multiprocessing as mlpr
    import time
    
    #Create a queue
    q = mlpr.Queue()
    
    time_start = time.time()
    for i in range(1):
        p_test = mlpr.Process(target=Card_Valid_Func, args=(i,q,))
        p_test.start()
        p_test.join()
    time_end = time.time() - time_start
    print('Time Elapsed: ',str(round(time_end,3)))
    
    print(q.get())
'''