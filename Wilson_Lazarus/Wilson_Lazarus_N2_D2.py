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

#NODE 21
def Two_Str8_Cards(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #Convert hand into list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #If no straight cards make no recommendation
    W21_drop_card = []
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Build of list of unique straight values
    str8_vals = []
    #Test minimum values first to prioritize maximum values
    for i in range(4):
        #Test if str8_vals has the correct card quantity
        if (len(str8_vals) < 2):
            #Crit values in Min straight range
            crit_val = (min_val+1) + i
            if (crit_val in value_list):
                str8_vals.append(hand[value_list.index(crit_val)])
                str8_vals.append(hand[value_list.index(min_val)])
    #Test if str8_vals has the correct card quantity
    if (len(str8_vals) < 2):
        for j in range(4):
            #Test if str8_vals has the correct card quantity
            if (len(str8_vals) < 2):
                #Crit values in Max straight range
                crit_val = (max_val-1) - j
                if (crit_val in value_list):
                    str8_vals.append(hand[value_list.index(max_val)])
                    str8_vals.append(hand[value_list.index(crit_val)])
    #Test if str8_vals is empty
    if (len(str8_vals) < 2):
        #Make a new list of cards without the previous straight limits
        new_three = []
        for k in range(len(value_list)):
            if ((value_list[k] != max_val) and (value_list[k] != min_val)):
                new_three.append(hand[k])
        #Check if new_three is empty
        if (new_three != []):
            #Obtain new value list for new_three
            NT_value_list = Jacks_or_Better_4WL.Obtain_Vals(new_three)
            #Find straight limits
            NT_max_val = max(NT_value_list)
            NT_min_val = min(NT_value_list)
            #Test minimum values first to prioritize maximum values
            for m in range(4):
                #Test if str8_vals has the correct card quantity
                if (len(str8_vals) < 2):
                    #Crit values in NT Min straight range
                    crit_val = (NT_min_val+1) + m
                    if (crit_val in NT_value_list):
                        str8_vals.append(hand[value_list.index(crit_val)])
                        str8_vals.append(hand[value_list.index(NT_min_val)])
            #Test if str8_vals has the correct card quantity
            if (len(str8_vals) < 2):
                for n in range(4):
                    #Test if str8_vals has the correct card quantity
                    if (len(str8_vals) < 2):
                        #Crit values in NT Max straight range
                        crit_val = (NT_max_val-1) - n
                        if (crit_val in NT_value_list):
                            str8_vals.append(hand[value_list.index(NT_max_val)])
                            str8_vals.append(hand[value_list.index(crit_val)])
    #Final check if str8_vals were found
    if (len(str8_vals) == 2):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] not in str8_vals):
                W21_drop_card.append(hand[o])
    return(W21_drop_card)

