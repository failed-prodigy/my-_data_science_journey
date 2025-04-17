# Day 1 – Python Notes 🐍

## Topics Covered:
- Print and Input functions
- Variables and Data Types
- Conditional Statements (if/else)
- Functions

---

## Print and Input
```python
print("Hello, world!")
name = input("Enter your name: ")
print(f"Welcome, {name}")


Variables and Data Types

name = "George"  # String
age = 25         # Integer
height = 5.9     # Float
is_student = True # Boolean

Conditional Statements

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


Functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Lakshman"))
