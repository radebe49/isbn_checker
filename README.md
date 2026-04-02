# ISBN-10 Checker

A simple ISBN-10 validator I wrote for my Maths & CS class assignment.

Right now it only has the core calculation logic — no API or valiidations just the functions that do the actual maths. The plan is to eventually wrap it in an API but for now I wanted to get the logic right first.

## How ISBN-10 validation actually works

An ISBN-10 is 10 digits long. To check if its valid you take each digit and multiply it by its position (1st digit × 1, 2nd digit × 2, ... 10th digit × 10), then add all those up. If the total is divisible by 11, the ISBN is valid.

So for example `0618260307`:

```
0×1 + 6×2 + 1×3 + 8×4 + 2×5 + 6×6 + 0×7 + 3×8 + 0×9 + 7×10
= 0 + 12 + 3 + 32 + 10 + 36 + 0 + 24 + 0 + 70
= 187
```

187 ÷ 11 = 17 with no remainder, so its valid.

One edge case is that the last digit can be `X` which just means 10. So if you see something like `020161622X` you treat that X as the value 10 and multiply it by position 10 giving you 100.

## What the code does

- `check_digit(isbn)` — give it 9 digits and it calculates what the 10th digit should be
- `validate_isbn10(isbn)` — give it all 10 digits and it tells you if its valid or not
- `convert_to_isbn13(isbn)` — converts an ISBN-10 to ISBN-13 (sticks 978 in front and recalculates the check digit)
- `validate_isbn13(isbn)` — same idea but for 13-digit ISBNs (uses alternating weights of 1 and 3 instead of positions)

## How to run

```bash
python isbn_checker.py
```

It will validate the test ISBNs from the assignment and print the results.

## Credits
Thanks to Mr.Nyaga for helping e understand the meaning of linear engineering in that i think about the actual mathematical logic first before attempting to validate the issue and eventually expose it to the internet

## What I yet to do

- add input cleaning (handle dashes and spaces)
- add input validation (check length, reject bad characters)
- wrap in Flask API with proper endpoints
