m=int(input())
while True:
    for i in range(2,m):
        if m%i==0:
            m=m+1
            break
    else:
        print(m)
        break
