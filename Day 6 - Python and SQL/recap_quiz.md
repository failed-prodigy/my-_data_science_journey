# Day 6 Recap Quiz

## Questions

1. What is the difference between parameters and arguments in Python functions?
2. How would you write a simple calculator using functions?
3. What does an INNER JOIN do in SQL?
4. How does a LEFT JOIN differ from a RIGHT JOIN?
5. Write a SQL query using FULL OUTER JOIN.

## Answers

1. **Parameters** are variables listed in a function definition. **Arguments** are the actual values passed to the function when it is called.

2. Example:
```python
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(add(num1, num2))
```

3. INNER JOIN returns records that have matching values in both tables.

4. LEFT JOIN returns all records from the left table and the matched records from the right table. RIGHT JOIN does the opposite.

5.
```sql
SELECT a.name, b.salary
FROM employees a
FULL OUTER JOIN payroll b ON a.id = b.emp_id;
```
