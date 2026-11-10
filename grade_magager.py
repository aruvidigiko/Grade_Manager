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


# ---- Temporary tests (we'll delete these later) ----
print(get_grade(100))
print(get_grade(90))
print(get_grade(89))
print(get_grade(80))
print(get_grade(60))
print(get_grade(59))
print(get_grade(0))