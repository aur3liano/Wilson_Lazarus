#WILSON-LAZARUS
#This code is a multi layer feed forward neural network designed to learn how to play Multi-Hand Jacks or Better
#WL will be trained on the game until the set of priority coefficients converges
#_______________________________________________________________________________________________________________

#NODE Drop Card Compile
def Drop_Card_Compile(Drop_Card_Master_List):
    #Access random library
    import random
    #Iterate through each drop card list in the master drop card list
    Uni_drop_list = []
    for i in range(len(Drop_Card_Master_List)):
        #Acquire current drop list
        drop_list = Drop_Card_Master_List[i]
        for j in range(len(drop_list)):
            #Determine if card is unique
            if (drop_list[j] not in Uni_drop_list):
                #If card is unique add to list
                Uni_drop_list.append(drop_list[j])
    #Initialize the unique card dictionary
    Uni_drop_dict = {}
    #Iterate through each unique card in the dictionary
    for k in range(len(Uni_drop_list)):
        #Specify the current card
        uni_card = Uni_drop_list[k]
        counter = 0;
        #Add each total occurence of the current card in each sub list
        for m in range(len(Drop_Card_Master_List)):
            counter = counter + Drop_Card_Master_List[m].count(uni_card)
        #Make a new entry in the dictionary
        Uni_drop_dict[uni_card] = counter
    #Find the max card occurence
    if (Uni_drop_dict != {}):
        max_count = max(Uni_drop_dict.values())
        #Normalize dictionary values with respect to max_count
        for n in range(len(Uni_drop_list)):
            Uni_drop_dict[Uni_drop_list[n]] = Uni_drop_dict[Uni_drop_list[n]]/max_count
        #Iterate through all unique drop cards to build the final drop card list
        final_drop_list = []
        for n in range(len(Uni_drop_list)):
            #Set random flag
            RF = random.random()
            #Get current flag probability
            card_prob = Uni_drop_dict[Uni_drop_list[n]]
            #Test each card
            if (card_prob > RF):
                final_drop_list.append(Uni_drop_list[n])
    else:
        final_drop_list = []
    return(final_drop_list)

#NODE 111
def JoB_Pair_Exists(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no pair make no recommendation
    W111_drop_card = []
    #Establish list of acceptable pairs
    pair_list = [11,12,13,14]
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of the pair
    pair_value = 0
    for i in range(len(pair_list)):
        if (value_list.count(pair_list[i]) == 2):
            pair_value = pair_list[i]
    if (pair_value != 0):
        #Build the drop card list of values that are not the pair value
        for j in range(len(hand)):
            if (value_list[j] != pair_value):
                W111_drop_card.append(hand[j])
    return(W111_drop_card)

#NODE 112
def JoB_Pair_Potential(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Establish list of acceptable pairs
    pair_list = [11,12,13,14]
    #If no pair make no recommendation
    W112_drop_card = []
    #Check if the hand has a value of jacks or better
    pair_value = 0
    for i in range(len(value_list)):
        if (value_list[i] in pair_list):
            pair_value = hand[i]
    if (pair_value != 0):
        #Build the drop card list of values that are not the pair value
        for j in range(len(hand)):
            if (hand[j] != pair_value):
                W112_drop_card.append(hand[j])
    return(W112_drop_card)

#NODE 11
def Pair_Deci_Strat(hand):
    #Call the centi-strategy nodes
    W111_drop_card = JoB_Pair_Exists(hand)
    W112_drop_card = JoB_Pair_Potential(hand)
    #Test NODE 113 implementation
    if (W111_drop_card == []) and (W112_drop_card == []):
        W11_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W111_drop_card,W112_drop_card]
        W11_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W11_drop_card)

#NODE 121
def Double_Pair_Exists(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no double pair make no recommendation
    W121_drop_card = []
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of each pair
    value_1 = 0
    value_2 = 0
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) == 2):
            value_1 = value_list[i]
            for j in range(len(hand)):
                if ((value_list.count(value_list[j]) == 2) and (value_list[i] != value_list[j])):
                    value_2 = value_list[j]
    if (value_1 != 0) and (value_2 != 0):
        #Build the drop card list of values that are not the pair values
        for k in range(len(value_list)):
            if (value_list[k] != value_1) and (value_list[k] != value_2):
                W121_drop_card.append(hand[k])
    return(W121_drop_card)

