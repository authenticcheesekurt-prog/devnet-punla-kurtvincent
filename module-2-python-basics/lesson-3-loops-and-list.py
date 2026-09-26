"""
Module 2 — Lesson 3: Loops & Lists
Student: [Kurt Vincent Punla]
Date: [September 26, 2026]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
- A list is a container that holds multiple values in one place, in a specific order - like a numbered list on paper
- A loop repeat an action without writing it out over and over
There are 2 types of loop (for loop & while loop)
- A forloop it is commonly used when the number of repetitions is known in advance.
- A whileloop it is useful when the number of repetitions is not known beforehand.


============================================
KEY VOCABULARY
============================================
- list: an ordered collection of values stored under one variable.
- for loop: a loop that runs its code once for each item in a sequence.
- while loop: a loop that keeps running as long as a given condition.
- index: a number that marks an item's position in a list.
- iteration: one full pass through the loop's code.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# for loop over a list
scores = [88, 92, 75, 100]
for s in scores:
  print(s)

#while loop
count = 0
while count < 3:
  print("Hello")
  count = count + 1


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

- one confusing part is remembering that list indexes usually start at 0, which can easily cause off by one error when using loops

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
