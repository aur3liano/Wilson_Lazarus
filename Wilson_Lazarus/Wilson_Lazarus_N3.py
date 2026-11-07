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

#NODE 31-34
def Flush_num(hand,num):
    #Access Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Convert hand into list of suits
    suit_list = Jacks_or_Better_4WL.Obtain_Suits(hand)
    #Check if hand contains the quantity of desired cards
    desired_cards = []
    Wnode_drop_card = []
    if (suit_list.count("s") == num):
        for i in range(len(suit_list)):
            if (suit_list[i] == "s"):
             desired_cards.append(hand[i])
    elif (suit_list.count("d") == num):
        for j in range(len(suit_list)):
            if (suit_list[j] == "d"):
             desired_cards.append(hand[j])
    elif (suit_list.count("c") == num):
        for k in range(len(suit_list)):
            if (suit_list[k] == "c"):
             desired_cards.append(hand[k])
    elif (suit_list.count("h") == num):
        for m in range(len(suit_list)):
            if (suit_list[m] == "h"):
             desired_cards.append(hand[m])
    for n in range(len(hand)):
        if (hand[n] not in desired_cards):
            Wnode_drop_card.append(hand[n])
    return(Wnode_drop_card)

#NODE 3
def Flush_Cards(hand):
    #Call the deci-strategy nodes
    W31_drop_card = Flush_num(hand,2)
    W32_drop_card = Flush_num(hand,3)
    W33_drop_card = Flush_num(hand,4)
    W34_drop_card = Flush_num(hand,5)
    #Test NODE 35 implementation
    if (W31_drop_card == []) and (W32_drop_card == []) and (W33_drop_card == []) and (W34_drop_card == []):
        W3_drop_card = []
    else:
        #Compile the drop card lists
        Drop_Card_Master_List = [W31_drop_card,W32_drop_card,W33_drop_card,W34_drop_card]
        W3_drop_card = Drop_Card_Compile(Drop_Card_Master_List)
    return(W3_drop_card)

#Neural Network
def Drop_Card_Neural_Network(hand):
    #Call the macro-strategy nodes
    W3_drop_card = Flush_Cards(hand)
    #Compile drop card lists
    Drop_Card_Master_List = [W3_drop_card]
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
    credit_start = 10000
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
            total_hands = 1
        else:
            total_hands = 1
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
