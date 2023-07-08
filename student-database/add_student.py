from Student import Student

def initialize():
    answer = input("Would you like to add a student? (y/n)")
    while answer not in ["y", "n"]:
        answer = input("Please type 'y' or 'n'. Would you like to add a student?")
    if answer == "y":
        add_student()
    if answer == "n":
        print("Ok, see ya!")

def add_student(): 

    first_name = input("what is the student's first name?")
    last_name = input("what is the student's last name?")
    instrument = input("what is the student's instrument?")
    grade = input("what is the student's grade?")
    is_active = input("Is the student active?")
    database = open("./database.txt", "a")
    database.write(f"{first_name}, {last_name}, {instrument}, {grade}, {is_active}\n")
    database.close()
    initialize()

initialize()


    


