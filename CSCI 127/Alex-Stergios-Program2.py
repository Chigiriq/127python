# -----------------------------------------+
# Alex Stergios                            |
# CSCI 127, Program 2                      |
# Last Updated: 6/2/23                     |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+

def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):
    suit = hand[0][1]
    card = [10, 11, 12, 13, 14]
    
    for i in range(len(hand)):
        #same suit
        if hand[i][1] == suit:  
            #rflush
            if card[i] == hand[i][0]:
                ans = True  
            #not rfush
            else:
                ans = False
                break    
        #not same suit
        else:
            ans = False
            break
        
    return ans

def straight_flush(hand):
    suit = hand[0][1]
    #straight?
    if straight(hand) == True:
        for i in range(len(hand)):
            #suit
            if hand[i][1] == suit:
                ans = True    
            #not same suit
            else:
                ans = False
                break
    else:
        ans = False
        
        
    return ans
                     
def straight(hand):
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    base = hand[0][0]
    
    index = cards.index(base)
    
    for i in range(len(hand)):
        #consecutive numbers
        if hand[i][0] == cards[index]:
            index += 1
            result = True
        #not consecutive
        else:
            result = False
            break
    
    return result
        
def four_of_a_kind(ranks):
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)
            
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

def full_house(ranks):
    #only validates if there's at least 3 duplicates found (i.e. aabbb or aaabb for a full house)
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)

    if len(duplicates) >= 3:        
        # n_r_l: [a, b]
        # d: [a, b, b]
        if new_ranks_list[0] == duplicates[0] and new_ranks_list[1] == duplicates[1] and duplicates[1] == duplicates[2]:
            return True
        
        
        # n_r_l: [a, b]
        # d: [a, a, b]
        elif new_ranks_list[0] == duplicates[0] and new_ranks_list[1] == duplicates[1] and duplicates[0] == duplicates[1]:
            return True
        
        else:
            return False
        
    else:
        return False

def three_of_a_kind(ranks):
    #only true if full house fails before this
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)
   
    #are two duplicates present    
    if len(duplicates) == 2:
        #are the duplicates equal?
        if duplicates[0] == duplicates[1]:
            return True
        #nope
        else:
            False         
    #not 3 of a kind           
    else:
        return False

def two_pair(ranks):
    #this solution only works so long as 3 of a kind is called and failed before this
    #function assumes that 2 duplicates exist but are different
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)
    
    #are two pairs present      
    if len(duplicates) == 2:
        return True
     
    #not two pairs           
    else:
        return False

def one_pair(ranks):
    new_ranks_list = []
    duplicates = []
    
    for i in ranks:
        if i not in new_ranks_list:
            new_ranks_list.append(i)
        else:
            duplicates.append(i)
    
    duplicate_amount = len(duplicates) + 1
    
    #pair
    if duplicate_amount == 2:
        return True
    
    #not pair
    else:
        return False   


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+

main()