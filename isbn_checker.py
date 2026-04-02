#

def check_digit(isbn):
    # isbn is the first 9 digits as a string(using for loop to repeat the multiplication of each digit by its position)
    # we need d10 such that: d1*1 + d2*2 + ... + d9*9 + d10*10 ≡ 0 (mod 11)
    # rearranging: d10 ≡ (-total) * 10^(-1) (mod 11)
    # since 10 * 10 = 100 = 99 + 1 ≡ 1 (mod 11), the inverse of 10 is 10
    # so: d10 = (-total * 10) % 11

    total = 0
    for i in range(9):
        total = total + int(isbn[i]) * (i + 1)

    # checking the actual digit(end digit)
    check = (-total * 10) % 11
    # actually checking if the check digit is 10
    if check == 10:
        return "X"
    return str(check)


def validate_isbn10(isbn):
    # multiplying each digit by its position (1 to 10), sum, check mod 11
    total = 0
    for i in range(10):
        #checking if the digit is X, if so we add the total as is(adding by 10+10 since if X appears the math is value(10) +position(10)) else we just proceed with total=total+int(isbn[i]) * (i + 1)
        if isbn[i] == "X":
            total = total + 10 * 10
        else:
            total = total + int(isbn[i]) * (i + 1)

    # now we actually check if the total is divisible by 11
    if total % 11 == 0:
        return "Valid"
    else:
        return "Invalid"


def convert_to_isbn13(isbn):
    # prefix 978 + first 9 digits, then compute isbn13 check digit. we are using 978 to convert from normal isbn10 to global standard isbn13(the standard used in barcodes)
    body = "978" + isbn[:9]
    
    total = 0
    for i in range(12):
        #if its even the weight is 1 so we leave as it is but if its odd the weight is 3, hence we multiply by three...im using the total=total+int(isbn[i]) * 3
        if i % 2 == 0:
            total = total + int(body[i])
        else:
            total = total + int(body[i]) * 3

    #now we actually convert to get the isbn13 string. 10- is finding distance to the next multiple of 10 and %10 us module 10
    check = (10 - (total % 10)) % 10
    return body + str(check)


def validate_isbn13(isbn):
    # alternating weights 1 and 3, sum must be divisible by 10. 
    total = 0
    for i in range(13):
        #same logic as above but now we are checking if the index is even(leave as is) or odd(multiply by 3)
        if i % 2 == 0:
            total = total + int(isbn[i])
        else:
            total = total + int(isbn[i]) * 3

    # now we actually check if the total is divisible by 10
    if total % 10 == 0:
        return "Valid"
    else:
        return "Invalid"


# --- testing ---(Disclaimer. This part of the code is the ONLY section i involved AI. I didn't exactly know how to run the tests from my .py file.
if __name__ == "__main__":
    print("--- ISBN-10 Validation ---")
    test_isbns = ["0618260307", "0451524934", "0262033844", "0131103628",
                  "0132350882", "020161622X", "0201633612", "0735619670",
                  "0521642981", "0198538030"]

    for isbn in test_isbns:
        print(isbn, "->", validate_isbn10(isbn))

    print()
    print("--- Check Digit ---")
    print("061826030 ->", check_digit("061826030"))
    print("020161622 ->", check_digit("020161622"))

    print()
    print("--- Convert to ISBN-13 ---")
    print("0618260307 ->", convert_to_isbn13("0618260307"))

    print()
    print("--- ISBN-13 Validation ---")
    print("9780618260300 ->", validate_isbn13("9780618260300"))
