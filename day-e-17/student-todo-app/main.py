from student_manager import StudentManager  # Import the StudentManager class
from storage import Storage  # Import the Storage class

def display_students(students: list) -> None:
    """Display the list of students."""
    if not students:
        print("No students to display")
    else:
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

def main():
    # Initialize StudentManager and Storage
    manager = StudentManager()
    store = Storage()

    # Load saved students from storage (students.json)
    saved_students = store.load()
    manager.load_students(saved_students)

    while True:
        # Menu for Student Management Application
        print("\nStudent Management Application: ")
        print("\n1. Add Student\n2. View Students\n3. Search Student by ID\n4. Delete Student\n5. Exit\n")
        choice = input("Choice -> ")

        if choice == '1':
            # Add a new student
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            
            # Validate input
            if name.strip() and grade.strip():
                # Validate age as a positive integer
                if age.strip().isdigit() and int(age) > 0:
                    student = manager.add_student(name.strip(), int(age), grade.strip())
                    store.save(manager.get_all_students())  # Pass the list of Student objects, not the dict
                    print(f"Student added with ID: {student.id}")
                else:
                    print("Invalid age. Please enter a positive integer.")
            else:
                print("Invalid input. Please make sure all fields are filled correctly.")

        elif choice == '2':
            # View all students
            display_students(manager.get_all_students())

        elif choice == '3':
            # Search for a student by ID
            student_id = input("Enter the student ID to search: ")
            student = manager.search_student_by_id(student_id)
            if student:
                print(f"Student found: {student.id} - {student.name}, Age: {student.age}, Grade: {student.grade}")
            else:
                print("Student ID not found")

        elif choice == '4':
            # Delete a student by ID
            student_id = input("Enter the student ID to delete: ")
            if manager.delete_student(student_id):
                store.save(manager.get_all_students())  # Save after deleting a student
                print("Student deleted")
            else:
                print("Student ID not found")

        elif choice == '5':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
