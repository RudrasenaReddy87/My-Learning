n = int(input())
c = 1
for i in range(1,n+1):
    for j in range(c,i+c):
        print(j,end=' ')
        c += 1
    print()