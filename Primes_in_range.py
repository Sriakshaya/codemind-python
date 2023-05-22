def prime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            
            return False
    else:
        return True
n=int(input())
m=int(input())
c=0
for j in range(n,m+1):
    if(j==1):
        continue
    if(prime(j)):
        c+=1
print(c)