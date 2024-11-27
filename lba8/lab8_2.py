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

    def set_title(self, title):
        self.tile = title     
        
    def get_cell_number(self):
        return self.phone_num
    
    
    def get_area_code(self):
        self.area_code = self.phone_num[0:3]
        return self.area_code

    

    def print_entry(self):
        answer = ""        
        answer += str(self.Fname) + " "
        answer += str(self.Lname) + "\t\t"
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