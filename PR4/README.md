# 📊 Data Analyzer and Transformer Program

A beginner-friendly Python project that analyzes and transforms a dataset using a menu-driven program. This project demonstrates Python functions, lambda functions, recursion, lists, sorting, and dictionary operations.

## 👨‍💻 Author

**Amit Baldaniya**

B.Sc. IT Student

## 📌 Project Description

The Data Analyzer and Transformer Program is a console-based Python application designed to perform different operations on a dataset.

The program provides a main menu where users can select options to display data summaries, calculate factorials, filter values, sort data, and display dataset statistics.

## 🚀 Features

1. **Input Data** – Display and store dataset values.
2. **Display Data Summary** – Show total elements, minimum, maximum, sum, and average.
3. **Calculate Factorial** – Calculate factorial using a recursive function.
4. **Filter Data by Threshold** – Filter values greater than or equal to a selected threshold.
5. **Sort Data** – Sort data in ascending or descending order.
6. **Display Dataset Statistics** – Display minimum, maximum, sum, and average in dictionary format.
7. **Exit Program** – Exit the application.

## 🛠️ Technologies Used

* Python 3
* Lists
* Functions
* Lambda Functions
* Recursion
* Dictionary
* `match-case`
* `sorted()`
* Built-in Functions

## 📂 Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── PR-4.py
└── README.md
```

## ▶️ How to Run

### Step 1: Install Python

Download and install Python 3 from the official website:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone https://github.com/yourusername/Data-Analyzer-and-Transformer.git
```

### Step 3: Open the Project Folder

```bash
cd Data-Analyzer-and-Transformer
```

### Step 4: Run the Python Program

```bash
python PR-4.py
```

## 📋 Sample Dataset

```python
array = [34, 12, 56, 78, 43, 21, 90]
```

## 🖥️ Sample Output

```text
Welcome To Data Analyzer and Transformer Program

---------------------------------------------------------

Main Menu:

1.Input data
2.Display Data Summary
3.Calculate Factorial
4.Filter Data by Threshold
5.Sort Data
6.Display Dataset Statistics
7.Exit Program

Please Enter Your Choice: 2
```

### Data Summary

```text
Data Summary

Total elements: 7
Minimum value: 12
Maximum value: 90
Sum of all value: 334
Average value: 47.714285714285715
```

### Dataset Statistics

```text
Dataset Statistics:

minimum Value : 12
maximum Value : 90
Sum of all values : 334
Avrage Value : 47.714285714285715
```

## 📚 Python Concepts Used

### 1. Lambda Function

Used to filter data based on a threshold value.

```python
filter = lambda num, arr: [
    element for element in arr if element >= num
]
```

### 2. Recursive Function

Used to calculate the factorial of a number.

```python
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
```

### 3. Sorting

```python
sorted(array)
```

Ascending order.

```python
sorted(array, reverse=True)
```

Descending order.

### 4. Dictionary

Used to store and display dataset statistics.

```python
{
    "minimum Value": min(array),
    "maximum Value": max(array),
    "Sum of all values": sum(array),
    "Avrage Value": sum(array) / len(array)
}
```

## 🎯 Learning Objectives

* Understand Python functions and their uses.
* Learn how to use lambda functions.
* Understand recursion in Python.
* Perform mathematical operations on lists.
* Learn ascending and descending sorting.
* Use dictionaries to store data.
* Develop a menu-driven Python application.
* Improve problem-solving and programming skills.

## 🔮 Future Improvements

* Add user input to enter a custom dataset.
* Add data validation for invalid inputs.
* Add data visualization using Matplotlib.
* Add CSV file import and export.
* Add more data analysis operations.
* Improve the user interface.
* Add error handling using `try-except`.

## 📄 License

This project is created for educational and learning purposes.

---

⭐ If you find this project useful, feel free to star the repository.

**Thank you for visiting my project!**
