class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, condition, value):
        if condition == '>':
            result = [emp for emp in self.employees if emp.salary > value]
        elif condition == '<':
            result = [emp for emp in self.employees if emp.salary < value]
        elif condition == '>=':
            result = [emp for emp in self.employees if emp.salary >= value]
        elif condition == '<=':
            result = [emp for emp in self.employees if emp.salary <= value]
        else:
            result = []
        return result

def main():
    database = EmployeeDatabase()

    # Adding employees to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        result = database.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = database.search_by_name(name)
    elif choice == 3:
        condition = input("Enter condition (> < >= <=): ")
        value = float(input("Enter salary value: "))
        result = database.search_by_salary(condition, value)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No results found.")
    else:
        print("Search Results:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
