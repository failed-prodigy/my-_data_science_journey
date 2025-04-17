
---

### 📄 `sql_notes.md`

```markdown
# Day 1 – SQL Notes 🗃️

## Topics Covered:
- SELECT statements
- WHERE clause
- AND / OR logic

---

## SELECT
```sql
SELECT * FROM customers;
SELECT name, age FROM students;


WHERE Clause

SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM students WHERE grade = 'A';


AND / OR Conditions

-- AND: Both conditions must be true
SELECT * FROM customers WHERE bill > 100 AND age > 30;

-- OR: At least one condition must be true
SELECT * FROM customers WHERE bill > 100 OR age > 30;


Sample Query

SELECT name FROM students WHERE age > 18 AND grade = 'A';
