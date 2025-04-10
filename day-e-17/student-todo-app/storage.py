import json
import os
from student import Student  # Ensure that the Student class is imported

class Storage(object):

    def __init__(self, filepath='students.json'):
        self.filepath = filepath

    def save(self, student_list):
        """Save a list of students to a file."""
        # Convert the list of student objects to dictionaries
        student_dicts = [student.to_dict() for student in student_list]
        with open(self.filepath, 'w') as f:
            json.dump(student_dicts, f, indent=4)

    def load(self):
        """Load the list of students from a file."""
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath) as f:
            student_dicts = json.load(f)
            return [Student.from_dict(student_data) for student_data in student_dicts]