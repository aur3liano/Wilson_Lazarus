#This program runs every conceivable hand combination for the 30 possible unknown decisions that a user could make
#The final (31st) combination simply needs to be evaluated by the reward subroutine
#Once the averages and errors have been collected the combinations are 

def hand_index_conv(test_combination,hand):
    #Cycle through each test combination value to collect hand cards
    second_hand = []
    for i in range(len(test_combination)):
        second_hand.append(hand[test_combination[i]-1])
    return(second_hand)

def Data_Collection(hand):
    #Access the Jacks or Better experimental case study function list
    import Jacks_or_Better_Exp_CS
    #Establish the pallidromic master list
    master_list = [[[]], [[1], [2], [3], [4], [5]], [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]], [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]], [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]], [[1, 2, 3, 4, 5]]]
    #Cycle through each list collecting the the data for each test combination and skip the empty list
    averages = []
    errors = []
    for m in range(1,6):
        internal_list = master_list[m]
        for i in range(len(internal_list)):
            test_combination = master_list[m][i]
            #Convert test_combination to card values
            second_hand = hand_index_conv(test_combination,hand)
            #Obtain average and error for the test combination
            [rel_BNG_avg,rel_BNG_error] = Jacks_or_Better_Exp_CS.Case_Study(hand,second_hand)
            #Concatenate values
            averages.append(rel_BNG_avg)
            errors.append(rel_BNG_error)
    return(averages,errors)

def Definitive_Validation():
    #Access the Jacks or Better experimental case study function list
    import Jacks_or_Better_Exp_CS
    #Open the data file for writing
    file = open("Def_Val.txt","w+")
    #Count the hands processed
    hand_iters = 0
    while (hand_iters < 10):
        #hand iteration counter
        hand_iters = hand_iters + 1
        #Establish experiment parameters
        first_hand = Jacks_or_Better_4WL.Random_Cards(5)
        #Collect validation data for the hand
        [averages,errors] = Data_Collection(first_hand)
        #Print data averages
        for i in range(len(averages)):
            file.write(str(averages[i])),
            file.write(" ")
        file.write('\n')
        #Print data errors
        for j in range(len(errors)):
            file.write(str(errors[j])),
            file.write(" ")
        file.write('\n')
    file.close()

Definitive_Validation()
