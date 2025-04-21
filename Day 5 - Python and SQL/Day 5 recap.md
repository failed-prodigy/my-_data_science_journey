🧠 Day 5 Recap Quiz

1. What Python data structure allows you to store key-value pairs, such as names and bids?
✅ Answer: Dictionary.
Example: bids = {"Lakshman": 500, "Raj": 700}

2. Write a function that finds the highest bidder from a dictionary of names and bids.
✅ Answer:

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")

3. What is the purpose of COALESCE in SQL? Provide an example.
✅ Answer: It replaces NULL values with a default value.
Example:

SELECT name, COALESCE(phone, 'N/A') FROM users;

4. What does CAST do in SQL?
✅ Answer: It converts one data type into another.
Example:

SELECT CAST(price AS INTEGER) FROM products;

5. How is the CASE statement in SQL similar to Python’s if/elif/else? Provide a query example.
✅ Answer: CASE lets you write conditional logic in SQL.
Example:

SELECT name,
       CASE 
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 75 THEN 'B'
           ELSE 'C'
       END AS grade
FROM students;

Let me know if you'd like the PDF version or GitHub folder structure for today as well!
