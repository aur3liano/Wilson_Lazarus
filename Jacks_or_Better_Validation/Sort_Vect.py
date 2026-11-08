# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:05:53 2019

This script sorts a vector of values

@author: justin.l.paul3
"""

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

def Sort_2D_List(Row_List_2D):
    #Build the columns of the 2D list
    Col_List_2D = []
    for c in range(len(Row_List_2D[0])):
        col = []
        for r in range(len(Row_List_2D)):
            col.append(Row_List_2D[r][c])
        Col_List_2D.append(col)
    '''
    Sort by row and column procedure
    '''
    for cl2 in range(Col_List_2D):
        #Sort each column
        [sorted_col_vect, sorted_ide_vect] = Sort_1D_List(Col_List_2D[cl2])
        #Reorganize the rows by the column
        #For each unique element in each sorted column sort the proceeding columns
    return(1)
    
def Rand_List_Gen(n):
    #Import the random library
    import random
    #Generate a list of random values
    Vect = [0]*n
    for v in range(len(Vect)):
        Vect[v] = random.randint(1,3)
    return(Vect)
    
def Test_Sort():
    avg_norm = [-0.642036436851864,-0.582363002265105,-0.578506503401081,-0.53017656858062, -0.57040742776234, -0.573447256278688, 1,-0.693643325646017,
                -0.721242331944823,-0.70042579856492, -0.536660280544241,-0.720431653937224,-0.703112935065291,-0.672522895019338,-0.692607506861229,
                -0.186653688970156, 0.1047717860084,   0.1116227428139,   0.10766009392565, -0.798027321646558,-0.798063275687022,-0.819438808791277,
                -0.79805557124978, -0.798099229727485,-0.819424255965375,-0.797854399832899,-0.692469683039452,-0.692462834650792,-0.6928677456303,
                -0.841997401036504,-0.841928061101324,-0.856048582469152]

    min_norm = [-0.654133432447834,-0.611189171038459,-0.602422910370632,-0.591770128777076,-0.593135959461168,-0.597436668977938, 1,-0.711051803009886,
                -0.738750430637867,-0.7167706738883,  -0.550239630894288,-0.737684629171736,-0.719040080938115,-0.689832585440733,-0.709008290051502,
                -0.209055823750278, 0.097826968614676, 0.102922232252269, 0.101327018764909,-0.813395781275211,-0.813393164741334,-0.83518017016192,
                -0.813424563147865,-0.813512653121743,-0.835147027399471,-0.813135000065413,-0.705946073236783,-0.7062085988025,  -0.706425771114338,
                -0.857946631430677,-0.857895172931085,-0.872177959190793]

    max_norm = [-0.630378670708004,-0.55458365167458, -0.55545861731894, -0.470819769684836,-0.548504279430911,-0.550329015659448, 1,-0.67686703463973,
                -0.704370037343635,-0.684674485043635,-0.5235740623537,  -0.703805218022779,-0.687764181209503,-0.655841803521884,-0.676802315759216,
                -0.165065084500164, 0.11146440335496,  0.120007295582894, 0.113763184370643,-0.783216965424148,-0.78329008935408, -0.80426909270013,
                -0.783244702087226,-0.783245542592168,-0.804272454719897,-0.783128712405264,-0.679482686018453,-0.679216245951918,-0.679802077896317,
                -0.82662736465559, -0.82654079264659, -0.840504941748805]
    #Sort the average norm vector
    [sort_avg_vect,sort_avg_ide_vect] = Sort_1D_List(avg_norm)
    #Sort the minimum norm vector
    [sort_min_vect,sort_min_ide_vect] = Sort_1D_List(min_norm)
    #Sort the maximum norm vector
    [sort_max_vect,sort_max_ide_vect] = Sort_1D_List(max_norm)
    #Print the results to a text file
    sorted_vals_file = open("Sorted_Vals.txt","a+")
    for i in range(len(sort_avg_vect)):
        sorted_vals_file.write(str(sort_avg_vect[i]))
        sorted_vals_file.write("\t")
        sorted_vals_file.write(str(sort_avg_ide_vect[i]))
        sorted_vals_file.write("\t")
        sorted_vals_file.write(str(sort_min_vect[i]))
        sorted_vals_file.write("\t")
        sorted_vals_file.write(str(sort_min_ide_vect[i]))
        sorted_vals_file.write("\t")
        sorted_vals_file.write(str(sort_max_vect[i]))
        sorted_vals_file.write("\t")
        sorted_vals_file.write(str(sort_max_ide_vect[i]))
        sorted_vals_file.write("\n")
    sorted_vals_file.close()
    return(sort_avg_vect)

Test_Sort()
