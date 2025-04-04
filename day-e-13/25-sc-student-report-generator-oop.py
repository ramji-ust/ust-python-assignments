import json
from students import Student
from operator import methodcaller

# Read data from JSON file
with open("students.json", "r") as json_file:
    student_data = json.load(json_file)

# Create a list of Student objects
students = []
for data in student_data:
    temp = Student(data['name'], data['regid'], data['age'])
    temp.set_marks(phy=data['phy'], chem=data['chem'], bio=data['bio'], math=data['math'])
    students.append(temp)

# Calculate average and assign ranks
avgs = list(map(methodcaller('calculate_average'), students))
avgs = sorted(set(avgs), reverse=True)
ranks = [student.set_rank(avgs.index(student.average) + 1) for student in students]

# Write data to a report JSON file
report_data = []
for student in students:
    student_dict = {
        "name": student.name,
        "age": student.age,
        "regid": student.regid,
        "phy": student.marks.get('phy', 0),
        "chem": student.marks.get('chem', 0),
        "math": student.marks.get('math', 0),
        "bio": student.marks.get('bio', 0),
        "avg": student.average,
        "rank": student.rank
    }
    report_data.append(student_dict)

# Sort report data by rank
report_data_sorted = sorted(report_data, key=lambda x: x['rank'])

with open("studentreport-oop.json", "w") as json_out:
    json.dump(report_data_sorted, json_out, indent=2)

print("Report written to studentreport-oop.json")

