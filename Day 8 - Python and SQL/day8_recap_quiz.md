# Day 8 Recap Quiz

## Questions & Answers

**1. What are global and local variables in Python? Give an example.**  
→ Local variables exist within functions, global ones outside. Local overrides global if same name used.

**2. Write a Python program that uses a global counter incremented inside a function.**
```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

**3. What’s the output of a guessing game using random number generation and loops?**  
→ The game gives "Too High", "Too Low", or "Correct" based on user guesses.

**4. In SQL, how do you list all distinct replacement costs from a film table?**  
→ `SELECT DISTINCT replacement_cost FROM film;`

**5. How do you use CASE in SQL to categorize values?**  
→ `CASE WHEN replacement_cost < 20 THEN 'low' ... END`

**6. How can you find the city with most sales from customers in SQL?**  
→ Use JOIN on payment, customer, and address tables + GROUP BY + SUM(amount)

**7. What is the toughest subquery challenge you did and what was the answer?**  
→ Bonus Q14: Top-performing film in animation: DOGMA FAMILY with 178.70
