# ISBN Checker (10 & 13)

A simple ISBN validator I wrote for my Maths & CS class assignment. 

```
student-id: sct-254-167/2023
name: Boby Barack
```

Right now it has the core calculation logic for both ISBN-10 and ISBN-13 — no API or visualizations yet, just the functions that do the actual maths. The plan is to eventually wrap it in an API, but for now I wanted to express the logic I understand first.

## How ISBN-10 validation actually works

An ISBN-10 is 10 digits long. To check if its valid you take each digit and multiply it by its position (1st digit × 1, 2nd digit × 2, ... 10th digit × 10), then add all those up. If the total is divisible by 11, the ISBN is valid.

So for example `0618260307`:

```
0×1 + 6×2 + 1×3 + 8×4 + 2×5 + 6×6 + 0×7 + 3×8 + 0×9 + 7×10
= 0 + 12 + 3 + 32 + 10 + 36 + 0 + 24 + 0 + 70
= 187
```

187 ÷ 11 = 17 with no remainder, so its valid.

A special case I've come across is that the last digit can be `X` which just means 10. So if you see something like `020161622X` you treat that X as the 10th value and multiply it by position 10 giving you 100.

## How ISBN-13 validation actually works

ISBN-13 is the newer standard used for barcodes on almost all books now. It's 13 digits long and uses a different check (Mod 10 instead of Mod 11).

Instead of multiplying by the position, you use **alternating weights** of 1 and 3:
- Multiply the 1st, 3rd, 5th... digits by **1**
- Multiply the 2nd, 4th, 6th... digits by **3**

Then you sum them all up. If the final total is divisible by 10, the ISBN is valid!

Example `9780618260300`:
```
9×1 + 7×3 + 8×1 + 0×3 + 6×1 + 1×3 + 8×1 + 2×3 + 6×1 + 0×3 + 3×1 + 0×3 + 0×1
= 9 + 21 + 8 + 0 + 6 + 3 + 8 + 6 + 6 + 0 + 3 + 0 + 0
= 70
```
70 ÷ 10 = 7 with no remainder, so its valid!

## What the code does

- `check_digit(isbn)` — give it the first 9 digits of an ISBN-10 and it calculates what that 10th digit should be.
- `validate_isbn10(isbn)` — give it all 10 digits and it tells you if its valid or not.
- `convert_to_isbn13(isbn)` — converts an ISBN-10 to ISBN-13. It sticks `978` (the GS1 bookland prefix) in front and recalculates the new Mod 10 check digit.
- `validate_isbn13(isbn)` — same idea but for 13-digit ISBNs using the alternating weight logic.

## How to run

```bash
python isbn_checker.py
```

It will execute the test ISBNs from the assignment and print the results to the console.

## Credits
Thanks to Mr. Nyaga for helping me understand the meaning of linear engineering by thinking about the actual mathematical logic first before attempting to validate the input used for testing or running the program(if input functions are added) and eventually expose it to the internet through the API.

## What I yet to do

- Add input cleaning (handle dashes and spaces).
- Add input validation (check length of input and reject bad characters).
- Wrap in a Flask API (Internet exposure) with proper endpoints.
