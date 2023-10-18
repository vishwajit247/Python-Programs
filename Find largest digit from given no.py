n=int(input())
a=0
while n!=0:
    d=n%10
    if d>a:
        a=d
    n=n//10
print(a)
