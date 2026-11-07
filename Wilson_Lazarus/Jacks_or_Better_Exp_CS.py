#MULTI-HAND JACKS OR BETTER
#This code is a virtual poker game called Jacks or Better that uses multiple hands
#The user is given a set amount of credits for the user
#The user inputs bets per hand
#The user inputs the total hands to bet on
#The user selects the cards to drop from the first hand
#The reward is given for the bet
#Conditionally the user continues the game starting back at bets per hand
#_________________________________________________________________________________

def Random_Cards(n):
    #Import the random library
    import random
    #Gather n unique suits and values
    hand = []
    while (len(hand) < n):
        #Call random integer for card suit
        #suit = random.randint(0,3)
        #Call random integer for card value
        #value = random.randint(1,13)
        #Identify unique card
        #card = value + (13*suit)
        card = random.randint(1,52)
        if card in hand:
            #Skip duplicate card
            continue
        else:
            #Append unique card
            hand.append(card)
    #Give the hand back to main driver
    return(hand)

def Hand_Translator(hand):
    #Initialize card lists
    disp_hand = []
    #Iterate through each card to find the identity
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
            #First suit is spades
            suit = "s"
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
        #Convert to conventioal card identification
        value = str(value)
        if (suit == 1):
            suit = "d"
        elif (suit == 2):
            suit = "c"
        elif (suit == 3):
            suit = "h"
        if (value == "11"):
            value = "J"
        elif (value == "12"):
            value = "Q"
        elif (value == "13"):
            value = "K"
        elif (value == "14"):
            value = "A"
        #Create the card
        card = value + suit
        #Append the card
        disp_hand.append(card)
    #Give disp_hand back to main driver
    return(disp_hand)

def Obtain_Vals(hand):
    #Cycle through each card to obtain values
    value_list = []
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
        #Append the value to value list
        value_list.append(value)
    return(value_list)

def Obtain_Suits(hand):
    #Initialize suit list
    suit_list = []
    #Iterate through each card to find the identity
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
            #First suit is spades
            suit = "s"
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
        #Convert to conventioal card identification
        if (suit == 1):
            suit = "d"
        elif (suit == 2):
            suit = "c"
        elif (suit == 3):
            suit = "h"
        #Append suits to suit list
        suit_list.append(suit)
    return(suit_list)

def Obtain_Vals_Suits(hand):
    #Initialize lists
    suit_list = []
    value_list = []
    #Iterate through each card to find the identity
    for i in range(len(hand)):
        #Identify the value
        if (hand[i] < 14):
            #Modulo not required for first suit
            value = int(hand[i]) + 1
            #First suit is spades
            suit = "s"
        else:
            if ((hand[i] % 13) == 0):
                #Check if the card is an Ace
                value = 14
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
            else:
                #Modulo required for all suits above the first
                value = (int(hand[i]) % 13) + 1
                #Identify the suit
                suit = (int(hand[i]) - (value - 1))/13
        #Convert to conventioal card identification
        if (suit == 1):
            suit = "d"
        elif (suit == 2):
            suit = "c"
        elif (suit == 3):
            suit = "h"
        #Append card elements to lists
        suit_list.append(suit)
        value_list.append(value)
    return(value_list,suit_list)

def Pair(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Check if the hand is a Pair
    pair = [0, " "]
    pair_list = [11,12,13,14]
    for i in range(len(pair_list)):
        if (value_list.count(pair_list[i]) > 1):
            pair = [Reward, "Pair!"]
    return(pair)

def Double_Pair(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Check if the hand is a double pair
    double_pair = [0, " "]
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) > 1):
            for j in range(len(hand)):
                if ((value_list.count(value_list[j]) > 1) and (value_list[i] != value_list[j])):
                    double_pair = [Reward, "Double_Pair!"]
    return(double_pair)

def Triple(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Check if the hand is a triple
    triple = [0, " "]
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) > 2):
            triple = [Reward, "Triple!"]
    return(triple)

