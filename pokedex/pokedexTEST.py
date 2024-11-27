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


    def __str__(self):
        if len(self.types) > 1:
            answer = str(self.types[0]) + " and "+ str(self.types[1])

        else:
            answer = self.types = str(self.types[0])


        return "Number: " + str(self.number) + ", " +str(self.name) + ", CP: " + str(self.combat_points) + ", Type: " + answer
 
        #loop through each pokemon in pokedex and print to avoid printing ram locations


    
#class end

#other function start  

def print_pokedex(dex_list):
    print("\nThe Pokedex\n-----------")

    # for i in range(0, 31):
    #     print(str(dex_list[i]))
    completed_list = []
    i = 0
    while len(dex_list) != len(completed_list):
        print(str(dex_list[i]))
        
        completed_list.append(dex_list[i])
        i += 1


#other function end

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


# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex2.txt")
 
    
    # print_pokedex(pokedex)
    print(pokedex[24].types[0])
# ---------------------------------------

main()