#NODE 22
def Thr_Str8_Cards(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #Convert hand into list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #If no straight cards make no recommendation
    W22_drop_card = []
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Build of list of unique straight values
    str8_vals = []
    #Test minimum values first to prioritize maximum values
    for i in range(4):
        #Test if str8_vals has the correct card quantity
        if (len(str8_vals) < 3):
            #Crit values in Min straight range
            crit_val = (min_val+1) + i
            if (crit_val in value_list):
                #Set the first values of the straight cards
                value_1 = crit_val
                value_2 = min_val
                str8_vals.append(hand[value_list.index(crit_val)])
                str8_vals.append(hand[value_list.index(min_val)])
                for i2 in range(4):
                    #Second Crit values in Min straight range
                    crit_val_2 = (min_val+1) + i2
                    if (crit_val_2 in value_list) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                        str8_vals.append(hand[value_list.index(crit_val_2)])
    #Test if str8_vals has the correct card quantity
    if (len(str8_vals) < 3):
        #Reset list of unique straight values
        str8_vals = []
        for j in range(4):
            #Test if str8_three has the correct card quantity
            if (len(str8_vals) < 3):
                #Crit values in Max straight range
                crit_val = (max_val-1) - j
                if (crit_val in value_list):
                    #Set the first values of the straight cards
                    value_1 = crit_val
                    value_2 = max_val
                    str8_vals.append(hand[value_list.index(crit_val)])
                    str8_vals.append(hand[value_list.index(max_val)])
                    for j2 in range(4):
                        #Second Crit values in Max straight range
                        crit_val_2 = (max_val-1) - j2
                        if (crit_val_2 in value_list) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                            str8_vals.append(hand[value_list.index(crit_val_2)])
    #Test if str8_vals has the correct card quantity
    if (len(str8_vals) < 3):
        #Make a new list of cards without the previous straight limits
        new_three = []
        for k in range(len(value_list)):
            if (value_list[k] != max_val) and (value_list[k] != min_val):
                new_three.append(hand[k])
        #Check if new_three is empty
        if (new_three != []):
            #Obtain new value list for new_three
            NT_value_list = Jacks_or_Better_4WL.Obtain_Vals(new_three)
            #Find straight limits
            NT_max_val = max(NT_value_list)
            NT_min_val = min(NT_value_list)
            #Reset list of unique straight values
            str8_vals = []
            #Test minimum values first to prioritize maximum values
            for n in range(4):
                #Test if str8_vals has the correct card quantity
                if (len(str8_vals) < 3):
                    #Crit values in NT Min straight range
                    crit_val = (NT_min_val+1) + n
                    if (crit_val in NT_value_list):
                        #Set the first values of the straight cards
                        NT_value_1 = crit_val
                        NT_value_2 = NT_min_val
                        str8_vals.append(hand[NT_value_list.index(crit_val)])
                        str8_vals.append(hand[NT_value_list.index(NT_min_val)])
                        for n2 in range(4):
                            #Second Crit values in NT Min straight range
                            crit_val_2 = (NT_min_val+1) + n2
                            if (crit_val_2 in NT_value_list) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                                str8_vals.append(hand[NT_value_list.index(crit_val_2)])
            #Test if str8_vals has the correct card quantity
            if (len(str8_vals) < 3):
                #Reset list of unique straight values
                str8_vals = []
                for m in range(4):
                    #Test if str8_vals has the correct card quantity
                    if (len(str8_vals) < 3):
                        #Crit values in NT Max straight range
                        crit_val = (NT_max_val-1) - m
                        if (crit_val in NT_value_list):
                            #Set the first values of the straight cards
                            NT_value_1 = crit_val
                            NT_value_2 = NT_max_val
                            str8_vals.append(hand[NT_value_list.index(crit_val)])
                            str8_vals.append(hand[NT_value_list.index(NT_max_val)])
                            for m2 in range(4):
                                #Second Crit values in NT Max straight range
                                crit_val_2 = (NT_max_val-1) - m2
                                if (crit_val_2 in NT_value_list) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                                    str8_vals.append(hand[NT_value_list.index(crit_val_2)])
    #Final check if str8_vals were found
    if (len(str8_vals) == 3):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] not in str8_vals):
                W22_drop_card.append(hand[o])
    return(W22_drop_card)

