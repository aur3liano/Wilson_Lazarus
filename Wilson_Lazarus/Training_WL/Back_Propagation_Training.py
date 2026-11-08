#Writing Configuration File
def Config_File_Write(WL_config,filename):
    #Decompose WL_config
    Node_PC_vect = WL_config[0]
    Node_gain_vect = WL_config[1]
    Node_sub_iter_vect = WL_config[2]
    Nodes_used = WL_config[3]
    mand_iters = WL_config[4]
    gain_adapt = WL_config[5]
    BNG = WL_config[6]
    #Open the configuration file for writing
    config_file = open(filename,'a')
    '''
    Write the Priority coefficients, gains, sub iterations,
    mandatory iterations and the gain adaptation value
    to the configuration file
    '''
    for NPCv in range(len(Node_PC_vect)):
        config_file.write((str(Node_PC_vect[NPCv])+"\t"),)
    for NGv in range(len(Node_gain_vect)):
        config_file.write((str(Node_gain_vect[NGv])+"\t"),)
    for NSIv in range(len(Node_sub_iter_vect)):
        config_file.write((str(Node_sub_iter_vect[NSIv])+"\t"),)
    for NU in range(len(Nodes_used)):
        config_file.write((str(Nodes_used[NU])+"\t"),)
    config_file.write((str(mand_iters)+"\t"),)
    config_file.write((str(gain_adapt)+"\t"),)
    config_file.write((str(BNG)+"\t"))
    #Write the next line
    config_file.write("\n")
    #Close the configuration file
    config_file.close()
    return(filename)

def Config_File_Read(Centi_Nodes,Deci_Nodes,filename,trunc_flag):
    #Open the configuration file for reading
    config_file = open(filename,'r+')
    #Read the contents
    config = config_file.readlines()
    #Convert list to string
    config = config[0]
    #Convert the string back to a list
    config = config.split("\t")
    #Test to see if erasing data is necessary
    if (trunc_flag == 1):
        #Remove the previous contents
        config_file.truncate(0)
    #Close the file
    config_file.close()
    #Initialize lists to build
    Node_PC_vect = (Centi_Nodes + Deci_Nodes)*[0]
    Node_gain_vect = (Centi_Nodes + Deci_Nodes)*[0]
    Node_sub_iter_vect = (Centi_Nodes + Deci_Nodes)*[0]
    Nodes_used = (Centi_Nodes + Deci_Nodes)*[0]
    #Cycle through all of the different expected lists
    for li in range(12):
        gains_index_start = (Centi_Nodes+Deci_Nodes)*1
        sub_iter_index_start = (Centi_Nodes+Deci_Nodes)*2
        nodes_used_index_start = (Centi_Nodes+Deci_Nodes)*3
        Node_PC_vect[li] = float(config[li])
        Node_gain_vect[li] = float(config[li+gains_index_start])
        Node_sub_iter_vect[li] = int(float(config[li+sub_iter_index_start]))
        Nodes_used[li] = int(float(config[li+nodes_used_index_start]))
    MI_index_start = ((Centi_Nodes+Deci_Nodes)*3)+1
    GA_index_start = ((Centi_Nodes+Deci_Nodes)*3)+2
    BNG_index_start = ((Centi_Nodes+Deci_Nodes)*3)+3
    mand_iters = int(float(config[MI_index_start]))
    gain_adapt = float(config[GA_index_start])
    BNG = float(config[BNG_index_start])
    WL_config = [Node_PC_vect,Node_gain_vect,Node_sub_iter_vect,Nodes_used,
                 mand_iters,gain_adapt,BNG]
    return(WL_config)

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

def Random_Cards(n):
    #Import the random library
    import random
    #Gather n unique suits and values
    hand = []
    while (len(hand) < n):
        #Call random integer for next card
        card = random.randint(1,52)
        if card in hand:
            #Skip duplicate card
            continue
        else:
            #Append unique card
            hand.append(card)
    #Give the hand back to main driver
    return(hand)

#NODE 111
def JoB_Pair_Exists(hand):
    #If no pair make no recommendation
    W111_drop_card = []
    #Establish list of acceptable pairs
    pair_list = [11,12,13,14]
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    
#NODE 121
def Double_Pair_Exists(hand):
    #If no double pair make no recommendation
    W121_drop_card = []
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    #If no double pair potential make no recommendation
    W122_drop_card = []
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    
#NODE 131 and NODE 142 and NODE 152
def Triple_Exists(hand):
    #If no double pair potential make no recommendation
    W131_drop_card = []
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    
#NODE 141
def Quad_Exists(hand):
    #If no double pair potential make no recommendation
    W141_drop_card = []
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
    
