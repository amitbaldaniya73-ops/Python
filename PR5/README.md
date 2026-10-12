# 👨‍💼 Employee Management System

A menu-driven **Employee Management System** developed using Python and Object-Oriented Programming (OOP). This project allows users to create and display Person, Employee, and Manager details using inheritance, constructors, method overriding, and polymorphism.

## 📌 Project Overview

The Employee Management System is a beginner-friendly Python project designed to demonstrate the practical implementation of OOP concepts.

Users can create different types of objects, enter their details, and display the stored information through a simple menu-driven interface.

## ✨ Features

- Create Person details
- Create Employee details
- Create Manager details
- Display Person, Employee, and Manager information
- Use inheritance to reuse code
- Implement method overriding
- Demonstrate polymorphism
- Use constructors to initialize object data
- Simple and interactive menu-driven interface

## 🛠️ Technologies Used

- **Language:** Python
- **Concepts:** Object-Oriented Programming (OOP)
- **Input/Output:** Console-based interface
- **Control Statements:** `while`, `match-case`, and `if-else`

## 📚 OOP Concepts Used

### 1. Class and Object
Classes define the structure of Person, Employee, and Manager objects.

### 2. Inheritance
The Employee class inherits from Person, and the Manager class inherits from Employee.

```python
class Employee(person):
    pass

class manager(Employee):
    pass
```

This demonstrates **multilevel inheritance**.

### 3. Constructor
The `__init__()` method initializes object attributes such as name, age, employee ID, salary, and department.

### 4. Method Overriding
Each class defines its own `display()` method to show the details relevant to that class.

### 5. Polymorphism
The same method name, `display()`, produces different outputs depending on the object calling it.

### 6. `super()` Function
The `super()` function calls the parent class constructor, helping reuse existing initialization code.

## 📋 Menu Options

| Option | Description |
|---|---|
| 1 | Create Person |
| 2 | Create Employee |
| 3 | Create Manager |
| 4 | Show Details |
| 5 | Exit the Program |

## ▶️ How to Run

**Step 1:** Install Python 3.10 or newer.

**Step 2:** Clone the repository.

```bash
git clone https://github.com/amitbaldaniya73-ops/Python.git
```

**Step 3:** Open the project folder and save your program as `employee_management.py`.

**Step 4:** Run the program.

```bash
python employee_management.py
```

## 💻 Sample Output

```text
Choose an option:

1. Create Person
2. Create Employee
3. Create Manager
4. Show Details
5. Exit

Enter a choice: 3
Enter name: Rahul
Enter age: 25
Enter employee ID: 101
Enter salary: 30000
Enter department: IT

Manager created successfully.
```

## 🎯 Learning Objectives

- Understand the fundamentals of Python OOP.
- Learn how inheritance improves code reusability.
- Understand constructors and the `super()` function.
- Practice method overriding and polymorphism.
- Build a menu-driven console application.

## 🔮 Future Improvements

- Add update and delete functionality.
- Store multiple employees in a list.
- Add input validation and error handling.
- Save employee records to a file or database.
- Add a graphical user interface (GUI).

## 👨‍💻 Author

**Amit Baldaniya**

B.Sc. IT Student | Python Programming | Object-Oriented Programming

- GitHub: [amitbaldaniya73-ops](https://github.com/amitbaldaniya73-ops)

## 📄 License

This project is created for educational and learning purposes. You are welcome to study and modify the code for your own practice.