# --------------------------------------
# CSCI 127, Lab 6                      |
# 6/4/23                               |
# Alex Stergios                        |
# --------------------------------------
#removed location.full column

#modified the grades example used in class to make csv into list

# The missing functions go here.
def average_magnitude(file):
    earthquakes = open(file,"r")

    # Create empty list to store unclean strings from csv
    uber_list = []

    # Loop through each row of file and split string to list
    for row in earthquakes:
        uber_list.append( row.split(",") )

    # Create empty list to store cleaned strings from csv
    empty_list = []

    # Strip each string and append to each row
    # Append each row to cleaned strings list
    row_num = 0
    for row in uber_list:
        row_list = []
        for item in row:
            row_list.append( item.strip() )
            
        empty_list.append( row_list )
        
        #count rows for while loop
        row_num += 1

    i = 1
    sum = 0
    #sum to end of list
    while i != row_num:
        
        row_value = float(uber_list[i][2])
        
        sum += row_value  
        i+=1  
        
    average = sum / row_num       

    earthquakes.close()
    
    return average


    
def earthquake_locations(file):
    earthquakes = open(file,"r")

    # Create empty list to store unclean strings from csv
    uber_list = []

    # Loop through each row of file and split string to list
    for row in earthquakes:
        uber_list.append( row.split(",") )

    # Create empty list to store cleaned strings from csv
    empty_list = []

    # Strip each string and append to each row
    # Append each row to cleaned strings list
    row_num = 0
    for row in uber_list:
        row_list = []
        for item in row:
            row_list.append( item.strip() )
            
        empty_list.append( row_list )
        
        #count rows for while loop
        row_num += 1

    #no duplicates
    locations = []
    location_list = []
    duplicates = []
    j = 1
    
    #location column
    while j != row_num:
    
        add = uber_list[j][8]
        locations.append(add)
        
        for i in locations:
            if i not in location_list:
                location_list.append(i)
            else:
                duplicates.append(i)
        j += 1
    
    
    #print
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    sorted_list = sorted(location_list)
    for k in range(len(location_list)):
        answer = sorted_list[k]
        print(str(k+1)+ ". " + answer)
        
    print("\n")



def count_earthquakes(file, lower, upper):
    
    lower_number = float(lower)
    upper_number = float(upper)
    
    earthquakes = open(file,"r")

    # Create empty list to store unclean strings from csv
    uber_list = []

    # Loop through each row of file and split string to list
    for row in earthquakes:
        uber_list.append( row.split(",") )

    # Create empty list to store cleaned strings from csv
    empty_list = []

    # Strip each string and append to each row
    # Append each row to cleaned strings list
    row_num = 0
    for row in uber_list:
        row_list = []
        for item in row:
            row_list.append( item.strip() )
            
        empty_list.append( row_list )
        
        #count rows for while loop
        row_num += 1

    #row_num is total number of earthquakes    
    #now determine if in bounds

    #first find magnitude of each location
    i = 1
    count = 0
    #sum to end of list
    while i != row_num:
        #earthquake magnitude
        row_value = float(uber_list[i][2])
        
        #under upper bound
        if row_value <= upper_number:
            #under lower bound
            if row_value > lower_number:
                count += 1
            else:
                count += 0     
        else:
            count += 0
            
        i += 1
        
    return count



# --------------------------------------

def main(file_name):   
    magnitude = average_magnitude(file_name)
 
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")