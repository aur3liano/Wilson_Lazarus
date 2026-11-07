#This program generates all of the possible 5 card hands for a 52 card deck

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
    
Generate_Hands()
