n=int(input())
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%02d"%(c),end=" ")
        c=c+1
    print()
