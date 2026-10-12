class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson details:")
        print("Name: ", self.name)
        print("Age: ", self.age)


class Employee(person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("\nEmployee details:")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Employee ID: ", self.emp_id)
        print("Salary: ", self.salary)


class manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        print("\nManager details:")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Employee ID: ", self.emp_id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)


p1 = None
e1 = None
m1 = None

while True:
    print("\nChoose an option : \n ")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice1 = int(input("\nEnter a choice: "))

    match choice1:
        case 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            p1 = person(name, age)
            print("Person created successfully.\n")

        case 2:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            emp_id = int(input("Enter employee ID: "))
            salary = float(input("Enter salary: "))
            e1 = Employee(name, age, emp_id, salary)
            print("Employee created successfully.\n")

        case 3:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            emp_id = int(input("Enter employee ID: "))
            salary = float(input("Enter salary: "))
            department = input("Enter department: ")
            m1 = manager(name, age, emp_id, salary, department)
            print("Manager created successfully.\n")

        case 4:
            print("\n1. Show Person Details")
            print("2. Show Employee Details")
            print("3. Show Manager Details")
            choice3 = int(input("\nEnter a choice: "))

            match choice3:
                case 1:
                    if p1:
                        p1.display()
                    else:
                        print("No person created.")
                case 2:
                    if e1:
                        e1.display()
                    else:
                        print("No employee created.")
                case 3:
                    if m1:
                        m1.display()
                    else:
                        print("No manager created.")

        case 5:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
