-- Using COALESCE to replace nulls
SELECT name, COALESCE(phone, 'Not Available') FROM contacts;

-- Using CAST to convert string prices to integers
SELECT product_name, CAST(price AS INTEGER) FROM products;

-- Using REPLACE to rename cities
SELECT REPLACE(city, 'Old', 'New') FROM customers;

-- Using CASE for grading
SELECT student_name,
       CASE 
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 70 THEN 'B'
           ELSE 'C'
       END AS grade
FROM marksheet;
