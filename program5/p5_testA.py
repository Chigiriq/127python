import numpy as np

# ---------------------------------------------
# CSCI 127, Joy and Beauty of Data      
# Program 5: Wacky Packages
# Your Name(, Your Partner's Name)      
# Last Modified:              
# ---------------------------------------------
# A brief overview of the program.
# ---------------------------------------------

class WackyPackageSeries:
    def __init__(self, manufacturer, year, how_many):
        self.manufacturer = manufacturer
        self.year = year
        self.how_many = how_many
        self.cards = np.ndarray(how_many, dtype=WackyPackageCard)

# Place the missing methods here.  Do not modify the code below or above.

# ---------------------------------------------

    def read_series_information(self, file):
       
        series = open(file, "r")

        print("\nMy", self.year, "collection of", self.manufacturer, "Wacky Packages\n")
        print("Number    Description                   Value     Owned")
        print("------    -----------                   -----     -----")
            
        
        input_line = series.readline()
        i = 0
        while input_line:
            info_list = input_line.strip().split(",")
            number = int(info_list[0])              
            name = info_list[1]                     
            value = float(info_list[2])      
            
            self.cards[i]= WackyPackageCard(number, name, value)    
            input_line = series.readline()
             
              
            print(self.cards[i])
        
            i += 1
            
        series.close()
    
    def __str__(self):
        # return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)
        return "\n"
        pass
 
    
    
    def read_collection_information(self, file):
        
        print("\nMy", self.year, "collection of", self.manufacturer, "Wacky Packages\n")
        print("Number    Description                   Value     Owned")
        print("------    -----------                   -----     -----")
        owned = open(file, "r")
        
        owned_cards = 0
        input_line = owned.readline()
        i = 0
        while input_line:
            owned_cards = 0
            owned_str = input_line.strip()
            clean_str = " ".join(owned_str.split())
            
            #XXX good start but both lists arent sorted to each other
            #make a list of owned cards(sorted) and then a list of all cards sorted
            
            
            #loop self.card through owned cards
            for k in range(3):
                card_str = str(self.cards[k].get_description())
            
                if clean_str.lower() == card_str.lower():
                    owned_cards += 1
                else:
                    owned_cards += 0
        
                print(clean_str.lower(), "\t", card_str.lower())
        
        
            self.cards[i].set_cards_owned(owned_cards)
            print(self.cards[i])
            
            
            input_line = owned.readline()
            i += 1
            # print(clean_str.lower(), "\t", card_str.lower())
            
        owned.close()
        
    
    def collection_value(self):
        pass
    
    def determine_missing_information(self):
        pass
# ---------------------------------------------

class WackyPackageCard:
    def __init__(self, number, description, value):
        self.number = number
        self.description = description
        self.value = value
        self.cards_owned = 0

    def __str__(self):
        return "{:<10d}{:25}{:10.2f}{:10d}".format(self.number, self.description, self.value, self.cards_owned)

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
    my_collection.read_collection_information("mycards.csv")
    print(my_collection)
    # print("Value of collection = ${:.2f}".format(my_collection.collection_value()))
    # number_of_missing_cards, cost_of_missing_cards = my_collection.determine_missing_information()
    # print("Number of missing cards =", number_of_missing_cards)
    # print("Cost of purchasing missing cards = ${:.2f}".format(cost_of_missing_cards))
    
# ---------------------------------------------

main()