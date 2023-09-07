"""Write a program for given three integers a, b, and x, display a if x is 1 and b if x is 0, using only mathematical or bitwise operations. Assume x can only be 1 or 0.

Note: flow control statements not allowed (if-else and loops not allowed)"""

a=int(input("first integer value of a:"))
b=int(input("second integer value of b:"))
x=int(input("third integer value of x:"))
result=(a*x)+b*(1-x)
print(result)
