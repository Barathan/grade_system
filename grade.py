# grade_system.py

def get_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    elif 0 <= mark < 60:
        return "E"
    else:
        return None


try:
    mark = float(input("Enter a mark (0-100): "))

    grade = get_grade(mark)

    if grade is not None:
        print(f"Mark entered: {mark}")
        print(f"Grade: {grade}")
    else:
        print("Invalid mark. Please enter a value between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a numeric value.")