#NODE 151
def Full_House_Exists(hand):
    #If no double pair make no recommendation
    W151_drop_card = []
    #Convert hand into a list of values
    value_list = Obtain_Vals(hand)
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
        #If a Full House exists recommend dropping zero cards
        W151_drop_card = [0]
    return(W151_drop_card)

def Double_Pair_Exists_Act(N_PC,hand):
    #import random library
    import random
    #Test node 121 and node 153 activation
    rand_flag = random.random()
    if (rand_flag < N_PC):
        N_drop_card = Double_Pair_Exists(hand)
        activation = 1
    else:
        N_drop_card = []
        activation = 0
    return(N_drop_card,activation)

def Double_Pair_Poten_Act(N_PC,hand):
    #import random library
    import random
    #Test node 122, node 132 and node 143 activation
    rand_flag = random.random()
    if (rand_flag < N_PC):
        N_drop_card = Double_Pair_Potential(hand)
        activation = 1
    else:
        N_drop_card = []
        activation = 0
    return(N_drop_card,activation)
    
def Triple_Exists_Act(N_PC,hand):
    #import random library
    import random
    #Test node 131, node 142 and node 152 activation
    rand_flag = random.random()
    if (rand_flag < N_PC):
        N_drop_card = Triple_Exists(hand)
        activation = 1
    else:
        N_drop_card = []
        activation = 0
    return(N_drop_card,activation)

