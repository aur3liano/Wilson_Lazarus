#This program analyzes the Def_Val_@@@ data files produced by the validation script
#This program ranks the results of each case for each hand in a dictionary format

def Sort_List_Min_Build(old_dynamic_val_list,old_dynamic_ide_list):
    #Initialize the sorted value list
    sorted_val_list = [0]*len(old_dynamic_val_list)
    #Initialize the sorted identity list
    sorted_ide_list = [0]*len(old_dynamic_val_list)
    #Initialize the sort counter
    sort_counter = 0
    #Continue sorting until the old dynamic value list is empty
    while (len(old_dynamic_val_list) > 0):
        #Initialize the current minimum as greater than the maximum list value
        dynamic_min = max(old_dynamic_val_list) + 1
        #Find the actual current minimum
        for i in range(len(old_dynamic_val_list)):
            if (old_dynamic_val_list[i] < dynamic_min):
                dynamic_min = old_dynamic_val_list[i]
                min_index = i
        #Initialize the new dynamic value list for building
        new_dynamic_val_list = [0]*(len(old_dynamic_val_list)-1)
        #Initialize the new dynamic identity list for building
        new_dynamic_ide_list = [0]*(len(old_dynamic_val_list)-1)
        #Initialize the new dynamic list build counter
        build_counter = 0
        #Build the new dynamic list
        for j in range(len(old_dynamic_val_list)):
            if (j == min_index):
                #Skip the dynamic minimum
                continue
            else
                #Add each element that is not the dynamic minimum
                new_dynamic_val_list[build_counter] = old_dynamic_val_list[j]
                #Increment the build counter
                build_counter = build_counter + 1
        #Build the sorted value list with the dynamic minimum
        sorted_val_list[sort_counter] = dynamic_min
        #Build the sorted identity list with the dynamic minimum
        sorted_ide_list[sort_counter] = old_dynamic_ide_list[min_index]
        #Increment the sort counter
        sort_counter = sort_counter + 1
    return(sorted_val_list,sorted_ide_list)

def Def_Val_Analysis():
    #Open Def_Val_Hnd for reading
    Hnd_file = open("Def_Val_Hnd.txt","r")
    #Read data into a single hand master list
    Hnd_Mat = Hnd_file.readlines()
    Hnd_file.close()
    #Open Def_Val_Avg for reading
    Avg_file = open("Def_Val_Avg.txt","r")
    #Read data into a single averages master list
    Avg_Mat = Avg_file.readlines()
    Avg_file.close()
    #Open Def_Val_Err for reading
    Err_file = open("Def_Val_Err.txt","r")
    #Read data into a single errors master list
    Err_Mat = Err_file.readlines()
    Err_file.close()
    #Open Def_Val_Tim for reading
    Tim_file = open("Def_Val_Tim.txt","r")
    #Read data into a single times master list
    Tim_Mat = Tim_file.readlines()
    Tim_file.close()
    #Decompose master lists into hand lists for each hand recorded
    for i in range(len(Hnd_Mat)):
        #Pull data lists from each matrix
        crds = Hnd_Mat[i]
        avgs = Avg_Mat[i]
        errs = Err_Mat[i]
        tims = Tim_Mat[i]
        #Initialize lists for sorting
        old_dynamic_avgs = avgs
        old_dynamic_ides = [0]*len(avgs)
        for j in range(len(avgs)):
            old_dynamic_ides[j] = j
        #Sort the list of averages while preserving identity
        [sorted_avgs,sorted_ides] = Sort_List_Min_Build(old_dynamic_avgs,old_dynamic_ides)
        #Initialize list of sorted errors
        sorted_errs = [0]*len(sorted_ides)
        #Initialize the list of sorted times
        sorted_tims = [0]*len(sorted_ides)
        for k in range(len(errs)):
            #Use the identity list to generate the sorted error list
            sorted_errs[sorted_ides[k]] = errs[k]
            #Use the identity list to generate the sorted times list
            sorted_tims[sorted_ides[k]] = tims[k]
                

Def_Val_Analysis()
