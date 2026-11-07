#This program uses random search to confirm my conjecture:
#there are a total of 32 unique combinations for a 5 card hand
#in the palindromic sequence 1,5,10,10,5,1 for ascending card option quantity

def Com_Gen(n):
    #Import random library
    import random
    #Gather n unique cards
    test_comb = []
    while (len(test_comb) < n):
        #Generate random integer from 1 to 5
        card = random.randint(1,5)
        #Test if card is repeated
        if (card not in test_comb):
            test_comb.append(card)
    #Order test_comb chronologically
    test_comb.sort()
    #Give the test_comb back to Search
    return(test_comb)

def Search():
    #Initialize count directory
    count_dict = {}
    for i in range(5):
        count_dict[i] = 0
    #Initialize number of random tests
    #(almost garunteed test quantity independent result above 40 tests which is 4X max option value)
    num_tests = 100
    #Enter trivial option values
    count_dict[0] = 1
    count_dict[1] = 5
    count_dict[5] = 1
    #Find the rest of the option values
    for i in range(2,5):
        #Initialize uniq_com_list
        uniq_com_list = []
        #Initialize option count
        opt_count = 0
        #Initiate random tests
        for j in range(1,num_tests):
            #Acquire test combination
            test_comb = Com_Gen(i)
            #Check if test_comb is unique
            if (test_comb not in uniq_com_list):
                opt_count = opt_count + 1
                uniq_com_list.append(test_comb)
        #Update value of option in count dictionary
        count_dict[i] = opt_count
        #Set unique combination list
        if (i == 2):
            two_list = uniq_com_list
        elif (i == 3):
            three_list = uniq_com_list
        elif (i == 4):
            four_list = uniq_com_list
    #Print option values for zero cards
    print("Zero")
    zero_list = [[]]
    print(zero_list[0])
    #Print option values for one card
    print("One")
    one_list = []
    for k in range(1,6):
        print([k])
        #Build one list
        one_list.append([k])
    #Order unique two combination lists
    two_list.sort()
    #Print two list
    print("Two")
    for k in range(len(two_list)):
        two = two_list[k]
        print(two)
    #Order unique three combination lists
    three_list.sort()
    #Print two list
    print("Three")
    for k in range(len(three_list)):
        three = three_list[k]
        print(three)
    #Order unique four combination lists
    four_list.sort()
    #Print four list
    print("Four")
    for k in range(len(four_list)):
        four = four_list[k]
        print(four)
    #Print unique five combination lists
    print("Five")
    five_list = [[1,2,3,4,5]]
    print(five_list[0])
    #Compile master list
    master_list = [zero_list,one_list,two_list,three_list,four_list,five_list]
    #Test master list construction
    print("Master List")
    for m in range(6):
        internal_list = master_list[m]
        for i in range(len(internal_list)):
            print(master_list[m][i])
    print()
    #Print compiled master list
    print(master_list)
    print()
    #Sum the final option values
    fin_opt_vals = 0
    for n in range(len(count_dict)):
        opt_val = count_dict[n]
        fin_opt_vals = fin_opt_vals + opt_val
    #Print the sum
    print(str(fin_opt_vals),"possible unique card combinations")
    #Print the count dictionary
    print(count_dict)

Search()
