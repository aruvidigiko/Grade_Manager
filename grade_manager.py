students = []

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

def add_student() :
    while True :
        name = input("Enter Student Name: ").strip()
        if name == "" :
            print("Name cannot be Empty. Please try again.")
        else :
            break
    while True :
        mark_text = input(f"Enter mark for {name} (0-100) : ").strip()
        try :
            mark = int(mark_text)    
        except ValueError :
            print("Please enter a whole number, e.g. 85")
            continue
        if 0 <= mark <= 100 :
            break
        print("Mark must be between 0 and 100")

    students.append({"name" : name, "mark" : mark}) 
    print(f"Added {name} with mark {mark} (Grade {get_grade(mark)}). ")   


add_student()
add_student()
print(students)