#Wilson_Plays_JOB
def Wilson_Plays_JOB(reward_vector,Node_PC_vect):
    #import random library
    import random
    #import JoB for Wilson Lazarus
    import Jacks_or_Better_4WL
    #Breakdown the priority coefficient vector
    N110_PC = Node_PC_vect[0] #Deci Node 1
    N120_PC = Node_PC_vect[1] #Deci Node 2
    N130_PC = Node_PC_vect[2] #Deci Node 3
    N140_PC = Node_PC_vect[3] #Deci Node 4
    N150_PC = Node_PC_vect[4] #Deci Node 5
    N111_PC = Node_PC_vect[5] #Centi Node 1
    N112_PC = Node_PC_vect[6] #Centi Node 2
    N121_PC = Node_PC_vect[7] #Centi Node 3
    N122_PC = Node_PC_vect[8] #Centi Node 4
    N131_PC = Node_PC_vect[9] #Centi Node 5
    N141_PC = Node_PC_vect[10] #Centi Node 6
    N151_PC = Node_PC_vect[11] #Centi Node 7
    #Summon a random hand
    first_hand = Random_Cards(5)
    #Test node 111 activation
    rf_111 = random.random()
    if (rf_111 < N111_PC):
        W111_drop_card = JoB_Pair_Exists(first_hand)
        act_111 = 1
    else:
        W111_drop_card = []
        act_111 = 0
    #Test node 112 activation
    rf_112 = random.random()
    if (rf_112 < N112_PC):
        W112_drop_card = JoB_Pair_Potential(first_hand)
        act_112 = 1
    else:
        W112_drop_card = []
        act_112 = 0
    #Test node 121 and node 153 activation
    rf_121 = random.random()
    if (rf_121 < N121_PC):
        W121_drop_card = Double_Pair_Exists(first_hand)
        act_121 = 1
    else:
        W121_drop_card = []
        act_121 = 0
    #Test node 121 and node 153 activation
    [W121_drop_card,act_121_pre1] = Double_Pair_Exists_Act(N121_PC,first_hand)
    [W153_drop_card,act_121_pre2] = Double_Pair_Exists_Act(N121_PC,first_hand)
    #Consolidate node 121 activation
    if ((act_121_pre1 == 1) or (act_121_pre2 == 1)):
        act_121 = 1
    else:
        act_121 = 0
    #Test node 122, node 132, node 143 and node 154 activation
    [W122_drop_card,act_122_pre1] = Double_Pair_Poten_Act(N122_PC,first_hand)
    [W132_drop_card,act_122_pre2] = Double_Pair_Poten_Act(N122_PC,first_hand)
    [W143_drop_card,act_122_pre3] = Double_Pair_Poten_Act(N122_PC,first_hand)
    [W154_drop_card,act_122_pre4] = Double_Pair_Poten_Act(N122_PC,first_hand)
    #Consolidate node 122 activation
    if ((act_122_pre1 == 1) or (act_122_pre2 == 1) or (act_122_pre3 == 1) or (act_122_pre4 == 1)):
        act_122 = 1
    else:
        act_122 = 0
    #Test node 131, node 142 and node 152 activation
    [W131_drop_card,act_131_pre1] = Triple_Exists_Act(N131_PC,first_hand)
    [W142_drop_card,act_131_pre2] = Triple_Exists_Act(N131_PC,first_hand)
    [W152_drop_card,act_131_pre3] = Triple_Exists_Act(N131_PC,first_hand)
    #Consolidate node 131 activation
    if ((act_131_pre1 == 1) or (act_131_pre2 == 1) or (act_131_pre3 == 1)):
        act_131 = 1
    else:
        act_131 = 0
    #Test node 141 activation
    rf_141 = random.random()
    if (rf_141 < N141_PC):
        W141_drop_card = Quad_Exists(first_hand)
        act_141 = 1
    else:
        W141_drop_card = []
        act_141 = 0
    #Test node 151 activation
    rf_151 = random.random()
    if (rf_151 < N151_PC):
        W151_drop_card = Full_House_Exists(first_hand)
        act_151 = 1
    else:
        W151_drop_card = []
        act_151 = 0
    #Test node 110 activation
    rf_110 = random.random()
    if (rf_110 < N110_PC):
        if ((W111_drop_card == []) and (W112_drop_card == [])):
            W11_drop_card = []
            act_11 = 0
        else:
            #Compile the drop card lists
            DCML_11 = [W111_drop_card,W112_drop_card]
            W11_drop_card = Drop_Card_Compile(DCML_11)
            act_11 = 1
    else:
        W11_drop_card = []
        act_11 = 0
    #Test node 120 activation
    rf_120 = random.random()
    if (rf_120 < N120_PC):
        if ((W121_drop_card == []) and (W122_drop_card == [])):
            W12_drop_card = []
            act_12 = 0
        else:
            #Compile the drop card lists
            DCML_12 = [W121_drop_card,W122_drop_card]
            W12_drop_card = Drop_Card_Compile(DCML_12)
            act_12 = 1
    else:
        W12_drop_card = []
        act_12 = 0
    #Test node 130 activation
    rf_130 = random.random()
    if (rf_130 < N130_PC):
        if ((W131_drop_card == []) and (W132_drop_card == [])):
            W13_drop_card = []
            act_13 = 0
        else:
            #Compile the drop card lists
            DCML_13 = [W131_drop_card,W132_drop_card]
            W13_drop_card = Drop_Card_Compile(DCML_13)
            act_13 = 1
    else:
        W13_drop_card = []
        act_13 = 0
    #Test node 140 activation
    rf_140 = random.random()
    if (rf_140 < N140_PC):
        if ((W141_drop_card == []) and (W142_drop_card == []) and (W143_drop_card == [])):
            W14_drop_card = []
            act_14 = 0
        else:
            #Compile the drop card lists
            DCML_14 = [W141_drop_card,W142_drop_card,W143_drop_card]
            W14_drop_card = Drop_Card_Compile(DCML_14)
            act_14 = 1
    else:
        W14_drop_card = []
        act_14 = 0
    #Test node 150 activation
    rf_150 = random.random()
    if (rf_150 < N150_PC):
        if ((W151_drop_card == []) and (W152_drop_card == []) and (W153_drop_card == []) and (W154_drop_card == [])):
            W15_drop_card = []
            act_15 = 0
        else:
            #Compile the drop card lists
            DCML_15 = [W151_drop_card,W152_drop_card,W153_drop_card,W154_drop_card]
            W15_drop_card = Drop_Card_Compile(DCML_15)
            act_15 = 1
    else:
        W15_drop_card = []
        act_15 = 0
    #Execute the neural network
    if (W11_drop_card == []) and (W12_drop_card == []) and (W13_drop_card == []) and (W14_drop_card == []) and (W15_drop_card == []):
        W1_drop_card = []
    else:
        #Compile the drop card lists
        DCML_1 = [W11_drop_card,W12_drop_card,W13_drop_card,W14_drop_card,W15_drop_card]
        W1_drop_card = Drop_Card_Compile(DCML_1)
    #Compile activation flags
    Nodes_used = [act_11,act_12,act_13,act_14,act_15,act_111,act_112,act_121,act_122,act_131,act_141,act_151]
    #Build the second hand
    second_hand = []
    #Test if it was recommended to drop zero cards
    if (W1_drop_card == []):
            second_hand = first_hand
    else:
        for i in range(len(first_hand)):
            #Drop the cards in the Drop Card list
            if (first_hand[i] not in W1_drop_card):
                second_hand.append(first_hand[i])
    #Calculate cards to recover
    card_recover_quantity = len(first_hand)-len(second_hand)
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
    #Initialize bet
    bet_per_hand = 1
    total_hands = 1
    BET = (bet_per_hand*total_hands)
    total_reward = 0
    for j in range(total_hands):
        #Initialize individual hand reward
        temp_reward = 0
        #Collect other cards
        temp_cards = Random_Cards(card_recover_quantity)
        #Append new cards
        temp_hand = second_hand + temp_cards
        #Assign hand reward
        temp_reward = Jacks_or_Better_4WL.Reward(temp_hand,reward_vector)
        #Add hand reward to user account
        total_reward = total_reward + (temp_reward[0] * bet_per_hand)
        #Tally Rewards
        if (temp_reward[0] == reward_vector[0]):
            Pair = Pair + 1
        elif (temp_reward[0] == reward_vector[1]):
            DoubP = DoubP + 1
        elif (temp_reward[0] == reward_vector[2]):
            Trip = Trip + 1
        elif (temp_reward[0] == reward_vector[3]):
            Str8 = Str8 + 1
        elif (temp_reward[0] == reward_vector[4]):
            Floosh = Floosh + 1
        elif (temp_reward[0] == reward_vector[5]):
            FullH = FullH + 1
        elif (temp_reward[0] == reward_vector[6]):
            Quad = Quad + 1
        elif (temp_reward[0] == reward_vector[7]):
            Str8Fl = Str8Fl + 1
        elif (temp_reward[0] == reward_vector[8]):
            RoyFl = RoyFl + 1
    BNG = ((round((total_reward - BET),2))/total_hands)*100
    return(BNG,Nodes_used)
    
