string1 = "msu_college_enrollments.csv"
string2 = "cs_faculty.csv"

def main(line):
    a = line.replace("_", " ")
    b = a.replace(".csv", "")

    spaces = b.count(" ")
    if spaces == 1:
        n = b.find(" ") + 2
        print(b[:n].upper() + b[n:])
    else:
        n1 = b.find(" ") + 2
        n2 = b.rfind(" ") + 1
        print(b[:n1].upper() + b[n1:n2] + b[n2].upper() + b[n2+1:])    
            

main(string1)
main(string2)