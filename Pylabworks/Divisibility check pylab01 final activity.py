"""Given an integer number and two divisors d1 and d2, we have to check whether number is divisible by d1 and d2 or not.

Input Format

Take an integer n whose divisibilty is to be checked.
Take the first divisor value d1.
Take the second divisor value d2.

"""

num=int(input("Take an integer n whose divisibilty is to be checked.:"))
d1=int(input("Take the first divisor value d1.:"))
d2=int(input("Take the second divisor value d2.:"))
if num%d1==0 and num%d2==0:
    print("Yes.")
else:
    print("No.")
