## Day 5 - SQL Notes

**Topics Covered:**
- COALESCE: Replaces NULLs with a default value.
- CAST: Converts data types (e.g., string to integer).
- REPLACE: Substitutes parts of strings.
- CASE: Implements conditional logic in queries.

**Examples:**
```sql
SELECT name, COALESCE(phone, 'N/A') FROM customers;

SELECT name, CAST(price AS INTEGER) FROM products;

SELECT REPLACE(city, 'New', 'Old') FROM locations;

SELECT name,
       CASE 
           WHEN score >= 90 THEN 'A'
           WHEN score >= 75 THEN 'B'
           ELSE 'C'
       END AS grade
FROM students;
