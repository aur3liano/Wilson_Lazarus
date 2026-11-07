#This program generates all of the possible 5 card decisions for a 52 card deck

def Generate_Hands():
    import time
    #Initialize time list
    times = []
    #Initialize the master decision list length list and the MDL_length
    MDL_length_list = []
#ZERO CARD DECISIONS
    #Initialize the master decision list
    master_decision_list = [[0]]
    #Append the MHL_length to the MHL_length_list
    MDL_length_list.append(len(master_decision_list)) 
#SINGLE CARD DECISIONS
    #Initialize SINGLE-QUADRUPLE decisions start time
    start_time = time.time()
    #Card 1 ranges from 1 to 52
    for c1 in range(1,53):
        #Set the list of decision values
        hand = [c1]
        #Append the hand to the master list
        master_decision_list.append(hand)
        #Append the MHL_length to the MHL_length_list
        MDL_length_list.append(len(master_decision_list))        
#DOUBLE CARD DECISIONS
    #Card 1 ranges from 1 to 51
    for c1 in range(1,52):
        #Card 2 ranges from 2 to 52
        for c2 in range((c1+1),53):
            #Set the list of decision values
            hand = [c1,c2]
            #Append the hand to the master list
            master_decision_list.append(hand)
        #Append the MHL_length to the MDL_length_list
        MDL_length_list.append(len(master_decision_list))        
    #Open the master hand file
    master_file = open("All_Five_Card_Decisions.txt","a+")
    for j in range(len(master_decision_list)):
        #Loop through each particular decision in the master decision list
        for k in range(len(master_decision_list[j])):
            #Print each element in the master hand list to a text file
            master_file.write(str(master_decision_list[j][k])),
            #Print spaces in between each list element
            master_file.write(" ")
        #Print new line command
        master_file.write('\n')
    #Close the master hand file
    master_file.close()
    #Initialize MDL_length for progressive total value calculation
    MDL_length = len(master_decision_list)
#TRIPLE CARD DECISIONS
    #Card 1 ranges from 1 to 50
    for c1 in range(1,51):
        #Initialize the master decision list
        master_decision_list = []
        #Card 2 ranges from 2 to 51
        for c2 in range((c1+1),52):
            #Card 3 ranges from 3 to 52
            for c3 in range((c2+1),53):
                #Set the list of decision values
                hand = [c1,c2,c3]
                #Append the hand to the master list
                master_decision_list.append(hand)
        #Calculate progressive MDL_length value
        MDL_length = MDL_length + len(master_decision_list)
        #Append the MHL_length to the MDL_length_list
        MDL_length_list.append(MDL_length)        
        #Open the master hand file
        master_file = open("All_Five_Card_Decisions.txt","a+")
        for j in range(len(master_decision_list)):
            #Loop through each particular decision in the master decision list
            for k in range(len(master_decision_list[j])):
                #Print each element in the master hand list to a text file
                master_file.write(str(master_decision_list[j][k])),
                #Print spaces in between each list element
                master_file.write(" ")
            #Print new line command
            master_file.write('\n')
        #Close the master hand file
        master_file.close()
#QUADRUPLE CARD DECISIONS
    #Card 1 ranges from 1 to 49
    for c1 in range(1,50):
        #Initialize the master decision list
        master_decision_list = []
        #Card 2 ranges from 2 to 50
        for c2 in range((c1+1),51):
            #Card 3 ranges from 3 to 51
            for c3 in range((c2+1),52):
                #Card 4 ranges from 4 to 52
                for c4 in range((c3+1),53):
                    #Set the list of decision values
                    hand = [c1,c2,c3,c4]
                    #Append the hand to the master list
                    master_decision_list.append(hand)
        #Calculate progressive MDL_length value
        MDL_length = MDL_length + len(master_decision_list)
        #Append the MHL_length to the MDL_length_list
        MDL_length_list.append(MDL_length)        
        #Open the master hand file
        master_file = open("All_Five_Card_Decisions.txt","a+")
        for j in range(len(master_decision_list)):
            #Loop through each particular decision in the master decision list
            for k in range(len(master_decision_list[j])):
                #Print each element in the master hand list to a text file
                master_file.write(str(master_decision_list[j][k])),
                #Print spaces in between each list element
                master_file.write(" ")
            #Print new line command
            master_file.write('\n')
        #Close the master hand file
        master_file.close()
    #Append the time for each Card 1 iteration
    delta_time = time.time() - start_time
    times.append(delta_time)
    print(delta_time)
#QUINTUPLE CARD DECISIONS
    #Initialize QUINTUPLE DECISION start time
    start_time = time.time()
    #Card 1 ranges from 1 to 48
    for c1 in range(1,49):
        #Initialize the master decision list
        master_decision_list = []
        #Card 2 ranges from 2 to 49
        for c2 in range((c1+1),50):
            #Card 3 ranges from 3 to 50
            for c3 in range((c2+1),51):
                #Card 4 ranges from 4 to 51
                for c4 in range((c3+1),52):
                    for c5 in range((c4+1),53):
                        #Set the list of decision values
                        hand = [c1,c2,c3,c4,c5]
                        #Append the hand to the master list
                        master_decision_list.append(hand)
        #Calculate progressive MDL_length value
        MDL_length = MDL_length + len(master_decision_list)
        #Append the MHL_length to the MDL_length_list
        MDL_length_list.append(MDL_length)
        #Open the master hand file
        master_file = open("All_Five_Card_Decisions.txt","a+")
        for j in range(len(master_decision_list)):
            #Loop through each particular decision in the master decision list
            for k in range(len(master_decision_list[j])):
                #Print each element in the master hand list to a text file
                master_file.write(str(master_decision_list[j][k])),
                #Print spaces in between each list element
                master_file.write(" ")
            #Print new line command
            master_file.write('\n')
        #Close the master hand file
        master_file.close()
    #Append the time for QUINTUPLE DECISION time
    delta_time = time.time() - start_time
    times.append(delta_time)
    print(delta_time)
    #Open the MDL_list text file
    MDL_file = open("Master_Decision_Lengths.txt","w+")
    #Loop through the MDL_length_list
    for i in range(len(MDL_length_list)):
        #Print the MDL_lengths to a text file
        MDL_file.write(str(MDL_length_list[i]))
        #Print the new line command
        MDL_file.write('\n')
    #Close the times file
    MDL_file.close()
    #Open the delta times text file
    times_file = open("Master_Decision_Times.txt","w+")
    #Loop through the times list
    for i in range(len(times)):
        #Print the delta times to a text file
        times_file.write(str(times[i]))
        #Print the new line command
        times_file.write('\n')
    #Close the times file
    times_file.close()
    
Generate_Hands()
