import math
n=int(input())
for i in range(n):
    s=int(math.sqrt(n))
if s*s==n:
    print("True")
else:
    print("False")