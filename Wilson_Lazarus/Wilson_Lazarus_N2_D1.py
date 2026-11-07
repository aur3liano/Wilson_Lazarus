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
    #Implement the four test method to find two cards with straight potential
    value_1 = 0
    value_2 = 0
    NT_value_1 = 0
    NT_value_2 = 0
    #Max straight range
    for i in range(4):
        crit_val = (max_val-1) - i
        if (value_list.count(crit_val) == 1):
            value_1 = hand[value_list.index(max_val)]
            value_2 = hand[value_list.index(crit_val)]
    #Min straight range
    for j in range(4):
        crit_val = (min_val+1) + j
        if (value_list.count(crit_val) == 1):
            value_1 = hand[value_list.index(crit_val)]
            value_2 = hand[value_list.index(min_val)]
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
        #Check if new_three is empty
        if (new_three != []):
            #Obtain new value list for new_three
            NT_value_list = Jacks_or_Better_4WL.Obtain_Vals(new_three)
            #Find straight limits
            NT_max_val = max(NT_value_list)
            NT_min_val = min(NT_value_list)
            #NT Max straight range
            for m in range(4):
                crit_val = (NT_max_val-1) - m
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = hand[value_list.index(NT_max_val)]
                    NT_value_2 = hand[value_list.index(crit_val)]
            #NT Min straight range
            for n in range(4):
                crit_val = (NT_min_val+1) + n
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = hand[value_list.index(crit_val)]
                    NT_value_2 = hand[value_list.index(NT_min_val)]
            if (NT_value_1 != 0) and (NT_value_2 != 0):
                str8_couple = [NT_value_1,NT_value_2]
    if (value_2 != 0) or (NT_value_2 != 0):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] != str8_couple[0]) and (hand[o] != str8_couple[1]):
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
    #Implement the four test method to find three cards with straight potential
    value_1 = 0
    value_2 = 0
    value_3 = 0
    NT_value_1 = 0
    NT_value_2 = 0
    NT_value_3 = 0
    #Max straight range
    for i in range(4):
        crit_val = (max_val-1) - i
        if (value_list.count(crit_val) == 1):
            value_1 = max_val
            index_1 = value_list.index(max_val)
            value_2 = crit_val
            index_2 = value_list.index(crit_val)
            for i2 in range(4):
                crit_val_2 = (max_val-1) - i2
                if (value_list.count(crit_val_2) == 1) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                    value_3 = crit_val_2
                    index_3 = value_list.index(crit_val_2)
    #Min straight range
    for j in range(4):
        crit_val = (min_val+1) + j
        if (value_list.count(crit_val) == 1):
            value_1 = crit_val
            index_1 = value_list.index(crit_val)
            value_2 = min_val
            index_2 = value_list.index(min_val)
            for j2 in range(4):
                crit_val_2 = (min_val+1) + j2
                if (value_list.count(crit_val_2) == 1) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                    value_3 = crit_val_2
                    index_3 = value_list.index(crit_val_2)
    #Initialize the str8_couple
    str8_three = []
    if (value_3 != 0):
        str8_three = [hand[index_1],hand[index_2],hand[index_3]]
    else:
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
            #NT Max straight range
            for m in range(4):
                crit_val = (NT_max_val-1) - m
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = NT_max_val
                    NT_index_1 = value_list.index(NT_max_val)
                    NT_value_2 = NT_max_val - m
                    NT_index_2 = value_list.index(crit_val)
                    for m2 in range(4):
                        crit_val_2 = (NT_max_val-1) - m2
                        if (value_list.count(crit_val_2) == 1) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                            NT_value_3 = crit_val_2
                            NT_index_3 = value_list.index(crit_val_2)
            #NT Min straight range
            for n in range(4):
                crit_val = (NT_min_val+1) + n
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = crit_val
                    NT_index_1 = value_list.index(crit_val)
                    NT_value_2 = NT_min_val
                    NT_index_2 = value_list.index(NT_min_val)
                    for n2 in range(4):
                        crit_val_2 = (NT_min_val+1) + n2
                        if (value_list.count(crit_val_2) == 1) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                            NT_value_3 = crit_val_2
                            NT_index_3 = value_list.index(crit_val_2)
            if (NT_value_3 != 0):
                str8_three = [hand[NT_index_1],hand[NT_index_2],hand[NT_index_3]]
    if (value_3 != 0) or (NT_value_3 != 0):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] != str8_three[0]) and (hand[o] != str8_three[1]) and (hand[o] != str8_three[2]):
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
    #Implement the four test method to find two cards with straight potential
    value_1 = 0
    value_2 = 0
    value_3 = 0
    value_4 = 0
    NT_value_1 = 0
    NT_value_2 = 0
    NT_value_3 = 0
    NT_value_4 = 0
    #Max straight range
    for i in range(4):
        crit_val = (max_val-1) - i
        if (value_list.count(crit_val) == 1):
            value_1 = max_val
            index_1 = value_list.index(max_val)
            value_2 = crit_val
            index_2 = value_list.index(crit_val)
            for i2 in range(4):
                crit_val_2 = (max_val-1) - i2
                if (value_list.count(crit_val_2) == 1) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                    value_3 = crit_val_2
                    index_3 = value_list.index(crit_val_2)
                    for i3 in range(4):
                        crit_val_3 = (max_val-1) - i3
                        if (value_list.count(crit_val_3) == 1) and (crit_val_3 != value_1) and (crit_val_3 != value_2) and (crit_val_3 != value_3):
                            value_4 = crit_val_3
                            index_4 = value_list.index(crit_val_3)
    #Min straight range
    for j in range(4):
        crit_val = (min_val+1) + j
        if (value_list.count(crit_val) == 1):
            value_1 = crit_val
            index_1 = value_list.index(crit_val)
            value_2 = min_val
            index_2 = value_list.index(min_val)
            for j2 in range(4):
                crit_val_2 = (min_val+1) + j2
                if (value_list.count(crit_val_2) == 1) and (crit_val_2 != value_1) and (crit_val_2 != value_2):
                    value_3 = crit_val_2
                    index_3 = value_list.index(crit_val_2)
                    for j3 in range(4):
                        crit_val_3 = (min_val+1) + j3
                        if (value_list.count(crit_val_3) == 1) and (crit_val_3 != value_1) and (crit_val_3 != value_2) and (crit_val_3 != value_3):
                            value_4 = crit_val_3
                            index_4 = value_list.index(crit_val_3)
    #Initialize the str8_couple
    str8_couple = []
    if (value_4 != 0):
        str8_couple = [value_1,value_2,value_3,value_4]
    else:
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
            #NT Max straight range
            for m in range(4):
                crit_val = (NT_max_val-1) - m
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = NT_max_val
                    NT_index_1 = value_list.index(NT_max_val)
                    NT_value_2 = crit_val
                    NT_value_2 = value_list.index(crit_val)
                    for m2 in range(4):
                        crit_val_2 = (NT_max_val-1) - m2
                        if (value_list.count(crit_val_2) == 1) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                            NT_value_3 = crit_val_2
                            NT_index_3 = value_list.index(crit_val_2)
                            for m3 in range(4):
                                crit_val_3 = (NT_max_val-1) - m3
                                if (value_list.count(crit_val_3) == 1) and (crit_val_3 != NT_value_1) and (crit_val_3 != NT_value_2) and (crit_val_3 != NT_value_3):
                                    NT_value_4 = crit_val_3
                                    NT_index_4 = value_list.index(crit_val_3)
            #NT Min straight range
            for n in range(4):
                crit_val = (NT_min_val+1) + n
                if (value_list.count(crit_val) == 1):
                    NT_value_1 = crit_val
                    NT_index_1 = value_list.index(crit_val)
                    NT_value_2 = NT_min_val
                    NT_value_2 = value_list.index(NT_min_val)
                    for n2 in range(4):
                        crit_val_2 = (NT_min_val+1) - n2
                        if (value_list.count(crit_val_2) == 1) and (crit_val_2 != NT_value_1) and (crit_val_2 != NT_value_2):
                            NT_value_3 = crit_val_2
                            NT_index_3 = value_list.index(crit_val_2)
                            for n3 in range(4):
                                crit_val_3 = (NT_min_val+1) - n3
                                if (value_list.count(crit_val_3) == 1) and (crit_val_3 != NT_value_1) and (crit_val_3 != NT_value_2) and (crit_val_3 != NT_value_3):
                                    NT_value_4 = crit_val_3
                                    NT_index_4 = value_list.index(crit_val_3)
            if (NT_value_4 != 0):
                str8_couple = [NT_value_1,NT_value_2,NT_value_3,NT_value_4]
    if (value_4 != 0) or (NT_value_4 != 0):
        #Build the drop card list of values that are not the straight cards
        for o in range(len(hand)):
            if (hand[o] != str8_couple[0]) and (hand[o] != str8_couple[1]) and (hand[o] != str8_couple[2]) and (hand[o] != str8_couple[3]):
                W23_drop_card.append(hand[o])
    return(W23_drop_card)

#THIS NODE IS CURRENTLY USELESS BECAUSE IT MAKES NO DISTINCTION BETWEEN A RECOMMENDATION AND NO RECOMMENDATION
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
    if (W21_drop_card == []) and (W22_drop_card == []):
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

def Wilson_Lazarus():
    #Access Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Import time library
    import time
    #Establish starting credits
    credit_start = 1000000
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
        #Establish bet parameters
        bet_per_hand = 1
        if (WL_credits > (credit_start/100)):
            total_hands = int(credit_start/100)
        else:
            total_hands = int(WL_credits)
        #Summon a random hand
#Debugging
        first_hand = Jacks_or_Better_4WL.Random_Cards(5)
#        first_hand = [1,2,3,4,5]
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
        print(second_hand)
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
            temp_reward = Jacks_or_Better_4WL.Reward(temp_hand)
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
# Debugging
#        WL_credits = 0
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
