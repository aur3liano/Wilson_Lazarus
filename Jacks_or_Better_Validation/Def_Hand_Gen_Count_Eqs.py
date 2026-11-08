# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 07:29:04 2021

@author: Justin Paul
"""

def main():
    N = 52
    
    '''
    zero
    '''
    print('Decisions for zero cards: ',str(1))
    print()
    
    '''
    one
    '''
    print('Decisions for one card: ',str(52))
    print()
    
    '''
    two
    '''
    combo_2_sum = 0
    for i in range(1,N):
        combo_2_sum += (N-i)
    print('Decisions for two cards: ',str(combo_2_sum))
    print()
    
    '''
    three
    '''
    combo_3_sum = 0
    for i in range(1,N-1):
        for j in range((i+1),N):
            combo_3_sum += (N-j)
    print('Decisions for three cards: ',str(combo_3_sum))
    print()
    
    '''
    four
    '''
    combo_4_sum = 0
    for i in range(1,N-2):
        for j in range((i+1),N-1):
            for k in range((j+1),N):
                combo_4_sum += (N-k)
    print('Decisions for four cards: ',str(combo_4_sum))
    print()
    
    
    combo_5_sum = 0
    for i in range(1,N-3):
        for j in range((i+1),(N-2)):
            for k in range((j+1),(N-1)):
                for m in range((k+1),N):
                    combo_5_sum += (N-m)
    print('Decisions for five cards: ',str(combo_5_sum))
    print()
    
    
    return(1)

#One Card Decision Count
def One_Card_Dec_Count():
    dec_list = []
    for c1 in range(1,53):
        decision = [c1]
        dec_list.append(decision)
    print(decision)
    print()

#Two Card Decision Count
def Two_Card_Dec_Count():
    dec_list = []
    for c1 in range(1,52):
        for c2 in range((c1+1),53):
            decision = [c1,c2]
            dec_list.append(decision)
    print(decision)
    print()

#Three Card Decision Count
def Three_Card_Dec_Count():
    dec_list = []
    for c1 in range(1,51):
        for c2 in range((c1+1),52):
            for c3 in range((c2+1),53):
                decision = [c1,c2,c3]
                dec_list.append(decision)
    print(decision)
    print()

#Four Card Decision Count
def Four_Card_Dec_Count():
    dec_list = []
    for c1 in range(1,50):
        for c2 in range((c1+1),51):
            for c3 in range((c2+1),52):
                for c4 in range((c3+1),53):
                    decision = [c1,c2,c3,c4]
                    dec_list.append(decision)
    print(decision)
    print()
    
#Five Card Decision Count
def Five_Card_Dec_Count():
    full_dec_list = []
    for c1 in range(1,49):
        for c2 in range((c1+1),50):
            for c3 in range((c2+1),51):
                for c4 in range((c3+1),52):
                    for c5 in range((c4+1),53):
                        decision = [c1,c2,c3,c4,c5]
                        full_dec_list.append(decision)
    print(decision)
    print()
    
#main()
One_Card_Dec_Count()
Two_Card_Dec_Count()
Three_Card_Dec_Count()
Four_Card_Dec_Count()
Five_Card_Dec_Count()