#Initiate Training
def Initiate_Training(A,B,reward_vector):
    #Initialize strategy node priorities
    N110_PC = 0.5 #Deci Node 1
    N120_PC = 0.5 #Deci Node 2
    N130_PC = 0.5 #Deci Node 3
    N140_PC = 0.5 #Deci Node 4
    N150_PC = 0.5 #Deci Node 5
    N111_PC = 0.5 #Centi Node 1
    N112_PC = 0.5 #Centi Node 2
    N121_PC = 0.5 #Centi Node 3
    N122_PC = 0.5 #Centi Node 4
    N131_PC = 0.5 #Centi Node 5
    N141_PC = 0.5 #Centi Node 6
    N151_PC = 0.5 #Centi Node 7
    #Build a vector of the priority coefficients
    Node_PC_vect = [N110_PC,N120_PC,N130_PC,N140_PC,N150_PC,N111_PC,N112_PC,
                    N121_PC,N122_PC,N131_PC,N141_PC,N151_PC]
    '''
    Wilson plays Jacks or Better
    '''
    [BNG,Nodes_used] = Wilson_Plays_JOB(reward_vector,Node_PC_vect)
    #Initialize Back Propagation parameters
    A = 0.025
    B = 7
    C_ic = 0.5
    i_crit = round(C_ic*(1/A),0)
    mand_iters = B*i_crit
    gain = A*B
    gain_adapt = 1-gain
    #Initialize individual back propagation values
    N110_gain = round(gain,4) #Deci Node 1
    N120_gain = round(gain,4) #Deci Node 2
    N130_gain = round(gain,4) #Deci Node 3
    N140_gain = round(gain,4) #Deci Node 4
    N150_gain = round(gain,4) #Deci Node 5
    N111_gain = round(gain,4) #Centi Node 1
    N112_gain = round(gain,4) #Centi Node 2
    N121_gain = round(gain,4) #Centi Node 3
    N122_gain = round(gain,4) #Centi Node 4
    N131_gain = round(gain,4) #Centi Node 5
    N141_gain = round(gain,4) #Centi Node 6
    N151_gain = round(gain,4) #Centi Node 7
    N110_sub_iter = 0 #Deci Node 1
    N120_sub_iter = 0 #Deci Node 2
    N130_sub_iter = 0 #Deci Node 3
    N140_sub_iter = 0 #Deci Node 4
    N150_sub_iter = 0 #Deci Node 5
    N111_sub_iter = 0 #Centi Node 1
    N112_sub_iter = 0 #Centi Node 2
    N121_sub_iter = 0 #Centi Node 3
    N122_sub_iter = 0 #Centi Node 4
    N131_sub_iter = 0 #Centi Node 5
    N141_sub_iter = 0 #Centi Node 6
    N151_sub_iter = 0 #Centi Node 7
    #Build a vector of the priority coefficients
    Node_gain_vect = [N110_gain,N120_gain,N130_gain,N140_gain,N150_gain,
                      N111_gain,N112_gain,N121_gain,N122_gain,N131_gain,
                      N141_gain,N151_gain]
    #Build a vector of the priority coefficients
    Node_sub_iter_vect = [N110_sub_iter,N120_sub_iter,N130_sub_iter,
                          N140_sub_iter,N150_sub_iter,N111_sub_iter,
                          N112_sub_iter,N121_sub_iter,N122_sub_iter,
                          N131_sub_iter,N141_sub_iter,N151_sub_iter]
    '''
    Write out Priorities, Gains, Sub Iterations, Nodes used, Mandatory
    Iterations, Gain Adaptation and BNG
    '''
    WL_config = [Node_PC_vect,Node_gain_vect,Node_sub_iter_vect,Nodes_used,
                 mand_iters,gain_adapt,BNG]
    print(WL_config)
    filename_1 = "WL_prev_config.txt"
    filename_1 = Config_File_Write(WL_config,filename_1)
    filename_2 = "WL_config.txt"
    filename_2 = Config_File_Write(WL_config,filename_2)
    Initiated = 1
    return(Initiated)

