a=int(input())
b=int(input())
while True:
    r=a%b
    if r==0:
        break
    a,b=b,r
if b==1:
    print("Co-prime")
else:
    print("Not Co-prime")
