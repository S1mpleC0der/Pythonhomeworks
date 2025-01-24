import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    @staticmethod
    def view_all_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        if records:
            print("Employee Records:")
            for record in records:
                print(record.strip())
        else:
            print("No employee records found.")

    @staticmethod
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(employee_id):
                    print("Employee Found:")
                    print(record.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        updated = False
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for record in records:
                if record.startswith(employee_id):
                    parts = record.strip().split(", ")
                    if name:
                        parts[1] = name
                    if position:
                        parts[2] = position
                    if salary:
                        parts[3] = salary
                    file.write(", ".join(parts) + "\n")
                    updated = True
                else:
                    file.write(record)
        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        deleted = False
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
        with open(EmployeeManager.FILE_NAME, "w") as file:
            for record in records:
                if record.startswith(employee_id):
                    deleted = True
                else:
                    file.write(record)
        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    @staticmethod
    def menu():
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(employee_id, name, position, salary)
                EmployeeManager.add_employee(employee)
            elif choice == "2":
                EmployeeManager.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                EmployeeManager.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to skip): ") or None
                position = input("Enter new Position (leave blank to skip): ") or None
                salary = input("Enter new Salary (leave blank to skip): ") or None
                EmployeeManager.update_employee(employee_id, name, position, salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                EmployeeManager.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
