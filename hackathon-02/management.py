import json  # For saving/loading data in JSON format

# -----------------------
# Person Class
# -----------------------
class Person:
    def __init__(self, name, age, gender):
        # Initialize basic person attributes
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        # Return string with basic person details
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# -----------------------
# Employee Class (inherits from Person)
# -----------------------
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        # Initialize attributes from Person class
        super().__init__(name, age, gender)
        # Additional attributes for Employee
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def get_details(self):
        # Override get_details to include employee-specific data
        return (f"{super().get_details()}, Emp ID: {self.emp_id}, "
                f"Department: {self.department}, Salary: ₹{self.salary:.2f}")

    def is_eligible_for_bonus(self):
        # Return True if employee's salary is below ₹50,000
        return self.salary < 50000

    # Class method to create an Employee object from a comma-separated string
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, department, float(salary))
    from_string = classmethod(from_string)

    # Static method to print the bonus policy
    def bonus_policy():
        print("💰 Bonus Policy: Employees earning less than ₹50,000 are eligible for bonuses.")
    bonus_policy = staticmethod(bonus_policy)


# -----------------------
# Department Class
# -----------------------
class Department:
    def __init__(self, name):
        # Initialize department name and empty list of employees
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        # Add an employee to the department if they belong to it
        if isinstance(employee, Employee) and employee.department == self.name:
            self.employees.append(employee)

    def get_average_salary(self):
        # Return average salary of employees in this department
        if not self.employees:
            return 0.0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        # Return a list of employee detail strings
        return [emp.get_details() for emp in self.employees]


# -----------------------
# Persistence Functions
# -----------------------

def save_to_json(employees, filename="employees.json"):
    """
    Save a list of Employee objects to a JSON file.
    Converts each Employee to a dictionary using vars().
    """
    data = [vars(emp) for emp in employees]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_from_json(filename="employees.json"):
    """
    Load employee data from a JSON file and return a list of Employee objects.
    """
    employees = []
    with open(filename, "r") as f:
        data = json.load(f)
        for item in data:
            emp = Employee(
                item['name'], item['age'], item['gender'],
                item['emp_id'], item['department'], item['salary']
            )
            employees.append(emp)
    return employees