#NODE 122 and NODE 132 and NODE 143
def Double_Pair_Potential(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no double pair potential make no recommendation
    W122_drop_card = []
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of a pair
    pair = 0
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) == 2):
            pair = value_list[i]
    if (pair != 0):
        #Build the drop card list of values that are not the pair value
        for j in range(len(value_list)):
            if (value_list[j] != pair):
                W122_drop_card.append(hand[j])
    return(W122_drop_card)

#NODE 12
def Double_Pair_Deci_Strat(hand):
    #Call the centi-strategy nodes
    W121_drop_card = Double_Pair_Exists(hand)
    W122_drop_card = Double_Pair_Potential(hand)
    #Test NODE 123 implementation
    if (W121_drop_card == []) and (W122_drop_card == []):
        W12_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W121_drop_card,W122_drop_card]
        W12_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W12_drop_card)

#NODE 131 and NODE 142 and NODE 152
def Triple_Exists(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no double pair potential make no recommendation
    W131_drop_card = []
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of the triple
    trip = 0
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) == 3):
            trip = value_list[i]
    #Check if the triple exists
    if (trip != 0):
        #Build the drop card list of values that are not the pair value
        for j in range(len(value_list)):
            if (value_list[j] != trip):
                W131_drop_card.append(hand[j])
    return(W131_drop_card)

#NODE 13
def Triple_Deci_Strat(hand):
    #Call the centi-strategy nodes
    W131_drop_card = Triple_Exists(hand)
    #Double_Pair_Potential is the same as Triple_Potential
    W132_drop_card = Double_Pair_Potential(hand)
    #Test NODE 133 implementation
    if (W131_drop_card == []) and (W132_drop_card == []):
        W13_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W131_drop_card,W132_drop_card]
        W13_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W13_drop_card)

#NODE 141
def Quad_Exists(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no double pair potential make no recommendation
    W141_drop_card = []
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of the triple
    quad = 0
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) == 4):
            quad = value_list[i]
    #Check if the triple exists
    if (quad != 0):
        #Build the drop card list of values that are not the pair value
        for j in range(len(value_list)):
            if (value_list[j] != quad):
                W141_drop_card.append(hand[j])
    return(W141_drop_card)

#NODE 14
def Quad_Deci_Strat(hand):
    #Call the centi-strategy nodes
    W141_drop_card = Quad_Exists(hand)
    #Triple_Exists is the same as Quad_H_Potential
    W142_drop_card = Triple_Exists(hand)
    #Double_Pair_Potential is the same as Quad_L_Potential
    W143_drop_card = Double_Pair_Potential(hand)
    #Test NODE 144 implementation
    if (W141_drop_card == []) and (W142_drop_card == []) and (W143_drop_card == []):
        W14_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W141_drop_card,W142_drop_card,W143_drop_card]
        W14_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W14_drop_card)

#NODE 151
def Full_House_Exists(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no double pair make no recommendation
    W151_drop_card = []
    #Convert hand into a list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find the value of each pair
    value_1 = 0
    value_2 = 0
    for i in range(len(value_list)):
        if (value_list.count(value_list[i]) == 3):
            value_1 = value_list[i]
            for j in range(len(hand)):
                if ((value_list.count(value_list[j]) == 2) and (value_list[i] != value_list[j])):
                    value_2 = value_list[j]
    if (value_1 != 0) and (value_2 != 0):
        #Build the drop card list of values that are not the pair values
        for k in range(len(value_list)):
            if (value_list[k] != value_1) and (value_list[k] != value_2):
                W151_drop_card.append(hand[k])
    return(W151_drop_card)

#NODE 15
def Full_House_Deci_Strat(hand):
    #Call the centi-strategy nodes
    W151_drop_card = Full_House_Exists(hand)
    #Triple_Exists is the same as Full_House_H_Potential
    W152_drop_card = Triple_Exists(hand)
    #Double_Pair_Exists is the same as Full_House_M_Potential
    W153_drop_card = Double_Pair_Exists(hand)
    #Double_Pair_Potential is the same as Full_House_L_Potential
    W154_drop_card = Double_Pair_Potential(hand)
    #Test NODE 155 implementation
    if (W151_drop_card == []) and (W152_drop_card == []) and (W153_drop_card == []) and (W154_drop_card == []):
        W15_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W151_drop_card,W152_drop_card,W153_drop_card,W154_drop_card]
        W15_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W15_drop_card)

