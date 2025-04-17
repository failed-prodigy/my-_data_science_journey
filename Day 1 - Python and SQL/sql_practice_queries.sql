-- sql_practice_queries.sql

-- 1. Select all from a table
SELECT * FROM students;

-- 2. Filter based on one condition
SELECT * FROM employees WHERE salary > 50000;

-- 3. Filter using AND
SELECT * FROM customers WHERE bill > 100 AND age > 30;

-- 4. Filter using OR
SELECT * FROM customers WHERE bill > 100 OR age > 30;

-- 5. Specific query
SELECT name FROM students WHERE age > 18 AND grade = 'A';

