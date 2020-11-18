"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest.
If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""

def divisors(integer):
    i = 2
    list = []
    while integer > i:
        if integer % i == 0:
            list.append(i)
        i = i + 1
    if not list:
        return f"{integer} is prime"
    else:
        return list
