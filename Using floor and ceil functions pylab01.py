"""Use of floor and ceil functions on floating point values.

Both functions are library functions and declare in math.h header file. Floor ignores the fraction part and just print the same in floating point.

E.g.

floor(123.46) then it will return 123.000000

ceil(123.46) then it will return 124.000000"""

import math
num=float(input("ENTER NUMBER :"))
q=math.floor(num)
s=math.ceil(num)
print(q,".000000",sep="")
print(s,".000000",sep="")