#NODE 23
def For_Str8_Cards(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #Convert hand into list of values
    value_list = Jacks_or_Better_4WL.Obtain_Vals(hand)
    #If no straight cards make no recommendation
    W23_drop_card = []
    #Find straight limits
    max_val = max(value_list)
    min_val = min(value_list)
    #Build of list of unique straight values
    str8_vals = []
    #Test minimum values first to prioritize maximum values
    for i in range(4):
        #Test if str8_three has the correct card quantity
        if (len(str8_vals) < 4):
            #Crit values in Min straight range
            crit_val = (min_val+1) + i
            if (crit_val in value_list):
                #Set the first values of the straight cards
                value_1 = min_val
                value_2 = crit_val
                str8_vals.append(hand[value_list.index(crit_val)])
                str8_vals.append(hand[value_list.index(min_val)])
                for i2 in range(4):
                    #Second Crit values in Min straight range
                    crit_val_2 = (min_val+1) + i2
                    if (crit_val_2 in value_list) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                        #Set the third value of the straight cards
                        value_3 = crit_val_2
                        str8_vals.append(hand[value_list.index(crit_val_2)])
                        for i3 in range(4):
                            #Third Crit values in Min straight range
                            crit_val_3 = (min_val+1) + i3
                            if (crit_val_3 in value_list) and (crit_val_3 != value_1) and (crit_val_3 != value_2) and (crit_val_3 != value_3):
                                str8_vals.append(hand[value_list.index(crit_val_3)])
    #Test if str8_vals has the correct card quantity
    if (len(str8_vals) < 4):
        #Reset list of unique straight values
        str8_vals = []
        for j in range(4):
	    #Test if str8_vals has the correct card quantity
            if (len(str8_vals) < 4):
                #Crit values in Max straight range
                crit_val = (max_val-1) - j
                if (crit_val in value_list):
                    #Set the first values of the straight cards
                    value_1 = crit_val
                    value_2 = max_val
                    str8_vals.append(hand[value_list.index(crit_val)])
                    str8_vals.append(hand[value_list.index(max_val)])
                    for j2 in range(4):
                        #Second Crit values in Max straight range
                        crit_val_2 = (max_val-1) - j2
                        if (crit_val_2 in value_list) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                            #Set the third value of the straight cards
                            value_3 = crit_val_2
                            str8_vals.append(hand[value_list.index(crit_val_2)])
                            for j3 in range(4):
                                #Third Crit values in Max straight range
                                crit_val_3 = (max_val-1) - j3
                                if (crit_val_3 in value_list) and (crit_val_3 != value_1) and (crit_val_3 != value_2) and (crit_val_3 != value_3):
                                    str8_vals.append(hand[value_list.index(crit_val_3)])
    #Test if str8_three has the correct card quantity
    if (len(str8_vals) < 4):
        #Make a new list of cards without the previous straight limits
        new_three = []
        for k in range(len(value_list)):
            if (value_list[k] != max_val) and (value_list[k] != min_val):
                new_three.append(hand[k])
        #Check if new_three is empty
        if (new_three != []):
            #Obtain new value list for new_three
            NT_value_list = Jacks_or_Better_4WL.Obtain_Vals(new_three)
            #Find straight limits
            NT_max_val = max(NT_value_list)
            NT_min_val = min(NT_value_list)
            #Reset list of unique straight values
            str8_vals = []
            #Test minimum values first to prioritize maximum values
            for n in range(4):
                #Test if str8_three has the correct card quantity
                if (len(str8_vals) < 4):
                    #Crit values in NT Min straight range
                    crit_val = (NT_min_val+1) + n
                    if (crit_val in NT_value_list):
                        #Set the first values of the straight cards
                        NT_value_1 = crit_val
                        NT_value_2 = NT_min_val
                        str8_vals.append(hand[NT_value_list.index(crit_val)])
                        str8_vals.append(hand[NT_value_list.index(NT_min_val)])
                        for n2 in range(4):
                            #Second Crit values in NT Min straight range
                            crit_val_2 = (NT_min_val+1) + n2
                            if (crit_val_2 in NT_value_list) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                                #Set the third value of the straight cards
                                NT_value_3 = crit_val_2
                                str8_vals.append(hand[NT_value_list.index(crit_val_2)])
                                for n3 in range(4):
                                    #Third Crit values in NT Min straight range
                                    crit_val_3 = (NT_max_val+1) + n3
                                    if (crit_val_3 in NT_value_list) and (crit_val_3 != NT_value_1) and (crit_val_3 != NT_value_2) and (crit_val_3 != NT_value_3):
                                        str8_vals.append(hand[NT_value_list.index(crit_val_3)])
            #Test if str8_vals has the correct card quantity
            if (len(str8_vals) < 4):
                #Reset list of unique straight values
                str8_vals = []
                #NT Max straight range
                for m in range(4):
                    #Crit values in NT Max straight range
                    crit_val = (NT_max_val-1) - m
                    if (crit_val in NT_value_list):
                        NT_value_1 = crit_val
                        NT_value_2 = NT_max_val
                        str8_vals.append(hand[NT_value_list.index(crit_val)])
                        str8_vals.append(hand[NT_value_list.index(NT_max_val)])
                        for m2 in range(4):
                            #Second Crit values in NT Max straight range
                            crit_val_2 = (NT_max_val-1) - m2
                            if (crit_val_2 in NT_value_list) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                                #Set the third value of the straight cards
                                NT_value_3 = crit_val_2
                                str8_vals.append(hand[NT_value_list.index(crit_val_2)])
                                for n3 in range(4):
                                    #Third Crit values in NT Max straight range
                                    crit_val_3 = (NT_max_val-1) - m3
                                    if (crit_val_3 in NT_value_list) and (crit_val_3 != NT_value_1) and (crit_val_3 != NT_value_2) and (crit_val_3 != NT_value_3):
                                        str8_vals.append(hand[NT_value_list.index(crit_val_3)])
    #Final check if str8_vals were found
    if (len(str8_vals) == 4):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] not in str8_vals):
                W23_drop_card.append(hand[o])
    return(W23_drop_card)

