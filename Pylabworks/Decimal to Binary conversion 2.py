"""Read an integer number in Decimal and converts it into Binary Number System.

The logic behind to implement this program -

Get remainder using modulus operator by 2 and store it into an array then divide number by 2, repeat this process till given number is greater than 0. Because 2 is the base of Binary Number System."""

n=int(input())
a=bin(n).replace("0b", "")
print(a)
