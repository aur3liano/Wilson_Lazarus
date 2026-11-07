#This program completes targeted definitive validation
#of all possible unique decisions for 5 cards of 52 different values

def Zero_Cards(reward_vector):
    #Establish baseline probabilities
    All_Hands_Count = 2598960
    Baseline_Reward_Count = [1098240 123552 54912 10200 5108 3744 624 36 4]
    Baseline_Probabilities = [0] * len(Baseline_Reward_Count)
    for bp in range(len(Baseline_Reward_Count)):
        Baseline_Probabilities[bp] = Baseline_Reward_Count[bp]/All_Hands_Count
    #Calculate Baseline BNG
    Baseline_BNG = 0
    for bng in range(len(reward_vector)):
        Baseline_BNG = Baseline_BNG + (Baseline_Probabilities[bng]*reward_vector[bng])
    Baseline_BNG = (1*Baseline_BNG)-1
    #Set Baseline Probability Errors
    Baseline_Probability_Errors = [0] * len(Baseline_Reward_Count)
    return(Baseline_BNG,Baseline_Probabilities,Baseline_Probability_Errors)

def Five_Cards(reward_vector):
    #Import Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
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
                        #Evaluate the decision
                        reward

def Validate():
    #Import Jacks_or_Better_4WL
    import Jacks_or_Better_4WL
    #Establish reward vector for all decisions
    Reward_Vect_Baseline = [3.25,8.89,20,107.67,215,293.33,1760,30506.67,274560]
    Reward_Vect_Gain = 0.065735472679572 #Reward gain converged to baseline BNG of -75% as somewhat arbitrary
    reward_vector = [0] * 9
    for rv in range(len(Reward_Vect_Baseline)):
        reward_vector[rv] = Reward_Vect_Baseline[rv] * Reward_Vect_Gain
    
        
