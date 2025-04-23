📘 Day 7 Recap Quiz
❓ Questions

    Python Functions & Game Logic

        How do you implement a Blackjack game using functions and loops?

        How can you ensure the Ace card value adjusts from 11 to 1 if the total goes over 21?

    SQL UNION

        What is the difference between UNION and UNION ALL?

        Write a query that combines names from two tables customers_2023 and customers_2024.

    SQL Subqueries

        What is a subquery? Where can it be used?

        Write a query using a subquery to find employees earning more than the average salary.

✅ Answers

    Python

        A Blackjack game can be made using:

            A function to deal random cards

            A function to calculate score with Ace logic

            Loops to allow repeated card draws

            Conditions to compare scores and decide the winner

        To handle Ace (11 -> 1):
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

2.SQL UNION

    UNION removes duplicates. UNION ALL keeps all values including duplicates.
SELECT name FROM customers_2023
UNION
SELECT name FROM customers_2024;

3. SQL Subqueries

    A subquery is a query inside another SQL statement. It can be used in SELECT, WHERE, or FROM.
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
