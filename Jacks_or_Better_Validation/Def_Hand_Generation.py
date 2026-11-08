#This program generates all of the possible 5 card hands for a 52 card deck

def Gen_All_2_Combos():
    import time
    #Initialize time list
    times = []
    #Initizlize the master combonation list
    master_combo_list = []
    #Card 1 ranges from 1 to 51
    for c1 in range(1,52):
        start_time = time.time()
        #Card 2 ranges from 2 to 52
        for c2 in range((c1+1),53):
            combo = [c1,c2]
            master_combo_list.append(combo)
        end_time = start_time-time.time()
        times.append(end_time)
        print(end_time)
    print()
    print(len(master_combo_list))
    print()
    master_file = open("All_Two_Card_Hands.txt","a+")
    for mcl in range(len(master_combo_list)):
        for par_crd in range(len(master_combo_list[mcl])):
            master_file.write(str(master_combo_list[mcl][par_crd])),
            master_file.write(" ")
        master_file.write('\n')
    master_file.close()
    return(1)

def Gen_All_3_Combos():
    import time
    #Initialize time list
    times = []
    #Initizlize the master combonation list
    master_combo_list = []
    #Card 1 ranges from 1 to 50
    for c1 in range(1,51):
        start_time = time.time()
        #Card 2 ranges from 2 to 51
        for c2 in range((c1+1),52):
            #Card 2 ranges from 3 to 52
            for c3 in range((c2+1),53):
                combo = [c1,c2,c3]
                master_combo_list.append(combo)
        end_time = start_time-time.time()
        times.append(end_time)
        print(end_time)
    print()
    print(len(master_combo_list))
    print()
    master_file = open("All_Three_Card_Hands.txt","a+")
    for mcl in range(len(master_combo_list)):
        for par_crd in range(len(master_combo_list[mcl])):
            master_file.write(str(master_combo_list[mcl][par_crd])),
            master_file.write(" ")
        master_file.write('\n')
    master_file.close()
    return(1)

def Generate_Hands():
    import time
    #Initialize time list
    times = []
    #Initialize the master hand list length list and the MHL_length
    MHL_length = 0
    MHL_length_list = []
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        #Initialize the master hand list
        master_hand_list = []
        #Initialize Card 1 iteration start time
        start_time = time.time()
        #Card 2 ranges from 2 to 49
        for c2 in range((c1+1),50):
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    #Card 5 ranges from 5 to 52
                    for c5 in range((c4+1),53):
                        #Set the list of hand values
                        hand = [c1,c2,c3,c4,c5]
                        #Append the hand to the master list
                        master_hand_list.append(hand)
        #Calculate progressive MHL_length value
        MHL_length = MHL_length + len(master_hand_list)
        #Append the MHL_length to the MHL_length_list
        MHL_length_list.append(MHL_length)
        #Open the master hand file
        master_file = open("All_Five_Card_Hands.txt","a+")
        for j in range(len(master_hand_list)):
            #Loop through each particular hand in the master hand list
            for k in range(len(master_hand_list[j])):
                #Print each element in the master hand list to a text file
                master_file.write(str(master_hand_list[j][k])),
                #Print spaces in between each list element
                master_file.write(" ")
            #Print new line command
            master_file.write('\n')
        #Close the master hand file
        master_file.close()
        #Print the final hand for each Card 1 value as a sanity check
        print(hand)
        #Append the time for each Card 1 iteration
        delta_time = time.time() - start_time
        times.append(delta_time)
        print(delta_time)
    #Open the MHL_list text file
    MHL_file = open("Master_Hand_Lengths.txt","w+")
    #Loop through the MHL_length_list
    for i in range(len(MHL_length_list)):
        #Print the MHL_lengths to a text file
        MHL_file.write(str(MHL_length_list[i]))
        #Print the new line command
        MHL_file.write('\n')
    #Close the times file
    MHL_file.close()
    #Open the delta times text file
    times_file = open("Master_Hand_Times.txt","w+")
    #Loop through the times list
    for i in range(len(times)):
        #Print the delta times to a text file
        times_file.write(str(times[i]))
        #Print the new line command
        times_file.write('\n')
    #Close the times file
    times_file.close()
    
    
def main():
    #Control what functions are executed
    #Gen_All_2_Combos()
    Gen_All_3_Combos()
    return()

main()