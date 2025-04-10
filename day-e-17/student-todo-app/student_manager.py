from student import Student  # Assuming the Student class is in 'student.py'

class StudentManager(object):

    def __init__(self):
        self.students = []

    # Add a student
    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        return student
    
    # Get all students
    def get_all_students(self):
        return self.students

    # Search for a student by ID
    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    # Delete a student
    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True
        return False

    # Load students from a list of dictionaries
    def load_students(self, student_dicts):
        self.students = [Student.from_dict(student_data) for student_data in student_dicts]

    # List of students in dictionary format
    def to_dict_list(self):
        return [student.to_dict() for student in self.students]