def Straight(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Check if the hand is a straight
    straight = [0, " "]
    if ((max_val - min_val) == 4):
        if (value_list.count(max_val - 1) == 1):
            if (value_list.count(max_val - 2) == 1):
                if (value_list.count(max_val - 3) == 1):
                    straight = [Reward, "Straight!"]
    #Check if the hand is a steel wheel
    elif(max_val == 14):
        if (value_list.count(2) == 1):
            if (value_list.count(3) == 1):
                if (value_list.count(4) == 1):
                    if (value_list.count(5) == 1):
                        straight = [Reward, "Steel Wheel!"]
    return(straight)

def Flush(hand,Reward):
    #Convert hand into list of suits
    suit_list = Obtain_Suits(hand)
    #Check if hand is a flush
    flush = [0, " "]
    if (suit_list.count("s") == 5):
        flush = [Reward, "Flush!"]
    elif (suit_list.count("d") == 5):
        flush = [Reward, "Flush!"]
    elif (suit_list.count("c") == 5):
        flush = [Reward, "Flush!"]
    elif (suit_list.count("h") == 5):
        flush = [Reward, "Flush!"]
    return(flush)

def Full_House(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Check if the hand is a full house
    full_house = [0, " "]
    for i in range(len(value_list)):
        #Check if the hand has a triple
        if (value_list.count(value_list[i]) == 3):
            for j in range(len(value_list)):
                #Check if the hand has an additional double
                if ((value_list.count(value_list[j]) == 2) and (value_list[i] != value_list[j])):
                    full_house = [Reward, "Full House!"]
    return(full_house)

def Quad(hand,Reward):
    #Convert hand into list of values
    value_list = Obtain_Vals(hand)
    #Check if the hand is a quad
    quad = [0, " "]
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) > 3):
            quad = [Reward, "Quad!"]
    return(quad)

def Straight_Flush(hand,Reward):
    #Convert hand into list of values and list of suits
    [value_list,suit_list] = Obtain_Vals_Suits(hand)
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Check if the hand is a straight flush
    straight_flush = [0, " "]
    if ((max_val - min_val) == 4):
        if (value_list.count(max_val - 1) == 1):
            if (value_list.count(max_val - 2) == 1):
                if (value_list.count(max_val - 3) == 1):
                    #If hand is a straight check if hand is a flush
                    if (suit_list.count("s") == 5):
                        straight_flush = [Reward, "Straight Flush!"]
                    elif (suit_list.count("d") == 5):
                        straight_flush = [Reward, "Straight Flush!"]
                    elif (suit_list.count("c") == 5):
                        straight_flush = [Reward, "Straight Flush!"]
                    elif (suit_list.count("h") == 5):
                        straight_flush = [Reward, "Straight Flush!"]
    #Check if the hand is a steel wheel
    elif(max_val == 14):
        if (value_list.count(2) == 1):
            if (value_list.count(3) == 1):
                if (value_list.count(4) == 1):
                    if (value_list.count(5) == 1):
                        #If hand is a steel wheel check if hand is a flush
                        if (suit_list.count("s") == 5):
                            straight_flush = [Reward, "Steel Wheel Flush!"]
                        elif (suit_list.count("d") == 5):
                            straight_flush = [Reward, "Steel Wheel Flush!"]
                        elif (suit_list.count("c") == 5):
                            straight_flush = [Reward, "Steel Wheel Flush!"]
                        elif (suit_list.count("h") == 5):
                            straight_flush = [Reward, "Steel Wheel Flush!"]
    return(straight_flush)

def Royal_Flush(hand,Reward):
    #Convert hand into list of values and list of suits
    [value_list,suit_list] = Obtain_Vals_Suits(hand)
    #Check if the hand is a royal flush
    royal_flush = [0, " "]
    if (value_list.count(14) == 1):
        if (value_list.count(13) == 1):
            if (value_list.count(12) == 1):
                if (value_list.count(11) == 1):
                    if (value_list.count(10) == 1):
                        #If hand is a straight check if hand is a flush
                        if (suit_list.count("s") == 5):
                            royal_flush = [Reward, "Royal Flush!"]
                        elif (suit_list.count("d") == 5):
                            royal_flush = [Reward, "Royal Flush!"]
                        elif (suit_list.count("c") == 5):
                            royal_flush = [Reward, "Royal Flush!"]
                        elif (suit_list.count("h") == 5):
                            royal_flush = [Reward, "Royal Flush!"]
    return(royal_flush)

