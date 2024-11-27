import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Alex Stergios                         |
# Last Modified: 6/12/23                |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

#7 things to do
#write pokemon class
#write print_menu function
#write print_pokedex function
#write lookup_by_name function
#write total_by_type function
#write average_hit_points function
#continue or stop thing

# Your solution goes here ...

#class start

class Pokemon:

    #init
    def __init__(self, init_name, init_number, init_combat_points, init_types):
        self.name = init_name
        self.number = init_number
        self.combat_points = init_combat_points
        self.types = init_types

        #XXX types is a list

    def __str__(self): 
        answer = str(self.types[0]) 
        if len(self.types) > 1:    
            for i in range(len(self.types)-1):
                answer += " and " + str(self.types[i+1])


        return "Number: " + str(self.number) + ", " +str(self.name).capitalize() + ", CP: " + str(self.combat_points) + ", Type: " + answer
     
#class end


#other function start
def print_menu():
    print("1. Print Pokedex\n2. Print Pokemon by Name\n3. Print Pokemon by Number\n4. Count Pokemon with Type\n5. Print Average Pokemon Combat Points\n6. Quit\n")
    

def print_pokedex(dex_list):
    print("\nThe Pokedex\n-----------")

    completed_list = []
    i = 0
    while len(dex_list) != len(completed_list):
        print(str(dex_list[i]))
        
        completed_list.append(dex_list[i])
        i += 1
    
       
def lookup_by_name(dex_list, name):
    completed_list = []
    i = 0
    found_answer = False
    
    while len(dex_list) != len(completed_list):       
        
        
        if name.lower() == dex_list[i].name:
            found_answer = True
            break
        
        completed_list.append(dex_list[i].number)
        i += 1  
    
    if found_answer == True:
        print(dex_list[i])
    else:
        print("There is no Pokemon named " + name)
    
  
def lookup_by_number(dex_list, number):
    # print(str(dex_list[number-1]))
    
    num_list = []
    i = 0
    while len(dex_list) != len(num_list):
        num_list.append(dex_list[i].number)
        i += 1
    
    if number in num_list:
         print(str(dex_list[number-1]))
    
    else:
        print("There is no pokemon number " + str(number))
    
        
    
        
        


def total_by_type(dex_list, pokemon_type):
    number = 0
    completed_list = []
    i = 0
    while len(dex_list) != len(completed_list):      
        #check each pokemon and find their types
        element_types = dex_list[i].types
        
        
        #compare with asked type
        if str(pokemon_type.lower()) in str(element_types):
            number += 1
            
        else:
            number += 0
            
        completed_list.append(dex_list[i])
        i += 1
    print("Number of Pokemon that contain type " + str(pokemon_type) + " = " +str(number))
        

def average_hit_points(dex_list):
    average = 0
    completed_list = []
    i = 0
    while len(dex_list) != len(completed_list):        
        average += dex_list[i].combat_points
        
        completed_list.append(dex_list[i])
        i += 1
        
        t = average / i
        
        answer = round(t, 2)

    print("Average CP: " + str(answer))
        


#other function end

#XXX TO DO:
    #make the type take in all elements of number 810
   



# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()