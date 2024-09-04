#Name: Evan Stackhouse
#Filename: M02CaseStudy.py
#This app will allow the user to input a student's GPA and find out what lists they have made

name = input("Please enter a student's last name or ZZZ to quit: ")

while name != "ZZZ":
    GPA = float(input("Please enter " + name + "'s GPA: "))
    if GPA >= 3.5:
        print(name + " made the Dean's List!")
    elif GPA >= 3.25:
        print(name + " made the Honor Roll!")
    else:
        print(name + " did not make it onto anything.")
    name = input("Please enter the next student's last name or ZZZ to quit the program: ")

print("Program quit!")