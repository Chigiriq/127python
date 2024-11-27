class Student:
    """ student identification or something idk """


    def __init__(self, iName, iYear, iGPA):
        self.name = iName
        self.year = iYear
        self.gpa = iGPA


    def getName(self):
        return self.name

    def getYear(self):
        return self.year
    
    def getGPA(self):
        return self.gpa
    


    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def setGPA(self, gpa):
        self.gpa = gpa




    def __str__(self):
        return "Name: " + self.name + "\nyear: " + str(self.year) + "\ngpa: " + str(self.gpa) + "\n"


student_one = Student("James", 3, 3.8)
print(student_one)

student_two = Student("Meredeth", 2, 4.8)
print(student_two)

student_three = Student("Beth", 4, 2.8)
print(student_three)

students = [student_one, student_two, student_three]

sum = 0 
for student in students:
    sum += student.getGPA()

print("Average GPA: ", sum / len(students), "\n")


#Get president's list

print("------------------------------------------------")
print("President's List Students\n")

pres_list = []
for i in range(len(students)):
    if students[i].getGPA() >= 3.75:
        pres_list.append(students[i])


for student in pres_list:
    print(student)