students = {}  # Dictionary to store student data

while True:
    print("\nStudent Management System")
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Print Student Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grades = input("Enter student grades (comma-separated): ")
        students[name] = grades.split(',')  # Store grades as a list of strings
        print(f"Student {name} added!")

    elif choice == '2':
        name = input("Enter student name to remove: ")
        if name in students:
            del students[name]
            print(f"Student {name} removed!")
        else:
            print("Student not found!")

    elif choice == '3':
        name = input("Enter student name: ")
        if name in students:
            print(f"{name}'s Grades: {', '.join(students[name])}")
        else:
            print("Student not found!")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
