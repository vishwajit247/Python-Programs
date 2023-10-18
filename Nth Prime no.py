n=int(input())
c=0
m=2
while True:
    for i in range(2,m):
        if m%i==0:
            break
    else:
        c=c+1
        print(m)
        if c==n:
            print(f'{n}th terms is: {m}')
            break
    m=m+1
