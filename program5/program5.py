import numpy as np
# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Your Name(, Your Partner's Name)      
# Last Modified:              
# ---------------------------------------------
# A brief overview of the program.
# ---------------------------------------------

#brief notes on this lab:

    #editing wacky package sereies... it has: numpy array of cards

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)       #set size of array
                                                                        #cause arrays have
                                                                        #set lengths

# Place the missing methods here.  Do not modify the code below or above.

    #adds each card as a file
    #not returning anything
    #just updating self.cards with each line (individual card)
    def read_series_information(self, info_file):
            
        #open 
        series = open(info_file, "r")

        #in each line
        input_line = series.readline()
        while input_line:
            info_list = input_line.strip().split(",")
            self.number = str(info_list[0])               # number
            self.name = info_list[1]                      # name
            self.value = str(info_list[2])        # value

            
            
            input_line = series.readline()
            
        
        
        #close
        series.close()


    #read through mycards.csv and update cards_owned for every single card

    #in mcards.csv theres a weird formatt
    def read_collection_information(self, owned_file):

                                                #XXX first strip string then run
                                                #    through join thing
        #strip 
        #thing = " ".join(my_str.split())
        pass


    def __str__(self):
        #XXX don't print in string method only return them
        # return "{:<10}{:25}{:10.2}{:10}".format(self.number, self.name, self.value, "0")

        # ans = self.number + " "*(9 - len(self.number)) + self.name + " "*(24 - len(self.name))
        ans = self.number + " " + self.name + " " + self.value
        return ans
    
    #calculate value of all cards in your collection
    def collection_value(self):
        #if card is owned (ie = 1+)
        #add value to sum
        #.... you get the rest

        pass


    #no other language does this btw
    #
    #number of cards missing = ...
    #cost of purchasing missing cards = ...
    def determine_missing_information(self):

        #return missing_cards, missing_card_cost
        pass
    

# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        # return "{:<10}{:25}{:10.2}{:10}".format(self.number, self.description, self.value, self.cards_owned)
    
        ans = self.number + " "*(9 - len(self.number)) + self.description + " "*(24 - len(self.description)) + "                 " + str(self.cards_owned)
        return ans


    def get_number(self):
        return self.number

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_cards_owned(self):
        return self.cards_owned

    def set_cards_owned(self, number):
        self.cards_owned = number

# ---------------------------------------------

def main():
    my_collection = WackyPackageSeries("Topps", 1973, 30)
    my_collection.read_series_information("series1.csv")
    print(my_collection)
    # my_collection.read_collection_information("mycards.csv")
    # print(my_collection)
    # print("Value of collection = ${:.2}".format(my_collection.collection_value()))
    # number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    # print("Number of missing cards =", number_of_missing_cards)
    # print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()