def Reward(hand,Reward_Vect):
    #Call the reward functions
    pair = Pair(hand,Reward_Vect[0])
    double_pair = Double_Pair(hand,Reward_Vect[1])
    triple = Triple(hand,Reward_Vect[2])
    straight = Straight(hand,Reward_Vect[3])
    flush = Flush(hand,Reward_Vect[4])
    full_house = Full_House(hand,Reward_Vect[5])
    quad = Quad(hand,Reward_Vect[6])
    straight_flush = Straight_Flush(hand,Reward_Vect[7])
    royal_flush = Royal_Flush(hand,Reward_Vect[8])
    reward_list_val = [pair[0],double_pair[0],triple[0],straight[0],flush[0],full_house[0],quad[0],straight_flush[0],royal_flush[0]]
    reward_list_id = [pair[1],double_pair[1],triple[1],straight[1],flush[1],full_house[1],quad[1],straight_flush[1],royal_flush[1]]
    num_reward = max(reward_list_val)
    reward_index = reward_list_val.index(num_reward)
    reward_id = reward_list_id[reward_index]
    reward = [num_reward, reward_id]
    return(reward)

def JoB_Exp(first_hand,second_hand,total_hands,Reward_Vect):
    #Import the time library
    import time
    #Establish starting credits for user
    exp_credit_start = total_hands
    exp_credits = exp_credit_start
    #Establish previous balance
    bet_net_gain = 0
    #Establish the bet per hand
    bet_per_hand = 1
    #Calculate cards to recover
    card_recover_quantity = len(first_hand)-len(second_hand)
    #Reduce user credit amount by total bet
    exp_credits = exp_credits - (bet_per_hand*total_hands)
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
    exp_reward = 0
    for j in range(total_hands):
        #Initialize individual hand reward
        temp_reward = 0
        #Collect other cards
        temp_cards = Random_Cards(card_recover_quantity)
        #Append new cards
        temp_hand = second_hand + temp_cards
        #Assign hand reward
        temp_reward = Reward(temp_hand,Reward_Vect)
        #Add hand reward to user account
        exp_reward = exp_reward + (temp_reward[0] * bet_per_hand)
        #Translate the hand into a display hand
        temp_hand = Hand_Translator(temp_hand)
        #Tally Rewards
        if (temp_reward[0] == Reward_Vect[0]):
            Pair = Pair + 1
        elif (temp_reward[0] == Reward_Vect[1]):
            DoubP = DoubP + 1
        elif (temp_reward[0] == Reward_Vect[2]):
            Trip = Trip + 1
        elif (temp_reward[0] == Reward_Vect[3]):
            Str8 = Str8 + 1
        elif (temp_reward[0] == Reward_Vect[4]):
            Floosh = Floosh + 1
        elif (temp_reward[0] == Reward_Vect[5]):
            FullH = FullH + 1
        elif (temp_reward[0] == Reward_Vect[6]):
            Quad = Quad + 1
        elif (temp_reward[0] == Reward_Vect[7]):
            Str8Fl = Str8Fl + 1
        elif (temp_reward[0] == Reward_Vect[8]):
            RoyFl = RoyFl + 1
    #Print Reward Tallies
    reward_list_str = ["ROYAL FLUSH(ES)","Straight Flush(es)","Quad(s)","Full House(s)","Flush(es)","Straight(s)","Triple(s)","Double Pair(s)","Pair(s)"]
    reward_list_num = [RoyFl,Str8Fl,Quad,FullH,Floosh,Str8,Trip,DoubP,Pair]
    print()
    for i in range(len(reward_list_str)):
        if (reward_list_num[i] == 0):
            continue
        else:
            print(str(reward_list_num[i]) +" "+ reward_list_str[i])
    #Calculate experiment net gain
    total_bet = bet_per_hand * total_hands
    bet_net_gain = exp_reward - total_bet
    return(reward_list_num,bet_net_gain)

