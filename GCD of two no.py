a=int(input())
b=int(input())
while True:
    r=a%b
    if r==0:
        print(b)
        break
    a,b=b,r
