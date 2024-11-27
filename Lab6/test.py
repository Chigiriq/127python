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
    grades_list = []

    # Strip each string and append to each row
    # Append each row to cleaned strings list
    row_num = 0
    for row in uber_list:
        row_list = []
        for item in row:
            row_list.append( item.strip() )
            
        grades_list.append( row_list )
        
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
        print(row_value)
        
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
        

    

    
        
        
# lower_bound = float(input("Enter a lower bound for the magnitude: "))
# upper_bound = float(input("Enter an upper bound for the magnitude: "))
print(count_earthquakes("earthquakes.csv", 5.0, 6.0))
