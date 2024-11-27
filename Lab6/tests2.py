earthquakes = open("earthquakes.csv","r")




uber_list =[]

for row in uber_list:
    row_list = []
    for item in row:
        row_list.append( item.strip() )
    earthquakes.append( row_list )

#read first line
input_line = earthquakes.readline()
average = 0
i=1
#loop through file
while input_line:
    row_list = uber_list[i][2]
    average += row_list[1]
    i+=1

    input_line = earthquakes.readline()


earthquakes.close()