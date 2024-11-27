#open
census_file = open("census.txt", "r")
summary_file = open("summary.txt", "w")

#read first line
input_line = census_file.readline()
total_population = 0

#loop through file
while input_line:
    row_list = input_line.split()
    total_population += int(row_list[1])

    input_line = census_file.readline()

summary_file.write("\n-----------------------------------\n")
summary_file.write("Total Population " + str(total_population))


#close
census_file.close()
summary_file.close()
