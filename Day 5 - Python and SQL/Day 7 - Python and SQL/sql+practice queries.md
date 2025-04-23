-- Using UNION
SELECT name FROM students_2023
UNION
SELECT name FROM students_2024;

-- Subquery in WHERE
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in FROM
SELECT avg_salary
FROM (SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department) AS dept_avg;

-- Subquery in SELECT
SELECT name, (SELECT MAX(salary) FROM employees) AS max_salary
FROM employees;
