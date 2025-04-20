# Day 4 – SQL Notes 🧠

## Topics Covered:
- LIKE Operator
- Wildcards: `%` and `_`
- Complex WHERE Clauses
- Combining AND with LIKE

## Syntax:
```sql
-- Single character wildcard
SELECT * FROM customers WHERE name LIKE '_an%';

-- Sequence wildcard
SELECT * FROM products WHERE product_name LIKE 'A%';

-- Combined conditions
SELECT * FROM customers WHERE country = 'USA' AND age > 25;

Key Points:

    % matches zero or more characters.

    _ matches exactly one character.

    LIKE is case-insensitive in some databases (e.g., MySQL).

    Useful for fuzzy filtering like searching for names, product IDs, etc.