def PC_Adapt(Prior_Coeff,BNG,sub_iter,gain):
    if (BNG >= 1):
        #Magnify successful decisions
        adj = round(gain*(1-Prior_Coeff),4)
    else:
        adj = round(-gain*Prior_Coeff,4)
    #Implement the adjustment
    Prior_Coeff = Prior_Coeff + adj
    #Increment simulation sub iterations
    sub_iter = sub_iter + 1
    return(Prior_Coeff,sub_iter)

#Initiate Training
def Fixed_Iteration_Training(A,B,reward_vector):
    #Read in previous configuration contents
    Centi_Nodes = 7
    Deci_Nodes = 5
    filename = "WL_prev_config.txt"
    trunc_flag = 1
    WL_config = Config_File_Read(Centi_Nodes,Deci_Nodes,filename,trunc_flag)
    #Decompose WL_config
    Node_PC_vect = WL_config[0]
    Node_gain_vect = WL_config[1]
    Node_sub_iter_vect = WL_config[2]
    Nodes_used = WL_config[3]
    mand_iters = WL_config[4]
    gain_adapt = WL_config[5]
    BNG = WL_config[6]
    '''
    Move through priority coefficients to implement back propagation
    '''
    for NPCv in range(len(Node_PC_vect)):
        if (Nodes_used[NPCv] == 1):
            [Node_PC_vect[NPCv],Node_sub_iter_vect[NPCv]] = PC_Adapt(Node_PC_vect[NPCv],BNG,Node_sub_iter_vect[NPCv],Node_gain_vect[NPCv])
        else:
            continue
    '''
    Determine if a gain needs adaptation
    '''
    for NPCv in range(len(Node_PC_vect)):
        if (Node_sub_iter_vect[NPCv] > mand_iters):
            Node_gain_vect[NPCv] = round(Node_gain_vect[NPCv]*gain_adapt,4)
            Node_sub_iter_vect[NPCv] = 0
        else:
            continue
    '''
    Wilson plays Jacks or Better
    '''
    [BNG,Nodes_used] = Wilson_Plays_JOB(reward_vector,Node_PC_vect)
    '''
    Write out Priorities, Gains, Sub Iterations, Nodes used, Mandatory
    Iterations, Gain Adaptation and BNG
    '''
    WL_config = [Node_PC_vect,Node_gain_vect,Node_sub_iter_vect,Nodes_used,
                 mand_iters,gain_adapt,BNG]
    filename_1 = "WL_prev_config.txt"
    filename_1 = Config_File_Write(WL_config,filename_1)
    filename_2 = "WL_config.txt"
    filename_2 = Config_File_Write(WL_config,filename_2)
    Training = 1
    return(Training)
    
def Wilson_Lazarus_Training():
    #Import time library
    import time
    #Establish reward vector
    Reward_Vect_Baseline = [1,2.735043,6.15385,33.1294,66.155,90.2564,541.538,9386.67,84480]
    Reward_Vect_Gain = 0.213640369599476 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    #Choose between convergence and fixed training sets
    training_method = "fixed"
    #Initiate training
    if (training_method == "convergence"):
        #Set convergence parameters
        A = 0.025
        B = 7
        Convergence_Vector = Convergence_Training(A,B,reward_vector)
    elif (training_method == "fixed"):
        '''
        #Set fixed training parameters
        Discretization = 0.001
        Amplification = 7
        '''
        Fixed_Iterations = 99999
        A = 0.025
        B = 7
        Initiated = Initiate_Training(A,B,reward_vector)
        for fi in range(Fixed_Iterations):
            Training = Fixed_Iteration_Training(A,B,reward_vector)
    else:
        print('Training Method Not Selected Properly')
        time.sleep(60)
    return(training_method)

Wilson_Lazarus_Training()