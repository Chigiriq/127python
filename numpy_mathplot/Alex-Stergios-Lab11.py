import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# Date
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    #------
    def is_it_low_roll(self):
        is_low = 1

        for i in range(len(self.rolls)):
            if self.rolls[i] > 2:
                is_low = 0
                break 
            
        return is_low
        #otherwise keep looping

    
    def is_it_three_of_a_kind(self):
        is_three = 0

        dup_list = []
        other_list = []
        roll_list = list(self.rolls)
        
        for i in roll_list:
            if i not in other_list:
                other_list.append(i)
            else:
                dup_list.append(i)
        
        
        #are two duplicates present    
        if len(dup_list) == 2:            
            #are the duplicates equal?
            if dup_list[0] == dup_list[1]:
                is_three = 1
            #nope
            else:
                is_three = 0         
        #not 3 of a kind           
        else:
            is_three = 0
            
        return is_three


    def is_it_large_straight(self):
        straight = 0
        roll_list = list(self.rolls)
        roll_list.sort()
        
        value = roll_list[0]
        compare_list = []
        for i in range(len(roll_list)):
            compare_list.append(value)
            
            if compare_list[i] == roll_list[i]:
                value += 1
                straight = 1
            else:
                straight = 0
                break
       
        return straight
                
        


    #------


# -------------------------------------------------


def main(how_many):

    low_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(8)       # 8-sided dice

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_low_roll():
            low_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Low Rolls:", low_rolls)
    print("Percent:", "{:.2f}%\n".format(low_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(20000)
    
        