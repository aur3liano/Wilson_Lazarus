#This program analyzes the Def_Val_@@@ data files produced by the validation script
#This program ranks the results of each case for each hand in a dictionary format

def Sort_1D_List(Vect):
    #Preserve original unsorted data structures
    old_dynamic_unsort_val = Vect
    #Assign identity to each Vect item
    old_dynamic_unsort_ide = [0]*len(Vect)
    for v in range(len(Vect)):
        old_dynamic_unsort_ide[v] = v
    #Initialize lists to hold sorted values
    sort_ide_vect = [0]*len(Vect)
    sort_val_vect = [0]*len(Vect)
    #Initialize sorted values counter
    val_sort_counter = 0
    #Sort the vector
    while (old_dynamic_unsort_ide != []):
        #Initialize the dynamic minimum
        dynamic_min = float("inf")
        #Find the actual dynamic minimum(s) of the old data structures
        for j in range(len(old_dynamic_unsort_val)):
            if (old_dynamic_unsort_val[j] < dynamic_min):
                dynamic_min = old_dynamic_unsort_val[j]
        #Collect all indicies for values equal to dynamic minimum
        dynamic_min_indices = []
        for j in range(len(old_dynamic_unsort_val)):
            if (old_dynamic_unsort_val[j] == dynamic_min):
                dynamic_min_indices.append(j)
        #Initialize new dynamic data structures for building
        new_dynamic_unsort_val = [0]*(len(old_dynamic_unsort_val)-len(dynamic_min_indices))
        new_dynamic_unsort_ide = [0]*(len(old_dynamic_unsort_ide)-len(dynamic_min_indices))
        #Build the new dynamic data structures
        build_counter = 0
        for k in range(len(old_dynamic_unsort_val)):
            #Exclude the actual dynamic minimum
            if (old_dynamic_unsort_val[k] == dynamic_min):
                continue
            else:
                new_dynamic_unsort_val[build_counter] = old_dynamic_unsort_val[k]
                new_dynamic_unsort_ide[build_counter] = old_dynamic_unsort_ide[k]
                build_counter += 1
        #Pass the actual dynamic minimum to the sorted data structures
        for m in range(len(dynamic_min_indices)):
            sort_ide_vect[val_sort_counter] = old_dynamic_unsort_ide[dynamic_min_indices[m]]
            sort_val_vect[val_sort_counter] = dynamic_min
            #Increment the sorted values counter
            val_sort_counter += 1
        #Reset the old dynamic data structures
        old_dynamic_unsort_ide = new_dynamic_unsort_ide
        old_dynamic_unsort_val = new_dynamic_unsort_val
    return(sort_val_vect,sort_ide_vect)

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
    #Open Scores file for writing
    Scs_file = open("Def_Val_Scs.txt","a+")
    #Decompose master lists into hand lists for each hand recorded
    for i in range(len(Hnd_Mat)):
        #Pull data lists from each matrix
        crds = Hnd_Mat[i]
        avgs = Avg_Mat[i]
        errs = Err_Mat[i]
        tims = Tim_Mat[i]
        #Initialize lists for sorting
        old_dynamic_avgs = avgs
        #Sort the list of averages while preserving identity
        [sorted_avgs,sorted_ides] = Sort_1D_List(old_dynamic_avgs)
        #Initialize list of sorted errors
        sorted_errs = [0]*len(sorted_ides)
        #Initialize the list of sorted times
        sorted_tims = [0]*len(sorted_ides)
        for k in range(len(errs)):
            #Use the identity list to generate the sorted error list
            sorted_errs[sorted_ides[k]] = errs[k]
            #Use the identity list to generate the sorted times list
            sorted_tims[sorted_ides[k]] = tims[k]
        #Calculate the scores
        Scores = []
        for m in range(len(sorted_avgs)):
            #Calculate score components
            low = (avgs[i]-errs[i])*(1/3)
            med = (avgs[i])*(1/3)
            high = (avgs[i]+errs[i])*(1/3)
            #Calculate the total score
            tot_score = low+med+high
            #Append the score
            Scores.append(tot_score)
        #Print scores to the score file
        for n in range(len(Scores)):
            scor = str(Scores[n])
            Scs_file.write(scor)
    Scs_file.close()
    return(1)

Def_Val_Analysis()
