import uuid  # Ref: https://docs.python.org/3/library/uuid.html

class Student:

    def __init__(self, name: str, age: int, grade: str, student_id=None):
        self.id = student_id if student_id else str(uuid.uuid4())  # Unique ID for each student
        self.name = name
        self.age = age
        self.grade = grade

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            student_id=data["id"]
        )