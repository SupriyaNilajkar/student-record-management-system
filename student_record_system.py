# Student Record Management System

students = []


# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'


# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")

    # Prevent duplicate roll numbers
    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("No student records found.\n")
        return

    for student in students:
        print("\n----------------------------")
        print(f"Name     : {student['name']}")
        print(f"Roll No  : {student['roll']}")
        print(f"Marks    : {student['marks']}")
        print(f"Total    : {student['total']}")
        print(f"Average  : {student['average']:.2f}")
        print(f"Grade    : {student['grade']}")
    print("----------------------------\n")


# Function to search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("----------------------------")
            print(f"Name     : {student['name']}")
            print(f"Roll No  : {student['roll']}")
            print(f"Marks    : {student['marks']}")
            print(f"Total    : {student['total']}")
            print(f"Average  : {student['average']:.2f}")
            print(f"Grade    : {student['grade']}")
            print("----------------------------\n")
            return

    print("Student not found!\n")


# Function to display class statistics
def class_statistics():
    if not students:
        print("No student records available.\n")
        return

    total_students = len(students)
    class_total = sum(student["total"] for student in students)
    class_average = class_total / total_students

    highest = max(students, key=lambda x: x["total"])
    lowest = min(students, key=lambda x: x["total"])

    print("\nClass Statistics")
    print("----------------------------")
    print(f"Total Students : {total_students}")
    print(f"Class Average  : {class_average:.2f}")
    print(f"Highest Scorer : {highest['name']} ({highest['total']})")
    print(f"Lowest Scorer  : {lowest['name']} ({lowest['total']})")
    print("----------------------------\n")


# Main menu using while loop
def main():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            class_statistics()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program
main()
