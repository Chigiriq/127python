import numpy as np
import math

a = [1,3,4,2,5]

straight = 0
roll_list = list(a)
roll_list.sort()

value = roll_list[0]
compare_list = []
for i in range(len(roll_list)):
    
    compare_list.append(value)
    print(roll_list, "\t", compare_list)
    
    if compare_list[i] == roll_list[i]:
        value += 1
        straight = 1
    else:
        straight = 0
        break
    
    


    
print(roll_list)
print(straight)