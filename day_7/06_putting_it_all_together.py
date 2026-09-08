# ---------------------------------------------------------
# DAY 7 | TOPIC 6: PUTTING IT ALL TOGETHER 🏗️
# A mini-project that uses everything from Day 6 & Day 7.
# ---------------------------------------------------------
#
# PROJECT: STUDENT GRADE MANAGER
# We'll build a program that can store students, record their scores,
# calculate stats, and print a full report — all using functions!
#
# Concepts used:
#   ✅ def, parameters, return  (Day 6)
#   ✅ default parameters        (Day 6)
#   ✅ keyword arguments         (Day 6)
#   ✅ multiple return values    (Day 7)
#   ✅ *args                     (Day 7)
#   ✅ **kwargs                  (Day 7)
#   ✅ functions calling functions (Day 7)
# ---------------------------------------------------------


# Helper Functions
def calculate_average(*scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average  # multiple return


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_status(grade):
    if grade == "F":
        return "Fail"
    return "Pass"


# Builder Function
def create_student(name, *scores, school="ABC School", **extras):
    total, average = calculate_average(*scores)
    grade = get_grade(average)
    status = get_status(grade)

    student = {
        "name": name,
        "scores": scores,
        "total": total,
        "average": average,
        "grade": grade,
        "status": status,
        "school": school
    }

    student.update(extras)
    return student


# Printer Function
def print_report_card(student):
    print("\n===== REPORT CARD =====")
    print("Name:", student["name"])
    print("Scores:", student["scores"])
    print("Total:", student["total"])
    print("Average:", round(student["average"], 2))
    print("Grade:", student["grade"])
    print("Status:", student["status"])

    for key, value in student.items():
        if key not in ["name", "scores", "total", "average", "grade", "status"]:
            print(f"{key.title()}: {value}")


# Class Summary Function
def class_summary(students):
    print("\n===== CLASS SUMMARY =====")

    total_avg = 0

    for student in students:
        total_avg += student["average"]
        print(f"{student['name']} -> {student['grade']} ({student['status']})")

    class_avg = total_avg / len(students)
    print(f"\nClass Average: {class_avg:.2f}")


# Main Program
student1 = create_student(
    "Bibek",
    85, 90, 88,
    age=20,
    city="Kathmandu"
)

student2 = create_student(
    "Sita",
    95, 92, 98,
    age=19,
    city="Pokhara"
)

student3 = create_student(
    "Ram",
    65, 70, 68,
    age=21,
    city="Butwal"
)

students = [student1, student2, student3]

# Print individual report cards
for student in students:
    print_report_card(student)

# Print class summary
class_summary(students)