"""Write a program for given an integer n, perform the following conditional actions:


If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""

num= int(input())
if num%2!=0:
    print("Weird")  
elif num%2==0 and 2<=num<=5:
    print("Not Weird")
elif num%2==0 and 6<=num<=20:
    print("Weird")
elif num%2==0 and num>20:
    print("Not Weird")
