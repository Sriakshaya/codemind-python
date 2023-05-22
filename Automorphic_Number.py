n=int(input())
l=len(str(n))
m=n*n
a=m%(10**l)
if a==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
