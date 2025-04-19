
# SQL Journal - Day 3

## Topics Covered:
- SELECT DISTINCT
- ORDER BY
- LIMIT and OFFSET

### Sample Queries Practiced:
```sql
SELECT DISTINCT department FROM employees;

SELECT * FROM employees ORDER BY salary DESC;

SELECT * FROM students LIMIT 5 OFFSET 10;
```

### Reflection:
Using ORDER BY and LIMIT gave a better sense of data presentation and pagination. OFFSET is useful for pagination and can be powerful when combined with LIMIT.
