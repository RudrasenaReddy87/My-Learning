n = int(input())
for i in range(n):
    s = ' '
    for j in range(n-i,0,-1):
        s=str(j)+s
    print(s)

# we need to decrese at end i mean 1,2,3,4,5 \ 1,2,3,4
# so i changed like inner loop