#NODE 1
def Card_Repetition(hand):
    #Call the deci-strategy nodes
    W11_drop_card = Pair_Deci_Strat(hand)
    W12_drop_card = Double_Pair_Deci_Strat(hand)
    W13_drop_card = Triple_Deci_Strat(hand)
    W14_drop_card = Quad_Deci_Strat(hand)
    W15_drop_card = Full_House_Deci_Strat(hand)
    #Test NODE 16 implementation
    if (W11_drop_card == []) and (W12_drop_card == []) and (W13_drop_card == []) and (W14_drop_card == []) and (W15_drop_card):
        W1_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W11_drop_card,W12_drop_card,W13_drop_card,W14_drop_card,W15_drop_card]
        W1_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W1_drop_card)

#NODE 21
def Two_Str8_Cards(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #Convert hand into list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Implement the four test method to find two cards with straight potential
    value_1 = 0
    value_2 = 0
    #Max straight range
    for i in range(4):
        if (value_list.count(max_val - i) == 1):
            value_1 = max_val
            value_2 = max_val - i
    for j in range(4):
        if (value_list.count(min_val + j) == 1):
            value_1 = min_val + j
            value_2 = min_val
    #Initialize the str8_couple
    str8_couple = []
    if (value_1 != 0) and (value_2 != 0):
        str8_couple = [value_1,value_2]
    else:
        #Make a new list of cards without the previous straight limits
        new_three = []
        for k in range(len(value_list)):
            if (value_list[k] != max_val) and (value_list[k] != min_val):
                new_three.append(hand[k])
        #Obtain

#NODE 2
def Straight_Cards(hand):
    #Call the deci-strategy nodes
    W21_drop_card = Two_Str8_Cards(hand)
    #Test NODE 25 implementation
    if (W21_drop_card == []):
        W2_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W21_drop_card]
        W2_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W2_drop_card)

#Neural Network
def Drop_Card_Neural_Network(hand):
    #Call the macro-strategy nodes
    W1_drop_card = Card_Repetition(hand)
    #W2_drop_card = Straight_Cards(hand)

    #Compile drop card lists
    #Drop_Card_Master_List = [W1_drop_card,W2_drop_card]
    Drop_Card_Master_List = [W1_drop_card]
    Drop_Card = Drop_Card_Compile(Drop_Card_Master_List)
    #Final check to make sure a recommendation is made
    if (Drop_Card == []):
        Drop_Card = hand
    return(Drop_Card)

def Wilson_Lazarus():
    #Establish reward vector
    Reward_Vect_Baseline = [3.25,8.89,20,107.67,215,293.33,1760,30506.67,274560]
    Reward_Vect_Gain = 0.065735472679572
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = (Reward_Vect_Baseline[rv] * Reward_Vect_Gain)
    #Access Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Import time library
    import time
    #Establish starting credits
    credit_start = 5000
    WL_credits = credit_start
    total_reward = 0
    #Establish total hand reward counts
    RoyFl_tot = 0
    Str8Fl_tot = 0
    Quad_tot = 0
    FullH_tot = 0
    Floosh_tot = 0
    Str8_tot = 0
    Trip_tot = 0
    DoubP_tot = 0
    Pair_tot = 0
    #Establish previous balance
    bet_net_gain = 0
    start_time = time.time()
    while (WL_credits > 1):
        #Print previous balance
        prev_bal = WL_credits - bet_net_gain
        print("Previous Balance = " + str(prev_bal))
        #Print current balance
        print("Current Balance = " + str(WL_credits))
        #Establish training flag
        '''
        train = "no"
        if (train == "yes"):
            WL_credits = credit_start
        else:
        '''
        #Establish bet parameters
        bet_per_hand = 1
        if (WL_credits > (credit_start/100)):
            total_hands = int(credit_start/100)
        else:
            total_hands = int(WL_credits)
        #Summon a random hand
#Debugging
        first_hand = Jacks_or_Better_4WL.Random_Cards(5)
