---

## 📘 Day 4 – Recap Quiz (Python + SQL)

---

### 🐍 Python – Functions, Loops, and Projects

**1. What is the purpose of using functions in Python?**  
Give an example of a function that returns a value.

**2. What’s the difference between an argument and a parameter?**  
Give an example showing both in use.

**3. How would you implement a Caesar cipher function that can both encode and decode text?**

**4. Describe how a `while` loop was used in your Hangman project. What does it check for?**

---

### 🛢 SQL – LIKE and Complex Conditions

**5. What does the `LIKE` operator do in SQL?**  
Give an example using `%` and `_`.

**6. Write a query to get all products starting with "A".**

**7. Combine `LIKE` with `AND` to find all customers from 'India' whose names start with 'S'.**

---

## ✅ Solutions

**1.**  
Functions help modularize and reuse code.  
Example:
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

**2.**  
- **Parameter**: The variable inside the function definition.  
- **Argument**: The value passed to the function when calling it.

```python
def greet(name):  # 'name' is the parameter
    print(f"Hello, {name}!")

greet("Lakshman")  # "Lakshman" is the argument
```

**3.**  
```python
def caesar_cipher(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - base + shift) % 26 if direction == 'encode' else (ord(char) - base - shift) % 26
            result += chr(base + offset)
        else:
            result += char
    return result
```

**4.**  
In Hangman, the while loop was used like this:
```python
while "_" in display and lives > 0:
```
It runs until either the word is guessed (no `_` left) or the player loses all lives.

**5.**  
`LIKE` is used to search for a pattern in a column.  
- `%` – wildcard for multiple characters  
- `_` – wildcard for a single character  
Example:
```sql
SELECT * FROM sales WHERE product_name LIKE '_an%';
```

**6.**
```sql
SELECT * FROM products WHERE product_name LIKE 'A%';
```

**7.**
```sql
SELECT * FROM customers WHERE country = 'India' AND name LIKE 'S%';
```

—