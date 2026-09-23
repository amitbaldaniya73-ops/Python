print("---Python oop project: Employee Management system----")

while True:

    print("\n choose an operation : \n ")
    print("1. Create a person")
    print("2. Create a employee")
    print("3. Create a manager")
    print("4. Show Details ")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:

            class person:
                name = None
                age = None

            p1 = person()
            p1.name = input("Enter name: ")
            p1.age = int(input("Enter age: "))

            print("\nPerson created with name:", p1.name, "and age :", p1.age, ".")

        case 2:

            class employee:
                name = None
                age = None
                Emp_id = None
                salary = None

            e1 = employee()
            e1.name = input("Enter Name: ")
            e1.age = int(input("Enter Age:"))
            e1.Emp_id = int(input("Enter Employee ID:"))
            e1.salary = int(input("Enter Salary:"))
            print(
                "Employee Create with name:",
                e1.name,
                "age:",
                e1.age,
                "Emp_id:",
                e1.Emp_id,
                "salary:",
                e1.salary,
                ".",
            )

        case 3:

            class manager:
                name = None
                age = None
                Emp_id = None
                salary = None
                department = None

            m1 = manager()
            m1.name = input("Enter Name: ")
            m1.age = int(input("Enter Age: "))
            m1.Emp_id = int(input("Enter Employee ID: "))
            m1.salary = int(input("Enter Salary: "))
            m1.department = input("Enter Department: ")
            print(
                "Manager created with name:",
                m1.name,
                "age:",
                m1.age,
                "Emp_id:",
                m1.Emp_id,
                "salary:",
                m1.salary,
                "department:",
                m1.department,
                ".",
            )

        case 4:
            print("Choose details to show : \n ")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            choice2 = int(input("Enter a choice: "))

            match choice2:
                case 1:
                    print("Person created with name:", p1.name, "and age :", p1.age, ".")
                case 2:
                    print("Employee Create with name:",e1.name,"age:",e1.age,"Emp_id:",e1.Emp_id,"salary:",e1.salary,".")

                case 3:
                    print(
                        "Manager created with name:",
                        m1.name,
                        "age:",
                        m1.age,
                        "Emp_id:",
                        m1.Emp_id,
                        "salary:",
                        m1.salary,
                        "department:",
                        m1.department,
                        "."
                    )
                case _:
                    print("Invalid choice.")

        case 5:
            print("Exiting the system. All resources have been freed   .")
            break

        case _:
            print("Invalid choice. Please try again.")

print("Goodbye!")