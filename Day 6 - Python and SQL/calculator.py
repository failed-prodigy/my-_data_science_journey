# Simple Calculator using Functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

operation = input("Choose operation (+, -, *, /): ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if operation == "+":
    print("Result:", add(n1, n2))
elif operation == "-":
    print("Result:", subtract(n1, n2))
elif operation == "*":
    print("Result:", multiply(n1, n2))
elif operation == "/":
    print("Result:", divide(n1, n2))
else:
    print("Invalid operation")
