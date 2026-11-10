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


def show_results():
    # Guard: nothing to show yet (also prevents dividing by zero)
    if len(students) == 0:
        print("No students added yet. Add a student first.")
        return

    # Table header
    print()
    print(f"{'Name':<12}{'Mark':>6}{'Grade':>8}")
    print("-" * 26)

    # One row per student, and collect the marks for the statistics
    marks = []
    for s in students:
        print(f"{s['name']:<12}{s['mark']:>6}{get_grade(s['mark']):>8}")
        marks.append(s["mark"])

    # Statistics
    average = sum(marks) / len(marks)
    print("-" * 26)
    print(f"Average: {average:.1f}   Highest: {max(marks)}   Lowest: {min(marks)}")
    print()


# ---- Temporary test ----
show_results()        # should say "No students added yet"
add_student()
add_student()
add_student()
show_results()