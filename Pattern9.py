n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    for j in range(n-1,0,-1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    for j in range(n-1,0,-1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
