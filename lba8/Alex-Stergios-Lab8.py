# -----------------------------------------------------
# CSCI 127, Lab 8
# 6/8/23
# Alex Stergios
# -----------------------------------------------------

# Your solution goes here ...
class Contact:

    #construct it
    def __init__(self, init_Fname, init_Lname, init_phone_num):
        self.Fname = init_Fname
        self.Lname = init_Lname
        self.phone_num = init_phone_num
        self.title = ""     
        
    #str stuff but i don't think it really does anything here
    def __str__(self):
        answer = ""
        answer += self.tile + " "
        answer += str(self.Fname) + " "
        answer += str(self.Lname) + "\t\t"
        answer += self.phone_num    
    
    #get/set it
    def set_first_name(self, name):
        self.Fname = name
        # return self.Fname

    #title
    def set_title(self, title):
        self.title = title     
        
    #full cell number
    def get_cell_number(self):
        return self.phone_num
    
    #first 3 chars of cell number
    def get_area_code(self):
        self.area_code = self.phone_num[0:3]
        return self.area_code

    
    #print all info needed
    def print_entry(self):
        answer = ""   
        
        #title specifics
        if self.title != "":
            answer += self.title + " "
            adjust = len(self.title) + len(self.Fname) + len(self.Lname) + 3
        else:
            adjust = len(self.Fname) + len(self.Lname) + 2
        
        #everything else
        answer += str(self.Fname) + " "
        answer += str(self.Lname) + (26 - adjust)*" "
        answer += self.phone_num
        
        print(answer)
   
    
# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("Jake", "Chipps", "406-123-4567")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()