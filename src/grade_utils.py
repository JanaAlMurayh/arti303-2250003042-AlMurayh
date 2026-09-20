def letter_grade(gpa: float) -> str:
    if gpa >= 4.50: return "A"
    if gpa >= 3.50: return "B"
    if gpa >= 2.50: return "C"
    if gpa >= 1.50: return "D"
    return "F"

def is_dean_list(gpa: float) -> bool:
    return gpa >= 4.50
