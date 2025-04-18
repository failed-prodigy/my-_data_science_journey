-- Count number of orders per customer
SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id;

-- Average salary per department
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- Departments with average salary above 50000
SELECT department, AVG(salary) as avg_sal FROM employees GROUP BY department HAVING avg_sal > 50000;
