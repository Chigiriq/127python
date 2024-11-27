import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# Date                              |
# Your Name                                       |
# -------------------------------------------------

def main(file_name):
    # read the file_name into a pandas dataframe
    file = pd.read_csv(file_name)  
    
    get_titles = open(file_name, "r")
    col_list = []
    
    input_line = get_titles.readline()
    while len(col_list) == 0:
        col_list.append(input_line.strip().split(","))
        input_line = get_titles.readline()
    
    get_titles.close()
     
    
    x_title = str(col_list[0][0])
    y_title = str(col_list[0][1])
    
    
    #why did i do this
    a = file_name.replace("_", " ")
    b = a.replace(".csv", "")

    spaces = b.count(" ")
    if spaces == 1:
        n = b.find(" ") + 2
        title_name = b[:n].upper() + b[n:]
    else:
        n1 = b.find(" ") + 2
        n2 = b.rfind(" ") + 1
        title_name = b[:n1].upper() + b[n1:n2] + b[n2].upper() + b[n2+1:]
    #seriously i regret every having worked with strings
    #also im too lazy to use loops 
       
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    file.plot.bar(x=x_title, y=y_title, color=["blue", "gold"], legend = False)
    

    # The only four statements that may use the matplotlib library appear next.
    # # Do not modify them.
    plt.xlabel(x_title)      # Note: x-axis should be determined above
    plt.ylabel(y_title)      # Note: y-axis should be determined above
    plt.title(title_name)
    plt.tight_layout()    
    interactive(False)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("msu_college_enrollments.csv")
main("cs_faculty.csv")