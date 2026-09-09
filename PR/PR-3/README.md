# 🧑‍💻 Interactive Personal Data Collector

A simple Python program that collects personal information from the user and displays the collected data along with its **data type** and **memory address**.

This project is created for learning basic Python concepts such as variables, data types, user input, type conversion, and the `id()` function.

## 🚀 Features

The program collects:

* 👤 Name
* 🎂 Age
* 📏 Height in meters
* 🔢 Favourite number

After collecting the information, the program displays:

* Entered value
* Data type of each value
* Memory address using Python's `id()` function
* Approximate birth year based on the entered age

## 🛠️ Concepts Used

* `input()`
* `int()`
* `float()`
* `print()`
* Variables
* Python Data Types
* `type()`
* `id()`
* Basic arithmetic operations
* String formatting and output

## 📋 Example

```text
---------------------------------------------------------------------
Welcome To The Interactive Personal Data Collector !

please enter your name: Amit
please enter your age: 18
please enter your height in meters: 1.70
please enter your favourite number: 7

Thank You! Here Is The Information We Collected:

Name: Amit
age: 18
height: 1.7
favourite_number: 7

Your birth year is approximately: 2008

Thank You For Using The Personal Data Collector. GoodBye!
---------------------------------------------------------------------
```

> **Note:** The memory address shown by `id()` can be different every time the program runs.

## 📂 Project Structure

```text
Personal-Data-Collector/
│
├── pr2.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Run the program

Open the terminal in the project folder and run:

```bash
python pr2.py
```

## 🎯 Learning Objectives

This project helps beginners understand:

1. How to take input from users
2. How to store data in variables
3. Difference between `str`, `int`, and `float`
4. Type conversion in Python
5. How `type()` works
6. How `id()` works
7. Basic mathematical calculations

## 👨‍💻 Author

**Amit Baldaniya**

B.Sc. IT Student

## ⭐ Future Improvements

Some possible improvements:

* Add email and phone number fields
* Add input validation
* Calculate exact birth year using date of birth
* Store collected information in a file
* Create a menu-driven version
* Add a graphical user interface (GUI)

---

⭐ **If you like this beginner Python project, feel free to star the repository!**
