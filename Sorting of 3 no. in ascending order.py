a,b,c=map(int,input().split())
if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>c:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if a>b:
        print(b,a,c)
    else:
        print(a,c,b)
