def add_employee(file_name):
    with open(file_name, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully.")

def view_employees(file_name):
    try:
        with open(file_name, 'r') as file:
            print("\nEmployee Records:")
            print(file.read())
    except FileNotFoundError:
        print("No employee records found.")

def search_employee(file_name):
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:", line.strip())
                    return
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")

def update_employee(file_name):
    emp_id = input("Enter Employee ID to update: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        updated = False
        with open(file_name, 'w') as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("Current Record:", line.strip())
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    file.write(line)
        if updated:
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee records found.")

def delete_employee(file_name):
    emp_id = input("Enter Employee ID to delete: ")
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        with open(file_name, 'w') as file:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    file.write(line)
        print("Employee record deleted successfully.")
    except FileNotFoundError:
        print("No employee records found.")

def main():
    file_name = "employees.txt"
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(file_name)
        elif choice == "2":
            view_employees(file_name)
        elif choice == "3":
            search_employee(file_name)
        elif choice == "4":
            update_employee(file_name)
        elif choice == "5":
            delete_employee(file_name)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