#        first_hand = [3,16,11,24,32]
#
        #Translate the first hand
        disp_first_hand = Jacks_or_Better_4WL.Hand_Translator(first_hand)
        #Print the first hand
        print(disp_first_hand)
        #Send the first hand to the 'centi' nodes
        Drop_Card = Drop_Card_Neural_Network(first_hand)
        #Build the second hand
        second_hand = []
        for i in range(len(first_hand)):
            #Drop the cards in the Drop Card list
            if (first_hand[i] not in Drop_Card):
                second_hand.append(first_hand[i])
        #Calculate cards to recover
        card_recover_quantity = len(first_hand)-len(second_hand)
        #Reduce Wilson-Lazarus credit amount by total bet
        WL_credits = WL_credits - (bet_per_hand*total_hands)
        #Wait for human audience
#        time.sleep(1.5)
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
            #Translate the hand into a display hand
            temp_hand = Jacks_or_Better_4WL.Hand_Translator(temp_hand)
            #Print the display hand and reward
            '''
            print(temp_hand, end="")
            print(" " + temp_reward[1])
            '''
            #Tally Rewards
            if (temp_reward[0] == 1):
                Pair = Pair + 1
            elif (temp_reward[0] == 2):
                DoubP = DoubP + 1
            elif (temp_reward[0] == 3):
                Trip = Trip + 1
            elif (temp_reward[0] == 4):
                Str8 = Str8 + 1
            elif (temp_reward[0] == 6):
                Floosh = Floosh + 1
            elif (temp_reward[0] == 9):
                FullH = FullH + 1
            elif (temp_reward[0] == 25):
                Quad = Quad + 1
            elif (temp_reward[0] == 50):
                Str8Fl = Str8Fl + 1
            elif (temp_reward[0] == 250):
                RoyFl = RoyFl + 1
        #Print Reward Tallies
        reward_list_str = ["ROYAL FLUSH(ES)","Straight Flush(es)","Quad(s)","Full House(s)","Flush(es)","Straight(s)","Triple(s)","Double Pair(s)","Pair(s)"]
        reward_list_num = [RoyFl,Str8Fl,Quad,FullH,Floosh,Str8,Trip,DoubP,Pair]
        print()
        for i in range(len(reward_list_str)):
            if (reward_list_num[i] == 0):
                continue
            else:
                print(str(reward_list_num[i]) + " " + reward_list_str[i])
        #Print total hands
        print("Total Hands = " + str(total_hands))
        #Print total bet
        total_bet = bet_per_hand * total_hands
        print("Total Bet = " + str(total_bet))
        #Print total bet reward
        print("Bet Reward = " + str(WL_reward))
        #Print bet gain
        bet_net_gain = round((WL_reward - total_bet),2)
        print("Net Gain = " + str(bet_net_gain))
        print()
        #Calculate Wilson-Lazarus balance
        WL_credits = round((WL_credits + WL_reward),2)
        #Track total earnings
        total_reward = round((total_reward + WL_reward),2)
        #Track total reward counts
        RoyFl_tot = RoyFl_tot + RoyFl
        Str8Fl_tot = Str8Fl_tot + Str8Fl
        Quad_tot = Quad_tot + Quad
        FullH_tot = FullH_tot + FullH
        Floosh_tot = Floosh_tot + Floosh
        Str8_tot = Str8_tot + Str8
        Trip_tot = Trip_tot + Trip
        DoubP_tot = DoubP_tot + DoubP
        Pair_tot = Pair_tot + Pair
    reward_list_num_tot = [RoyFl_tot,Str8Fl_tot,Quad_tot,FullH_tot,Floosh_tot,Str8_tot,Trip_tot,DoubP_tot,Pair_tot]
    #Print total earnings
    print("Total Earnings = " + str(total_reward) + "!")
    #Calculate all hands
    all_hands = credit_start + total_reward
    #Print the total reward percentages
    for i in range(len(reward_list_str)):
        if (reward_list_num_tot[i] == 0):
            continue
        else:
            print(str((reward_list_num_tot[i]/all_hands)*100) + "%" + " " + reward_list_str[i])
    print()
    #Notify user game is over
    print("Game Over")
    #Print rate and time elapsed
    print()
    print("--- %s seconds ---" % (time.time() - start_time))
    print()
    print("---" + " " + str(round((all_hands/(time.time() - start_time)),2)) + " hands/second " + "---")
    time.sleep(20)

Wilson_Lazarus()
