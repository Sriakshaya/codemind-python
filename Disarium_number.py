n=input()
s=0
a=1
for i in n:
    s=s+int(i)**a
    a+=1
print(s==int(n))