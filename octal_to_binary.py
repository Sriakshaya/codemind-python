n=int(input())
i=0
r=0
while n:
    d=n%10
    r+=d*(8**i)
    i+=1
    n=n//10
print(bin(r)[2:])
