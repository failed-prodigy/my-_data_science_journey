# SQL Notes - Day 6

## Topics Covered:
- Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

## Key Concepts:
- INNER JOIN: Returns only matching rows from both tables.
- LEFT JOIN: Returns all rows from the left table and matched rows from the right.
- RIGHT JOIN: Returns all rows from the right table and matched rows from the left.
- FULL OUTER JOIN: Returns all rows when there is a match in one of the tables.

## Example Query:
```sql
SELECT customers.name, orders.amount
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
```
