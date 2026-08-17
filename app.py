student_grades = {}

# Add Student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")


# Update Student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks updated to {grade}")
    else:
        print(f"{name} not found!")


# Delete Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found!")


# Display Students
def display_all_students():
    if student_grades:
        print("\nStudent Records")
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found.")


# Main Function
def main():
    while True:
        print("\n===== Student Grades Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter new grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid Choice!")


main()