#NODE 24
def Fiv_Str8_Cards(hand):
    #Access Jacks_or_Better_4WL code
    import Jacks_or_Better_4WL
    #If no straight make no recommendation
    W24_drop_card = []
    #See if the hand is a straight
    straight = Jacks_or_Better_4WL.Straight(hand)
    if (straight[0] != 0):
        W24_drop_card = []
    return(W24_drop_card)

#NODE 2
def Straight_Cards(hand):
    #Call the deci-strategy nodes
    W21_drop_card = Two_Str8_Cards(hand)
    W22_drop_card = Thr_Str8_Cards(hand)
    W23_drop_card = For_Str8_Cards(hand)
    W24_drop_card = Fiv_Str8_Cards(hand)
    #Test NODE 25 implementation
    if (W21_drop_card == []) and (W22_drop_card == []) and (W23_drop_card == []) and (W24_drop_card == []):
        W2_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W21_drop_card,W22_drop_card,W23_drop_card,W24_drop_card]
        W2_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W2_drop_card)

#Neural Network
def Drop_Card_Neural_Network(hand):
    #Call the macro-strategy nodes
    W2_drop_card = Straight_Cards(hand)
    #Compile drop card lists
    Drop_Card_Master_List = [W2_drop_card]
    Drop_Card = Drop_Card_Compile(Drop_Card_Master_List)
    #Final check to make sure a recommendation is made
    if (Drop_Card == []):
        Drop_Card = hand
    return(Drop_Card)

def Wilson_Lazarus(run):
    #Access Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Import time library
    import time
    #Establish starting credits
    credit_start = 1000
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
    #Count the number of hands
    hand_iters = 0
    #Open the data file for writing
    file = open("WL"+str(run)+".txt","w+")
#Since this macro node is defective negative credits are permitted to obtain more accurate probabilities
    while (hand_iters < 1000000):
        #hand iteration counter
        hand_iters = hand_iters + 1
	#Print previous balance
        prev_bal = WL_credits - bet_net_gain
        #Establish bet parameters
        bet_per_hand = 1
        if (WL_credits > (credit_start/100)):
            total_hands = 1
        else:
            total_hands = 1
        #Summon a random hand
        first_hand = Jacks_or_Better_4WL.Random_Cards(5)
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
            temp_reward = Jacks_or_Better_4WL.Reward(temp_hand)
            #Add hand reward to user account
            WL_reward = WL_reward + (temp_reward[0] * bet_per_hand)
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
        total_bet = bet_per_hand * total_hands
        bet_net_gain = round((WL_reward - total_bet),2)
        #Calculate Wilson-Lazarus balance
        WL_credits = round((WL_credits + WL_reward),2)
        #Track total earnings
        total_reward = round((total_reward + WL_reward),2)
	#Build common output vector of hand iterations, rewards, bet reward, bet net gain, current credits and total reward
        comm_out_vect = [hand_iters,RoyFl,Str8Fl,Quad,FullH,Floosh,Str8,Trip,DoubP,Pair,WL_reward,bet_net_gain,WL_credits,total_reward]
        #Print bet output vector
        for i in range(len(comm_out_vect)):
            file.write(str(comm_out_vect[i])),
            file.write(" ")
        file.write('\n')
    file.close()

def run_control():
    for i in range(1,6):
        Wilson_Lazarus(i)

run_control()
