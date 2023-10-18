n=int(input("Enter the no."))
a=int(input("Enter the digit"))
count=0
while n!=0:
    d=n%10
    if d==a:
        count=count+1
    n=n//10
print(count)
