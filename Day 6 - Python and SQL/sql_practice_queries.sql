-- SQL JOIN Practice Queries

-- INNER JOIN
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- LEFT JOIN
SELECT c.name, o.order_date
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;

-- RIGHT JOIN
SELECT o.order_date, c.name
FROM customers c
RIGHT JOIN orders o ON c.id = o.customer_id;

-- FULL OUTER JOIN
SELECT a.name, b.salary
FROM employees a
FULL OUTER JOIN payroll b ON a.id = b.emp_id;