def Vector_Stats(vector,experiments,hands_per_exp,beta_coeff):
    #Bring in square root function
    import math
    #Calculate vector average
    vector_avg = sum(vector)/len(vector)
    #Calculate the mean difference squared vector
    mds_vector = [0] * len(vector)
    for i in range(len(vector)):
        mds_vector[i] = (vector[i] - vector_avg) ** 2
    #Calculate the vector variance
    vector_var = sum(mds_vector)/len(vector)
    #Calculate the vecor standard deviation
    vector_stdev = math.sqrt(vector_var)
    #Calculate Vector error
    vector_error = (beta_coeff*vector_stdev)/math.sqrt(experiments)
    #Convert vector metrics to probabalistic values
    rel_vector_avg = round((vector_avg/hands_per_exp)*100,4)
    rel_vector_error = round((vector_error/hands_per_exp)*100,4)
    return(rel_vector_avg,rel_vector_error)

def Case_Study(first_hand,second_hand):
    #Import Time Library
    import time
    
    #Establish reward vector
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Gain converged for baseline BNG -75%
    Reward_Vect = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        Reward_Vect[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    
    #Establish experiment parameters
    #first_hand = [33,3,26,24,12]
    #second_hand = [26,24,12]
    hands_per_exp = 25000
    #List of student t distribution beta coefficient values for 95% confidence from 5 to 30
    stu_t_beta_coeff_list = [10, 10, 10, 10, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.16, 2.145, 2.131, 2.12, 2.11, 2.101, 2.093, 2.086, 2.08, 2.074, 2.069, 2.064, 2.06, 2.056, 2.052, 2.048, 2.045, 2.042]
    #Gaussian distribution beta coefficient value
    Gaussian_coeff = 2
    #Just in case reference before assignment
    beta_coeff = 10
    #Grab the start time
    start_time = time.time()
    #Initialize experiment statistical metrics
    RoyFl_num_list = []
    Str8Fl_num_list = []
    Quad_num_list = []
    FullH_num_list = []
    Floosh_num_list = []
    Str8_num_list = []
    Trip_num_list = []
    DoubP_num_list = []
    Pair_num_list = []
    BNG_list = []
    #Run experiments
    experiments = 0
    dynamic_err = 1
    dynamic_avg = 0
    while ((experiments < 5) or ((dynamic_err > 0.01*abs(dynamic_avg)) and (dynamic_err > 0.01) and (experiments < 50))):
        #Tell the researcher what experiment is being calculated
        print()
        print("Experiment: "+str(experiments+1))
        #Execute JoB_Exp function
        [reward_list_num,bet_net_gain] = JoB_Exp(first_hand,second_hand,hands_per_exp,Reward_Vect)
        RoyFl_num_list.append(reward_list_num[0])
        Str8Fl_num_list.append(reward_list_num[1])
        Quad_num_list.append(reward_list_num[2])
        FullH_num_list.append(reward_list_num[3])
        Floosh_num_list.append(reward_list_num[4])
        Str8_num_list.append(reward_list_num[5])
        Trip_num_list.append(reward_list_num[6])
        DoubP_num_list.append(reward_list_num[7])
        Pair_num_list.append(reward_list_num[8])
        BNG_list.append(bet_net_gain)
        #Establish the beta coefficient
        if (experiments < 30):
            beta_coeff = stu_t_beta_coeff_list[experiments]
        else:
            beta_coeff = Gaussian_coeff
        #Increment the experiment count
        experiments = experiments + 1
        #Calculate experimental Bet Net Gain statistics
        [rel_BNG_avg,rel_BNG_error] = Vector_Stats(BNG_list,experiments,hands_per_exp,beta_coeff)
        #Set the dynamic values
        dynamic_err = rel_BNG_error
        print(dynamic_err)
        dynamic_avg = rel_BNG_avg
        print(dynamic_avg)
    print()
    #Print vectors for additional post processing
    for j in range(experiments):
        print(RoyFl_num_list[j],Str8Fl_num_list[j],Quad_num_list[j],FullH_num_list[j],Floosh_num_list[j],Str8_num_list[j],Trip_num_list[j],DoubP_num_list[j],Pair_num_list[j],round(BNG_list[j],2))
    print()
    #Print all real valued measurements
    if sum(RoyFl_num_list) > 0:
        #Calculate experimental Royal Flush statistics
        [rel_RoyFl_avg,rel_RoyFl_error] = Vector_Stats(RoyFl_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Royal Flush measurement statement
        print("A Royal Flush will occur "+str(rel_RoyFl_avg)+"% +/- "+str(rel_RoyFl_error)+"% of the time")
    if sum(Str8Fl_num_list) > 0:
        #Calculate experimental Straight Flush statistics
        [rel_Str8Fl_avg,rel_Str8Fl_error] = Vector_Stats(Str8Fl_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Straight Flush measurement statement
        print("A Straight Flush will occur "+str(rel_Str8Fl_avg)+"% +/- "+str(rel_Str8Fl_error)+"% of the time")
    if sum(Quad_num_list) > 0:
        #Calculate experimental Quadruple statistics
        [rel_Quad_avg,rel_Quad_error] = Vector_Stats(Quad_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Quadruple measurement statement
        print("A Quad will occur "+str(rel_Quad_avg)+"% +/- "+str(rel_Quad_error)+"% of the time")
    if sum(FullH_num_list) > 0:
        #Calculate experimental Full House statistics
        [rel_FullH_avg,rel_FullH_error] = Vector_Stats(FullH_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Full House measurement statement
        print("A Full House will occur "+str(rel_FullH_avg)+"% +/- "+str(rel_FullH_error)+"% of the time")
    if sum(Floosh_num_list) > 0:
        #Calculate experimental Flush statistics
        [rel_Floosh_avg,rel_Floosh_error] = Vector_Stats(Floosh_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Flush measurement statement
        print("A Flush will occur "+str(rel_Floosh_avg)+"% +/- "+str(rel_Floosh_error)+"% of the time")
    if sum(Str8_num_list) > 0:
        #Calculate experimental Straight statistics
        [rel_Str8_avg,rel_Str8_error] = Vector_Stats(Str8_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Straight measurement statement
        print("A Straight will occur "+str(rel_Str8_avg)+"% +/- "+str(rel_Str8_error)+"% of the time")
    if sum(Trip_num_list) > 0:
        #Calculate experimental Triple statistics
        [rel_Trip_avg,rel_Trip_error] = Vector_Stats(Trip_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Triple measurement statement
        print("A Triple will occur "+str(rel_Trip_avg)+"% +/- "+str(rel_Trip_error)+"% of the time")
    if sum(DoubP_num_list) > 0:
        #Calculate experimental Double Pair statistics
        [rel_DoubP_avg,rel_DoubP_error] = Vector_Stats(DoubP_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Double Pair measurement statement
        print("A Double Pair will occur "+str(rel_DoubP_avg)+"% +/- "+str(rel_DoubP_error)+"% of the time")
    if sum(Pair_num_list) > 0:
        #Calculate experimental Pair statistics
        [rel_Pair_avg,rel_Pair_error] = Vector_Stats(Pair_num_list,experiments,hands_per_exp,beta_coeff)
        #Print Pair measurement statement
        print("A Pair will occur "+str(rel_Pair_avg)+"% +/- "+str(rel_Pair_error)+"% of the time")
    #Calculate experimental Bet Net Gain statistics
    [rel_BNG_avg,rel_BNG_error] = Vector_Stats(BNG_list,experiments,hands_per_exp,beta_coeff)
    #Print Bet Net Gain measurement statement
    print("The Bet Net Gain will be "+str(rel_BNG_avg)+"% +/- "+str(rel_BNG_error)+"% with 95% confidence")
    print()
    print("All measurements were made with 95% confidence assuming a Gaussian distribution with "+str(experiments)+" experiments and "+str(hands_per_exp)+" hands per experiment")
    #Print time elapsed
    print("--- %s seconds ---" % (time.time() - start_time))
    #return(rel_BNG_avg,rel_BNG_error)

Case_Study([1,2,3,4,5],[])
