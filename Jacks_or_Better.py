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

def Game():
    #Establish starting credits for user
    credit_start = 10
    usr_credits = credit_start
    total_reward = 0
    #Establish previous balance
    bet_net_gain = 0
    #Establish reward vector
    Reward_Vect = []
    Reward_Vect_Baseline = [3.25,8.89,20,107.67,215,293.33,1760,30506.67,274560]
    Reward_Vect_Gain = 0.065735472679572
    for rv in range(len(Reward_Vect_Baseline)):
        Reward_Vect.append(Reward_Vect_Baseline[rv] * Reward_Vect_Gain)
    while (usr_credits > 1):
        #Print previous balance
        prev_bal = usr_credits - bet_net_gain
        print("Previous Balance = " + str(prev_bal))
        #Print current balance
        print("Current Balance = " + str(usr_credits))
        #Prompt user to establish the bet per hand
        bet_per_hand = eval(input("What is your bet per hand? "))
        while (bet_per_hand < 1):
            #Tell user the minimum bet threshold
            print('WARNING: minimum bet is 1 credit')
            bet_per_hand = eval(input("What is your bet per hand? "))
        #Prompt user to establish the total hands
        total_hands = eval(input("How many hands do you want to bet on? "))
        #Summon a random hand
        first_hand = Random_Cards(5)
        #Translate the first hand
        disp_first_hand = Hand_Translator(first_hand)
        #Print the first hand
        print(disp_first_hand)
        #Prompt the user to select drop cards
        second_hand = []
        for i in range(len(first_hand)):
            usr_ans = str(input("Drop "+disp_first_hand[i]+"? (Answer yes or no) "))
            #Drop the cards user doesn't want
            if (usr_ans == "no"):
                second_hand.append(first_hand[i])
        #Calculate cards to recover
        card_recover_quantity = len(first_hand)-len(second_hand)
        #Reduce user credit amount by total bet
        usr_credits = usr_credits - (bet_per_hand*total_hands)
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
        usr_reward = 0
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
            usr_reward = usr_reward + (temp_reward[0] * bet_per_hand)
            #Translate the hand into a display hand
            temp_hand = Hand_Translator(temp_hand)
            #Print the display hand and reward
            print(temp_hand, end="")
            print(" " + temp_reward[1])
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
                print(str(reward_list_num[i]) + " " + reward_list_str[i])
        #Print total hands
        print("Total Hands = " + str(total_hands))
        #Print total bet
        total_bet = bet_per_hand * total_hands
        print("Total Bet = " + str(total_bet))
        #Print total bet reward
        print("Bet Reward = " + str(usr_reward))
        #Print bet gain
        bet_net_gain = round((usr_reward - total_bet),2)
        print("Net Gain = " + str(bet_net_gain))
        print()
        #Calculate user balance
        usr_credits = round((usr_credits + usr_reward),2)
    #Track total earnings
    total_reward = round((total_reward + usr_reward),2)
    #Print total earnings
    print("Total Earnings = " + str(total_reward) + "!")
    #Notify user game is over
    print("Game Over")
    
Game()
