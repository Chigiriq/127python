import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# Date                             |
# Your Name                                       |
# -------------------------------------------------

def read_file(file_name):
    data = open(file_name, "r")
    
    data_list = []
    names = []
    enrollment = []
    input_line = data.readline()
    i = 0
    
    
    #collect name and enrollment
    while input_line:        
        data_list = input_line.strip().split(",")
        
        if len(data_list) == 1:
            length = data_list[0]
            
        else:
            names.append(data_list[0])
            enrollment.append(int(data_list[1]))
        
        i += 1
        input_line = data.readline()
    data.close()   
    
    #apply name and enrollment lists to array
    college_names = np.array(names)
    college_enrollments = np.array(enrollment)
    
    #y-ticks
    ticks = 4600 // 400
    tick_list = [0]
    add = 400
    for i in range(ticks):
        tick_list.append(add)
        add += 400
        
    
    #plot and return
    plt.bar(college_names, college_enrollments, width=0.8, bottom=0,  color=['blue', 'gold'])
    plt.ylim(top = 4600)
    plt.xlabel("College Name")
    plt.ylabel("College Enrollment")
    plt.yticks(tick_list)
    plt.show()
    
    return college_names, college_enrollments
    

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)

# -------------------------------------------------

main("fall-2019.csv")