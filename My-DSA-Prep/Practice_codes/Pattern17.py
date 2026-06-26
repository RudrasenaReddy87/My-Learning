n = int(input())
for i in range(n):
    for j in range(n):
        if (i>=1 and i<=(n-2)):
            if j==0 or j==(n-1):
                print("*",end='')
            else:
                print(" ",end='')
        else:
            print("*",end='')
    print()