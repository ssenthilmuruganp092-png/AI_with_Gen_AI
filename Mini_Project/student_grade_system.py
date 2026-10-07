"""
Student Grade Management System
Uses: variables, data types, strings, conditions, loops, functions, modules.
"""
import grade_utils as gu

SUBJECTS = ["Maths", "Science", "English"]
students = {}   # {roll_no: {"name": str, "marks": {subject: float}}}


def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("  ! Roll number already exists.")
        return
    name = input("Enter student name: ").strip().title()
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                value = float(input(f"  Marks in {subject} (0-100): "))
            except ValueError:
                print("  ! Please enter a number.")
                continue
            if gu.is_valid_mark(value):
                marks[subject] = value
                break
            print("  ! Marks must be between 0 and 100.")
    students[roll] = {"name": name, "marks": marks}
    print(f"  Student '{name}' added successfully.")


def view_student():
    roll = input("Enter roll number: ").strip()
    student = students.get(roll)
    if student is None:
        print("  ! Student not found.")
        return
    avg = gu.calculate_average(list(student["marks"].values()))
    print(f"\n  Name   : {student['name']}  (Roll {roll})")
    for subject, mark in student["marks"].items():
        print(f"  {subject:<8}: {mark:.1f}")
    print(f"  Average: {avg:.2f} | Grade: {gu.assign_grade(avg)} | Result: {gu.get_result(avg)}")


def show_report():
    if not students:
        print("  No students yet.")
        return
    print(f"\n{'Roll':<6}{'Name':<12}{'Average':>8}{'Grade':>7}{'Result':>8}")
    print("-" * 41)
    for roll, s in students.items():
        avg = gu.calculate_average(list(s["marks"].values()))
        print(f"{roll:<6}{s['name']:<12}{avg:>8.2f}{gu.assign_grade(avg):>7}{gu.get_result(avg):>8}")


def show_topper():
    if not students:
        print("  No students yet.")
        return
    best = max(students.items(),
               key=lambda item: gu.calculate_average(list(item[1]["marks"].values())))
    avg = gu.calculate_average(list(best[1]["marks"].values()))
    print(f"  Topper: {best[1]['name']} (Roll {best[0]}) with average {avg:.2f}")


def main():
    menu = {"1": ("Add student", add_student), "2": ("View student", view_student),
            "3": ("Class report", show_report), "4": ("Show topper", show_topper)}
    while True:
        print("\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  ! Invalid choice, try again.")


if __name__ == "__main__":
    main()