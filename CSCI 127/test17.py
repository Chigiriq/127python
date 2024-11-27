def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
        
    print(result)
    return result


def four_of_a_kind(ranks):
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)
            

    print(new_ranks_list)
    print(duplicates)

    if len(duplicates) >= 3:
        #find out which n_r_l item is in duplicates
        #index 0 of n_r_l
        if new_ranks_list[0] == duplicates[0] and duplicates[0] == duplicates[1] and duplicates[1] == duplicates[2]:
            return True
        #index 1 of n_r_l
        elif new_ranks_list[1] == duplicates[0] and duplicates[0] == duplicates[1] and duplicates[1] == duplicates[2]:
            return True
        
        else:
            return False
              
    
   
    
    
    
poker_hand = [[2, 'clubs'], [2, 'diamonds'], [2, 'hearts'], [2, 'spades'], [7, 'clubs']]
a = get_all_ranks(poker_hand) 
print(four_of_a_kind(a))